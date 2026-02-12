#!/usr/bin/env python3

import uproot
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Open ROOT file and read blip energy
# -----------------------------
file = uproot.open("/home/shana/000001_ana_hist_2025-06-03T_003735Z.root")
tree = file["pdblipana/anatree"]

# Read and flatten blip energy
blip_energy = tree["blip_energy"].array(library="np")
blip_energy = np.concatenate(blip_energy)

# -----------------------------
# Create histogram
# -----------------------------
bins = 100
range_min, range_max = 0, 5
counts, bin_edges = np.histogram(blip_energy, bins=bins, range=(range_min, range_max))
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])

# Poisson errors
errors = np.sqrt(counts)
errors[errors == 0] = 1  # avoid division by zero

# -----------------------------
# Simple Gaussian fit using NumPy
# -----------------------------
# Estimate peak and width
mu_est = bin_centers[np.argmax(counts)]
sigma_est = np.sqrt(np.sum(counts * (bin_centers - mu_est)**2) / np.sum(counts))
A_est = max(counts)

# Create Gaussian curve with estimated parameters
def gaussian_np(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / (2 * sigma**2))

fit_curve = gaussian_np(bin_centers, A_est, mu_est, sigma_est)

# -----------------------------
# Plot histogram with Gaussian curve
# -----------------------------
plt.figure(figsize=(8,6))
plt.hist(blip_energy, bins=bins, range=(range_min, range_max), histtype="step", label="Data")
plt.errorbar(bin_centers, counts, yerr=errors, fmt='o', color='black', markersize=3, alpha=0.5)
plt.plot(bin_centers, fit_curve, 'r-', label=f"Approx. Gaussian: mu={mu_est:.2f}, sigma={sigma_est:.2f}")
plt.xlabel("Blip Energy [MeV]")
plt.ylabel("Entries")
plt.title("Blip Energy Distribution with Approx. Gaussian")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("blip_energy_fit_numpy.pdf")
plt.show()
