"""
plot gamma spectra
"""
from pyne import fispact
import matplotlib.pyplot as plt
import sys
import argparse


def plot_spectra_groups(fo, ts, save=False, sfile=""):
    """ plot gamma spectra in group wise"""

    plt.plot()
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot gamma spectra for a given timestep from a fispact output file")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("timestep", help="timestep number to plot", default=1, type=int )
    parser.add_argument("-o", "--output", action="store", dest="output",  help="path to the output file without filetype")

    args = parser.parse_args()
    fo = fispact.read_fis_out(args.input)
    if args.output:
        plot_spectra_groups(fo, args.timestep, True, args.output)
    else:
        plot_spectra_groups(fo, args.timestep)
