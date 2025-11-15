# Sn_Pb_Perovskite_Oxygen_Degradation_MD
Repository created as a reproducible demo for:
"Molecular Dynamics Insights into Oxidation and Structural Degradation Pathways in Sn-containing Perovskites"
Note: This repository contains **example** data and scripts for reproducibility demonstrations.
Full raw trajectory datasets used in the published manuscript are archived offline and are available from the corresponding author upon reasonable request (see Data Availability statement).

## Repository structure
- input_files/: LAMMPS input scripts and data file placeholders
- example_trajectory/: short example trajectory (LAMMPS dump format)
- processed_data/: example RDF, MSD, Arrhenius and structural metric files
- scripts/: Python scripts and notebooks used to process data
- snapshots/: coordinate frames used for figure rendering
- docs/: Documentation, Data Availability, Response-to-Editor

## How to run the demo analysis (example)
1. Ensure Python 3.8+ with numpy is installed.
2. From repository root:
   - `python3 scripts/rdf_analysis.py`
   - `python3 scripts/msd_analysis.py`
   - `python3 scripts/arrhenius_fit.py`

## How to run LAMMPS (example)
This repository contains an example LAMMPS input (input_files/in.mapbsn_o2) and a placeholder data file.
To run with LAMMPS (3 Mar 2025):
```
mpirun -np 8 lmp -in input_files/in.mapbsn_o2
```
Note: The provided MAPbSn_O2_3x3x3.data is a placeholder; replace with the original production data for full reproduction.

## Data Availability
Full raw trajectory datasets (>10 GB) are archived offline due to storage limits and are available from the corresponding author upon reasonable request. Processed datasets and analysis scripts are available in this repository.

## License
CC BY 4.0
