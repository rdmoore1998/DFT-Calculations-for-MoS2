# DFT-Calculations-for-MoS2
Introduction for running DFT calculation on MoS2 through QE. Here we run structural optimization (vc-relax), self consistant field calculations, DOS/PDOS, Band Structures, and Phonon Dispersions. 

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
