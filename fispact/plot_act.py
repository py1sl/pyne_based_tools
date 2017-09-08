from pyne import fispact
import matplotlib.pyplot as plt
import sys
import argparse


def plot_act(fo, leg=[], save=False, sfile=""):
    """ plot activity as log plot"""

    plt.plot(fo.sumdat[0], fo.sumdat[1])
    plt.yscale('log')
    
    if len(leg)>1:
       plt.legend(leg)
    plt.xlabel("Time (years)")
    plt.ylabel("Activity (Bq)")
    
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)
    

def plot_acts(fo_list, leg=[], save=False, sfile=""):
    """ plot activity for several fispact objects as log plot"""

    for fo in fo_list:
        plt.plot(fo.sumdat[0], fo.sumdat[1])
    plt.yscale('log')
    plt.xlabel("Time (years)")
    plt.ylabel("Activity (Bq)")
    
    if len(leg)>1:
       plt.legend(leg)
    
    if save == False:
        plt.show()
    else:
        plt.savefig(sfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot activity over time for a fispact output file")
    parser.add_argument("input", help="path to the input file")
    parser.add_argument("-o", "--output", action="store", dest="output",  help="path to the output file")
    args = parser.parse_args()
    fo = fispact.read_fis_out(args.input)
    if args.output:
        plot_act(fo, [],  True, args.output)
    else:
        plot_act(fo)

