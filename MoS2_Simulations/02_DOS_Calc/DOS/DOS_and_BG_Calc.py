import matplotlib.pyplot as plt
import numpy as np

# Load band structure data
data = np.loadtxt('MoS2_dos_MonoLayer.dat')
# Monolayer: -2.0913, 1L: -1.0111, 2L: 3.2502, 3L: 3.7916, 4L: 5.2282, Bulk: 8.5808 eV
Energy = data[:, 0] -(-2.0913)  # Energy - Fermi Energy
DOS = data[:, 1]          # DOS

plt.figure(figsize=(7,5))
# Plot each band
plt.plot(Energy, DOS,  color='red', label='Total DOS')
plt.axvline(x=0, color='black', linestyle='--', label='Fermi Level')

plt.xlabel('Energy [eV]',fontsize=18)
plt.ylabel('DOS [States/eV]',fontsize=18)
plt.title('MoS2 DOS',fontsize=20)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.grid(False)
plt.legend()
plt.show()
plt.savefig("DOS.png",dpi=300)



# Define threshold
threshold = 0.01  # states/eV

# Identify VBM
# Iterate from lower energies upwards to find the last energy below 0 eV with DOS > threshold
VBM = None
for energy, density in zip(Energy[::-1], DOS[::-1]):
    if energy < 0 and density > threshold:
        VBM = energy
        break

# Identify CBM
# Iterate from higher energies downwards to find the first energy above 0 eV with DOS > threshold
CBM = None
for energy, density in zip(Energy, DOS):
    if energy > 0 and density > threshold:
        CBM = energy
        break

# Calculate band gap
if VBM is not None and CBM is not None:
    E_gap = CBM - VBM
    print(f"Valence Band Maximum (VBM): {VBM:.3f} eV")
    print(f"Conduction Band Minimum (CBM): {CBM:.3f} eV")
    print(f"Band Gap: {E_gap:.3f} eV")
else:
    print("Unable to determine VBM and/or CBM with the given threshold.")
