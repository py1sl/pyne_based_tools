import sys
import glob

from pyne import gammaspec as gs
from pyne import spectanalysis as sa

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np


def plot_2dintensity(path):
    """ """
    files=glob.glob(path+"/*.Spe")
    times = []
    cps_data = []

    for f in files:
        spec=gs.read_dollar_spe_file(f)
        times.append(spec.start_time)
        lt=spec.live_time
        cps=np.array(spec.counts)/lt
        cps_data.append(cps)
        ebin=np.array(spec.ebin)

    cps_data=np.array(cps_data)
    cps_data=cps_data.T
    times=np.array(times)

    fig, ax = plt.subplots()
    cax=ax.pcolormesh(np.arange(0,10), ebin, cps_data, norm=LogNorm())
    ax.set_xlabel("Real_time(minutes)")
    ax.set_ylabel("Energy (KeV)")
    ax.set_title("Count rate ")
    cb=fig.colorbar(cax)
    plt.show()
