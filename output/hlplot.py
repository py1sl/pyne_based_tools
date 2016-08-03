import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pyne import nucname, nuc_data
import tables as tb

f=tb.openFile(nuc_data)
anums=map(nucname.anum, f.root.decay.level_list[:]['nuc_id'])

plt.semilogy(anums, f.root.decay.level_list[:]['half_life'], 'bo')
plt.xlabel('A')
plt.ylabel('half-life (s)')
plt.show()
