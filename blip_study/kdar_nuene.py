import numpy as np
import matplotlib.pyplot as plt
import awkward as ak

# -----------------------------
# 1. Simulate events
# -----------------------------
num_events = 500  # total number of events

# Each event has a random number of blips (1-10)
num_blips_per_event = np.random.randint(1, 11, size=num_events)

# Create jagged array of blip energies (MeV)
blip_energy = [np.random.normal(loc=50 + 200*np.random.rand(), scale=20, size=n) 
               for n in num_blips_per_event]

# Create jagged arrays for blip charge and size
blip_charge = [np.random.uniform(0, 200, size=n) for n in num_blips_per_event]
blip_size   = [np.random.randint(1, 5, size=n) for n in num_blips_per_event]

# Convert to awkward arrays
blip_energy = ak.Array(blip_energy)
blip_charge = ak.Array(blip_charge)
blip_size   = ak.Array(blip_size)

# -----------------------------
# 2. Apply selection cuts
# -----------------------------
blip_mask = (
    (blip_energy > 50) &
    (blip_energy < 500) &
    (blip_charge > 0) &
    (blip_size >= 1)
)

blip_energy_sel = blip_energy[blip_mask]

# -----------------------------
# 3. Compute event-level visible energy
# -----------------------------
event_visible_energy = ak.sum(blip_energy_sel, axis=1)
event_visible_energy = event_visible_energy[event_visible_energy > 0]
event_visible_energy = ak.to_numpy(event_visible_energy)

# -----------------------------
# 4. Plot KDAR energy histogram
# -----------------------------
plt.figure(figsize=(8,6))
plt.hist(event_visible_energy, bins=50, range=(0,600), histtype='step', color='blue', label="Events")
plt.axvline(236, color='red', linestyle='--', label="KDAR νµ expected energy")
plt.xlabel("KDAR Neutrino Energy [MeV]")
plt.ylabel("Number of events")
plt.title("KDAR Muon Neutrino Energy")
plt.legend()
plt.show()
