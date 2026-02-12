#!/usr/bin/env python3

import uproot
import numpy as np
import matplotlib.pyplot as plt

# Open ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read blip energy
blip_energy = tree["blip_energy"].array(library="np")
blip_energy = np.concatenate(blip_energy)

# Plot
plt.figure(figsize=(8,6))
plt.hist(blip_energy, bins=100, range=(0,5), histtype="step")
plt.xlabel("Energy (MeV)")
plt.ylabel("Entries")
plt.title("Blip Energy Distribution")

# Save output
plt.savefig("blip_energy.pdf")
plt.show()
