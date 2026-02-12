import uproot
import awkward as ak
import matplotlib.pyplot as plt

# Open file and tree
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read variables
blip_energy = ak.flatten(tree["blip_energy"].array())
blip_size   = ak.flatten(tree["blip_size"].array())

# Correlation plot
plt.figure(figsize=(7,5))
plt.scatter(blip_energy, blip_size, s=2, alpha=0.4)
plt.xlabel("Blip Energy [MeV]")
plt.ylabel("Blip Size [ticks]")
plt.title("Correlation: Blip Energy vs Blip Size")
plt.show()
