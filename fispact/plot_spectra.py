"""
plot gamma spectra
"""
from pyne import fispact
import matplotlib.pyplot as plt
import sys


def plot_spectra_groups(fo, ts, save=False, sfile=""):
    """ plot gamma spectra in group wise"""

    plt.plot()
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    


if __name__ == "__main__":
    path = sys.argv[1]
    fo = fispact.read_fis_out(path)
    plot_spectra_groups(fo, 1)
