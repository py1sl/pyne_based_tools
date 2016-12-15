"""
plot composition 



"""
from pyne import fispact
import matplotlib.pyplot as plt
import sys


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
    path = sys.argv[1]
    fo = fispact.read_fis_out(path)
    plot_comp_pie(fo, 1)
