import uproot
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
# Access a tree
tree = file["pdblipana/anatree"]

# List all branches
print(tree.keys())
