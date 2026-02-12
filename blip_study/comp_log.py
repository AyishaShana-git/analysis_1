import uproot
import matplotlib.pyplot as plt
import numpy as np

# Open your ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")   

# Get the main analysis tree
tree = file["pdblipana/BlipRecoAlg/matchtree"]

# Read branches
qA = tree["qA"].array(library="np")
dt = tree["dt"].array(library="np")


# Event selection (cuts)
mask = (qA > 100) & (dt < 10)

print("Total entries:", len(qA))
print("Selected events:", mask.sum())


# Define common bins using ALL events
bins = np.linspace(qA.min(), qA.max(), 50)

# Before selection
plt.hist(qA, bins=bins, histtype="step", linewidth=2, label="Before selection")

# After selection
plt.hist(qA[mask], bins=bins, histtype="step", linewidth=2, label="After selection")

plt.xlabel("Charge qA")
plt.ylabel("Entries")
plt.title("qA: before vs after selection")
plt.legend()
plt.tight_layout()
plt.yscale('log')
plt.show()
