"""
plot composition 



"""
from pyne import fispact
import matplotlib.pyplot as plt
import sys
import argparse

def plot_comp_pie(fo, ts, save=False, sfile=""):
    """ formatter pie chart of elemental composition for a timestep"""

    plt.plot()
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    
def plot_comp_periodic():
    """ elemental composition for a timestep as a table of elements"""

    plt.plot()
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot activity over time for a fispact output file")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("timestep", help="timestep number to plot", default=1, type=int )
    parser.add_argument("-o", "--output", action="store", dest="output",  help="path to the output file without filetype")
    parser.add_argument("--table", action="store_true",  help="make a plot of the composition in form of table of elements")

    args = parser.parse_args()
    fo = fispact.read_fis_out(args.input)
    plot_comp_pie(fo, args.timestep)
