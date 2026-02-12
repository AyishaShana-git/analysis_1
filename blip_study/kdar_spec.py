import numpy as np
import matplotlib.pyplot as plt

m_K = 493.677
m_mu = 105.658

E_nu = (m_K**2 - m_mu**2) / (2 * m_K)
print(f"Expected KDAR neutrino energy: {E_nu:.2f} MeV")

# Energy axis
E = np.linspace(0, 300, 1000)

# Ideal monoenergetic spectrum (delta function represented as zero everywhere)
spectrum = np.zeros_like(E)

plt.figure()
plt.plot(E, spectrum)
plt.axvline(E_nu, linewidth=2, label=f"KDAR ν energy = {E_nu:.1f} MeV")
plt.xlabel("Neutrino Energy (MeV)")
plt.ylabel("Probability")
plt.title("Expected KDAR Neutrino Energy Spectrum (No Smearing)")
plt.legend()
plt.show()
