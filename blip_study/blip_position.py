import uproot
import numpy as np
import awkward as ak
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")   

tree = file["pdblipana/anatree"] 

x = tree["blip_x"].array()
y = tree["blip_y"].array()
z = tree["blip_z"].array()

x = ak.to_numpy(ak.flatten(x))
y = ak.to_numpy(ak.flatten(y))
z = ak.to_numpy(ak.flatten(z))  

print("Total blips:", len(x))


plt.figure(figsize=(8,6))
plt.scatter(z, x, s=2, alpha=0.5)
plt.xlabel("Z position (cm)")
plt.ylabel("X position (cm)")
plt.title("Blip Positions in Detector (X–Z View)")
plt.grid(True)
plt.show()
