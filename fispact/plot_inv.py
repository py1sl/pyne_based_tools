"""

Plots table of isotopes views for inventory at a given timestep
note: metastables above m not recognised by pyne nucname
note: when metastables and the stable element are present the 
      data is for metastale
Author:  S Lilley

"""

import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
import sys
from pyne import nucname, nuc_data, fispact


def plot_inv(fo, ts, low_limit=1e-5, save=False, sfile=""):
    """plots activity"""
    
    act_grid = np.zeros((113,173))

    for nuc in fo.timestep_data[ts-1].inventory:
         if float(nuc[3]) > 0:
            if nuc[0][-1] == "n":
                nuc[0] = nuc[0][:-1]
            #nuc[0]=nuc[0].replace(" ", "")
            
            a = nucname.anum(nuc[0])
            z = nucname.znum(nuc[0])
            n=a-z
            act_grid[z,n] = np.log10(float(nuc[3]))

    act_grid = np.ma.masked_array(act_grid, act_grid<low_limit)

    plt.pcolormesh(act_grid)
    plt.colorbar()
    plt.xlabel("N")
    plt.ylabel("Z")

    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    

if __name__ == "__main__":
    path = sys.argv[1]
    fo = fispact.read_fis_out(path)
    ts = int(sys.argv[2])
    plot_inv(fo, ts)

