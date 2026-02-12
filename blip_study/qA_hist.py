import uproot
import numpy as np
import matplotlib.pyplot as plt

# Open the ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")

# Open the analysis tree
tree = file["pdblipana/BlipRecoAlg/matchtree"]
  

# Read qA branch
qA = tree["qA"].array(library="np")

# Basic sanity check
print("Total entries:", len(qA))
print("qA range:", np.min(qA), "to", np.max(qA))

# Plot histogram
plt.figure()
plt.hist(qA, bins=50)
plt.xlabel("Charge qA")
plt.ylabel("Entries")
plt.title("Charge (qA) Distribution")
plt.tight_layout()
plt.show()
