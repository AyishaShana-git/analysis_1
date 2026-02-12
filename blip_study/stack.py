import uproot
import numpy as np
import matplotlib.pyplot as plt

# Open ROOT file
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/BlipRecoAlg/matchtree"]

# Read branches
qA = tree["qA"].array(library="np")
dt = tree["dt"].array(library="np")

# Define categories (example: based on time cut)
signal = qA[dt < 10]     # events passing cut
background = qA[dt >= 10]  # events failing cut

# Plot stacked histogram
bins = 50
range_min, range_max = 0, 500

plt.figure(figsize=(8,6))
plt.hist([background, signal],
         bins=bins,
         range=(range_min, range_max),
         stacked=True,
         label=["Background (dt ≥ 10)", "Signal (dt < 10)"])

plt.xlabel("Charge (qA)")
plt.ylabel("Events")
plt.title("Stacked Charge Distribution")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("stacked_histogram.png", dpi=300)
plt.show()
