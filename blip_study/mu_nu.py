import matplotlib.pyplot as plt

kdar_energy = 236
plt.figure(figsize=(8,6))
plt.axvline(kdar_energy, color='red', linestyle='--', linewidth=2,
            label="KDAR νµ energy = 236 MeV")

plt.xlabel("Muon neutrino energy [MeV]")
plt.ylabel("Number of Events")
plt.title("Expected KDAR Muon Neutrino Energy")
plt.legend()
plt.xlim(0, 500)
plt.ylim(0, 10)
plt.show()
