import uproot

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root") 

for name, obj in file.items():
    if isinstance(obj, uproot.behaviors.TTree.TTree):
        print("TREE:", name)
