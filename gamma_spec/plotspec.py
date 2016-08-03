""" simple  gamma spec plotting
"""
from pyne import gammaspec as gs

import matplotlib.pyplot as plt
import sys

def plot_spec(spec, save=False, sfile=""):
    """ plot spectrum as log plot"""
    plt.plot(spec.ebin, spec.counts)
    plt.yscale('log')
    plt.xlabel("Energy (keV)")
    plt.ylabel("counts")
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)

if __name__ == "__main__":
    path=sys.argv[1]
    spec1=gs.read_dollar_spe_file(path)
    plot_spec(spec1)
