"""
produces a short pdf report with spectra and list of peaks, via latex
"""

import sys
import plot_intensity

from pyne import gammaspec as gs
from pyne import spectanalysis as sa

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

path="/mnt/hgfs/transfer/imat"

plot_intensity.plot_2dintensity(path)







