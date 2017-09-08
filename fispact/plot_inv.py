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
import argparse


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
    title = fo.sumdat[0][ts-1]
    make_plot(atom_grid, title, save, sfile)


def make_plot(data, title, save, sfile):
    """ makes the plot    """
    plt.clf()
    plt.pcolormesh(data)
    plt.colorbar()
    plt.xlabel("N")
    plt.ylabel("Z")
    plt.title(title)

    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot dominant for a given timestep from a fispact output file")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("timestep", help="timestep number to plot", default=1, type=int )
    parser.add_argument("-o", "--output", action="store", dest="output",  help="path to the output file")

    args = parser.parse_args()
    fo = fispact.read_fis_out(args.input)
    if args.output:
        plot_inv_para(fo, args.timestep, 1, 1e-10, True, args.output)
    else:
        plot_inv_para(fo, args.timestep, 1)

