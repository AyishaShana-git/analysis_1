import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

blip_energy = tree["blip_energy"].array()
blip_energy = ak.flatten(blip_energy)

counts, bin_edges = np.histogram(blip_energy, bins=50)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
errors = np.sqrt(counts)

plt.hist(blip_energy, bins=bin_edges, histtype="step", label="Histogram")
plt.errorbar(bin_centers, counts, yerr=errors, fmt='o', label="Stat. error")

plt.xlabel("Blip Energy (MeV)")
plt.ylabel("Entries")
plt.legend()
plt.show()

