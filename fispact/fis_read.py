from pyne import fispact
import matplotlib.pyplot as plt
import numpy as np


path = "/home/steve/opt/pyne/tests/fispii.out"
fo = fispact.read_fis_out(path)
ts1 = fo.timestep_data[1]
ts2 = fo.timestep_data[5]
ts3 = fo.timestep_data[-1]

inv=ts3.inventory

print inv[0]




print "Done"

