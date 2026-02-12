import uproot
import numpy as np
import matplotlib.pyplot as plt
import awkward as ak

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]
blip_energy = tree["blip_energy"].array()
event_visible_energy = ak.sum(blip_energy, axis=1)

peak_window = (event_visible_energy > 5) & (event_visible_energy < 300)
peak_data = event_visible_energy[peak_window]
mu = np.mean(peak_data)
sigma = np.std(peak_data)

resolution = (sigma / mu) * 100

print(f"Mean energy (mu) = {mu:.2f} MeV")
print(f"Sigma (width) = {sigma:.2f} MeV")
print(f"Energy Resolution = {resolution:.2f} %")
# Histogram
counts, bins, _ = plt.hist(peak_data, bins=40, density=True,
                           histtype='step', label="Data")

# Gaussian curve using calculated mu & sigma
x = np.linspace(180, 300, 500)
gaussian = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/sigma)**2)

plt.plot(x, gaussian, label="Gaussian Approximation")

plt.xlabel("Reconstructed Energy [MeV]")
plt.ylabel("Normalized Entries")
plt.title("KDAR Energy Peak and Resolution")
plt.legend()
plt.show()
