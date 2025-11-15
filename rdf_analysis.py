# rdf_analysis.py
# Example script to read rdf_Sn_I.dat and plot or process peak fits.
import numpy as np
data = np.loadtxt('processed_data/rdf_Sn_I.dat', comments='#')
r = data[:,0]; g = data[:,1]
imax = g.argmax()
print(f'Peak at r = {r[imax]:.3f} Å, g = {g[imax]:.3f}')
