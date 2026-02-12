import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read and flatten
blip_energy = ak.flatten(tree["blip_energy"].array())
blip_size   = ak.flatten(tree["blip_size"].array())

# Convert to NumPy
blip_energy = ak.to_numpy(blip_energy)
blip_size   = ak.to_numpy(blip_size)

# 2D correlation plot
plt.figure(figsize=(7,5))
plt.hist2d(blip_energy, blip_size, bins=50)
plt.xlabel("Blip Energy [MeV]")
plt.ylabel("Blip Size [ticks]")
plt.title("Blip Energy vs Blip Size")
plt.colorbar(label="Entries")
plt.show()

