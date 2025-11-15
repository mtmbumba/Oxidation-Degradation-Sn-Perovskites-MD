# arrhenius_fit.py
import numpy as np
data = np.loadtxt('processed_data/lnD_vs_1overT.dat', comments='#')
invT = data[:,0]; lnD = data[:,1]
coef = np.polyfit(invT, lnD, 1)
slope = coef[0]; intercept = coef[1]
print(f'Arrhenius fit slope = {slope:.6f}, intercept = {intercept:.6f}')
