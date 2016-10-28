from pyne import fispact
import matplotlib.pyplot as plt
import sys


def plot_act(fo, save=False, sfile=""):
    """ plot activity as log plot"""

    plt.plot(fo.sumdat[0], fo.sumdat[1])
    plt.yscale('log')
    plt.xlabel("Time (years)")
    plt.ylabel("Activity (Bq)")
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    

def plot_acts(fo_list, save=False, sfile=""):
    """ plot activity for several fispact objects as log plot"""

    for fo in fo_list:
        plt.plot(fo.sumdat[0], fo.sumdat[1])
    plt.yscale('log')
    plt.xlabel("Time (years)")
    plt.ylabel("Activity (Bq)")
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)


if __name__ == "__main__":
    path = sys.argv[1]
    fo = fispact.read_fis_out(path)
    plot_act(fo)

