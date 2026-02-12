import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

blip_energy = tree["blip_energy"].array()
blip_size   = tree["blip_size"].array()
blip_time   = tree["hit_time"].array()
n_blips = ak.num(blip_energy)
event_total_energy = ak.sum(blip_energy, axis=1)
event_max_energy = ak.max(blip_energy, axis=1)
plt.hist(n_blips, bins=20)
plt.xlabel("Number of blips per event")
plt.ylabel("Events")
plt.show()

plt.hist(event_total_energy, bins=50)
plt.xlabel("Total event energy [MeV]")
plt.ylabel("Events")
plt.show()
signal_mask = (
    (n_blips < 10) &
    (event_total_energy > 2) &
    (event_total_energy < 10) &
    (event_max_energy < 5)
)
signal_energy = event_total_energy[signal_mask]
background_energy = event_total_energy[~signal_mask]
plt.hist(signal_energy, bins=40, alpha=0.7, label="Signal-like")
plt.hist(background_energy, bins=40, alpha=0.5, label="Background-like")
plt.xlabel("Event total energy [MeV]")
plt.ylabel("Events")
plt.legend()
plt.title("Event Classification using Simple Cuts")
plt.show()
total_events = len(event_total_energy)
selected_events = ak.sum(signal_mask)

print("Total events:", total_events)
print("Signal-like events:", selected_events)
print("Selection efficiency:", selected_events / total_events)

