from pyne import fispact
import matplotlib.pyplot as plt
import sys


def plot_dominant(fo, ts, save=False, sfile=""):
    """ formatter pie chart of dominant nuclides for a timestep"""

    plt.plot()
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    


if __name__ == "__main__":
    path = sys.argv[1]
    fo = fispact.read_fis_out(path)
    plot_dominant(fo, 1)
