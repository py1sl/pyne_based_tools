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


def plot_inv_act_para(fo, ts, para, low_limit=1e-5, save=False, sfile=""):
    """plots parameter as table of nuclides form for a timestep
       this is for active parameters
    """
    
    act_grid = np.zeros((113,173))

    for nuc in fo.timestep_data[ts-1].inventory:
         if float(nuc[para]) > 0:
            if nuc[0][-1] == "n":
                nuc[0] = nuc[0][:-1]
            
            a = nucname.anum(nuc[0])
            z = nucname.znum(nuc[0])
            n=a-z
            act_grid[z,n] = np.log10(float(nuc[para]))

    act_grid = np.ma.masked_array(act_grid, act_grid<low_limit)
    make_plot(act_grid, save, sfile)


def plot_inv_para(fo, ts, param, low_limit=1e-10, save=False, sfile=""):
    """plots parameter as table of nuclides for a timestep 
       this is for stable parameters only
    """

    atom_grid = np.zeros((113,173))

    for nuc in fo.timestep_data[ts-1].inventory:
         if nuc[0][-1] == "n":
             nuc[0] = nuc[0][:-1]
         
         a = nucname.anum(nuc[0])
         z = nucname.znum(nuc[0])
         n=a-z
         atom_grid[z,n] = np.log10(float(nuc[param]))

    atom_grid = np.ma.masked_array(atom_grid, atom_grid<low_limit)
    make_plot(atom_grid, save, sfile)


def make_plot(data, save, sfile):
    """ makes the plot    """
    plt.pcolormesh(data)
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
    plot_inv_act_para(fo, ts, 3)

