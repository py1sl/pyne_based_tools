from pyne.endf import Library
import matplotlib.pyplot as plt
import sys




def plotxs(path):

    lib = Library(path)
    xs_data = lib.get_xs(922350000, 16)[0]
    fig = plt.figure()
    Eints, sigmas = xs_data['e_int'], xs_data['xs']
    plt.step(Eints, sigmas, where = "pre")
    plt.suptitle(r'(n, 2n) Reaction in $^{235}$U')
    plt.ylabel(r'$\sigma(E)$ (barns)')
    plt.xlabel(r'$E_{int} (eV)$')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()



if __name__ == "__main__":
    path=sys.argv[1]
    plotxs(path)
