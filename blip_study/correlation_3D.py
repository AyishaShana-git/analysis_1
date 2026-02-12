import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read and flatten blip-level variables
blip_energy = ak.to_numpy(ak.flatten(tree["blip_energy"].array()))
blip_size   = ak.to_numpy(ak.flatten(tree["blip_size"].array()))
blip_charge = ak.to_numpy(ak.flatten(tree["blip_charge"].array()))

# Reduce number of points for faster plotting (optional)
sample = np.random.choice(len(blip_energy), size=10, replace=False)

# Create 3D figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# 3D correlation scatter
sc = ax.scatter(blip_energy[sample],
                blip_size[sample],
                blip_charge[sample],
                c=blip_energy[sample],   # color shows energy variation
                cmap='viridis',
                s=4, alpha=0.6)

ax.set_xlabel("Blip Energy [MeV]")
ax.set_ylabel("Blip Size [ticks]")
ax.set_zlabel("Blip Charge [ADC]")
ax.set_title("3D Correlation: Energy vs Size vs Charge")

plt.colorbar(sc, label="Energy [MeV]")
plt.show()
