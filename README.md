# DFT-Calculations-for-MoS2

# **MoS$_2$ Simulation Workflow: Electronic and Phonon Properties**
This repository contains Quantum ESPRESSO input files, scripts, and results for simulating the structural, electronic, and phonon properties of bulk and monolayer MoS$_2$.

The project involves **first-principles Density Functional Theory (DFT)** calculations to analyze:
1. **Structural Relaxation**
2. **Electronic Structure**: Band structure, DOS, PDOS.
3. **Vibrational Properties**: Phonon dispersion curves.

---

## **Repository Structure**
```plaintext
MoS2_Simulations/
│
├── 01_SCF/                         # Self-Consistent Field Calculations
│   ├── scf.in                      # Input file for SCF calculation
│   ├── scf.out                     # SCF output file
│   ├── charge-density              # Generated charge density file
│   └── notes.md                    # Notes on SCF convergence
│
├── 02_NSCF/                        # Non-Self-Consistent Field Calculations
│   ├── nscf.in                     # Input file for NSCF calculation
│   ├── nscf.out                    # NSCF output file
│   └── band_structure.dat          # Band structure data
│
├── 03_DOS/                         # Density of States
│   ├── dos.in                      # Input file for DOS calculation
│   ├── dos.out                     # DOS output file
│   ├── dos.dat                     # DOS data file
│   ├── pdos.in                     # Input file for PDOS calculation
│   ├── pdos.out                    # PDOS output file
│   └── plotting_scripts/           # Python scripts for plotting DOS/PDOS
│
├── 04_BandStructure/               # Band Structure Calculations
│   ├── bands.in                    # Input file for band structure
│   ├── bands.out                   # Output file for band calculation
│   ├── bands.dat.gnu               # Band structure data
│   ├── plotting_script.py          # Python script to plot the band structure
│   └── images/                     # Figures of band structure
│
├── 05_Phonons/                     # Phonon Calculations
│   ├── ph.in                       # Input file for phonon calculation
│   ├── ph.out                      # Phonon calculation output
│   ├── q2r.in                      # Input for Q2R
│   ├── matdyn.in                   # Input for MATDYN
│   ├── MoS2.fc                     # Force constant file
│   ├── MoS2.freq                   # Frequencies file
│   └── phonon_dispersion_plot.py   # Python script to plot phonon dispersion
│
├── results/                        # Final results and plots
│   ├── Band_Structure.png          # Band structure plot
│   ├── DOS.png                     # Total DOS plot
│   ├── PDOS.png                    # Projected DOS plot
│   └── Phonon_Dispersion.png       # Phonon dispersion plot
│
└── README.md                       # This file
```

---

## **Prerequisites**
To run these simulations, you will need:
- **Quantum ESPRESSO**: A suite of tools for DFT simulations.
- **Python**: For plotting results, with libraries:
  - `matplotlib`
  - `numpy`
- A working knowledge of Quantum ESPRESSO input/output files.

---

## **Workflow**

### **1. Self-Consistent Field (SCF) Calculation**
The SCF calculation determines the **ground-state electron density**.

#### **Input File: `scf.in`**
- **Purpose**: Solve the Kohn-Sham equations self-consistently.
- **Key Parameters**:
  - `ibrav=4`: Defines the hexagonal lattice.
  - `ecutwfc`: Plane-wave cutoff energy for wavefunctions.
  - `k-point grid`: 6x6x6 for bulk MoS$_2$.
  - Atomic positions and pseudopotentials.

#### **Execution**:
```bash
pw.x < scf.in > scf.out
```

---

### **2. Non-Self-Consistent Field (NSCF) Calculation**
The NSCF calculation generates **electronic eigenvalues** for a denser k-point grid, which is essential for DOS and band structure calculations.

#### **Input File: `nscf.in`**
- Reads charge density from the SCF step.
- Uses a finer k-point grid (e.g., 12x12x1).

#### **Execution**:
```bash
pw.x < nscf.in > nscf.out
```

---

### **3. Density of States (DOS) and Projected DOS (PDOS)**
The DOS describes the distribution of electronic states, while PDOS breaks it into atomic or orbital contributions.

#### **Input Files**:
- `dos.in` (Total DOS)
- `pdos.in` (Projected DOS)

#### **Execution**:
```bash
dos.x < dos.in > dos.out
projwfc.x < pdos.in > pdos.out
```

#### **Plotting**:
Use the Python scripts provided in `03_DOS/plotting_scripts/` to generate DOS/PDOS plots.

---

### **4. Band Structure Calculation**
The band structure visualizes electronic energy levels along high-symmetry paths in the Brillouin zone.

#### **Steps**:
1. Generate k-points along high-symmetry paths (e.g., $\Gamma \to M \to K \to \Gamma$).
2. Perform the band structure calculation with `bands.x`.

#### **Execution**:
```bash
bands.x < bands.in > bands.out
```

#### **Plotting**:
- Data is saved in `bands.dat.gnu`.
- Use the Python script `plotting_script.py` to plot the band structure.

---

### **5. Phonon Dispersion Calculation**
Phonon calculations provide vibrational frequencies across the Brillouin zone.

#### **Steps**:
1. Run `ph.x` to compute the **dynamical matrix**.
2. Use `q2r.x` to convert to **force constants**.
3. Interpolate phonon frequencies using `matdyn.x`.

#### **Execution**:
```bash
ph.x < ph.in > ph.out           # Phonon calculation
q2r.x < q2r.in > q2r.out        # Force constant conversion
matdyn.x < matdyn.in > matdyn.out  # Phonon dispersion
```

#### **Plotting**:
- Frequencies are stored in `MoS2.freq`.
- Use `phonon_dispersion_plot.py` to visualize the phonon dispersion.

---

## **Results**
- **Electronic Properties**:
  - Band structure reveals a **direct band gap** for monolayer MoS$_2$.
  - DOS and PDOS confirm orbital contributions near the Fermi level.

- **Vibrational Properties**:
  - Phonon dispersion confirms the **dynamical stability** of MoS$_2$.

---

## **References**
- Quantum ESPRESSO Documentation: [www.quantum-espresso.org](http://www.quantum-espresso.org)
- Key Papers:
  - Perdew, Burke, Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996) — PBE Functional.
  - MoS$_2$ Monolayer Band Structure: Mak et al., Phys. Rev. Lett. 105, 136805 (2010).

---
