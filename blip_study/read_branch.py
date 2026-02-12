import uproot
import numpy as np
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
# Access a tree
tree = file["pdblipana/anatree"]
hit_trkid = tree["hit_trkid"].array(library="np")
print(hit_trkid[:10])
