import uproot
import numpy as np
import awkward as ak
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]
blip_energy = tree["blip_energy"].array()
event_visible_energy = ak.sum(blip_energy, axis=1)


peak_window = (event_visible_energy > 5) & (event_visible_energy < 20)
peak_data = event_visible_energy[peak_window]

mu = np.mean(peak_data)
sigma = np.std(peak_data)

resolution = (sigma / mu) * 100

print(f"Mean energy (mu) = {mu:.2f} MeV")
print(f"Sigma (width) = {sigma:.2f} MeV")
print(f"Energy Resolution = {resolution:.2f} %")

