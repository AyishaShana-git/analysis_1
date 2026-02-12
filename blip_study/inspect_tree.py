import uproot
import numpy as np

#  Open the ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")

# See what is inside the file
print("\n=== Objects in ROOT file ===")
for key in file.keys():
    print(key)

#  Open the tree (change path if needed)
tree = file["pdblipana/anatree"]   # or BlipRecoAlg/matchtree

# Basic tree information
print("\n=== Tree info ===")
print("Number of entries:", tree.num_entries)

# List all branches in the tree
print("\n=== Branches in the tree ===")
for branch in tree.keys():
    print(branch)

#  Inspect one branch in detail
branch_name = "lifetime"   # change to any branch you want
branch = tree[branch_name]

print("\n=== Branch inspection ===")
print("Branch name:", branch_name)
print("Branch interpretation:", branch.interpretation)

# Load data from the branch
data = branch.array(library="np")

print("\n=== Data inspection ===")
print("Type:", type(data))
print("Shape:", data.shape)
print("First 10 entries:", data[:10])
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Mean:", np.mean(data))

