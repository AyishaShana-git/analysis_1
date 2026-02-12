#!/usr/bin/env python3

import uproot
import numpy as np
import matplotlib.pyplot as plt

file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read blip time
blip_time = tree["hit_time"].array(library="np")
blip_time = np.concatenate(blip_time)

plt.figure(figsize=(8,6))
plt.hist(blip_time, bins=200, range=(0,5000), histtype="step", label="All events")

# Selection window (example)
plt.axvspan(200, 350, alpha=0.2, label="Selection window")

plt.xlabel("Time (ticks)")
plt.ylabel("Entries")
plt.title("Blip Time Distribution")
plt.legend()

plt.savefig("blip_time.pdf")
plt.show()
