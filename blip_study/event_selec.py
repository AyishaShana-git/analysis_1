import uproot
import awkward as ak
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read as awkward arrays (correct for blips)
blip_energy = tree["blip_energy"].array()

blip_size   = tree["blip_size"].array()

# Blip-level KDAR selection
blip_mask = (
    (blip_energy > 200) &
    (blip_energy < 300) &
    (blip_size >= 2) &
    (blip_size <= 10)
)

# Select blips
blip_energy_sel = blip_energy[blip_mask]

# Flatten for histogram
plt.hist(ak.flatten(blip_energy_sel), bins=50)
plt.xlabel("Blip Energy (MeV)")
plt.ylabel("Entries")
plt.title("Selected KDAR blips")
plt.show()
