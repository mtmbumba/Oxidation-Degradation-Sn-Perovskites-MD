# msd_analysis.py
# Example script to read msd data and extract diffusion coefficient via linear fit
import numpy as np
data = np.loadtxt('processed_data/msd_O2_raw.dat', comments='#')
t = data[:,0]; msd = data[:,1]
# simple linear fit over whole range (illustrative)
coef = np.polyfit(t, msd, 1)
slope = coef[0]
D = slope / 6.0  # 3D Einstein relation: msd = 6 D t (t in same units)
print(f'Estimated D = {D:.4e} A^2/ps (convert units as needed)')
