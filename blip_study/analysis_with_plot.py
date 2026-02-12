import uproot
import numpy as np
import matplotlib.pyplot as plt

# Open ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")

# Get match tree
tree = file["pdblipana/BlipRecoAlg/matchtree"]

# Read branches
qA = tree["qA"].array(library="np")
dt = tree["dt"].array(library="np")

# Event-by-event cuts
mask = (qA > 100) & (dt < 10)

print("Total entries:", len(qA))
print("Selected events:", mask.sum())

# PLOTTING (ADD HERE)
plt.hist(qA[mask], bins=50)
plt.xlabel("Charge qA")
plt.ylabel("Entries")
plt.title("Selected blips")
plt.tight_layout()
plt.show()
