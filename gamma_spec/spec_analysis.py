#
#
import sys
import plot_intensity
import plotspec
import spec_anal

from pyne import gammaspec as gs
from pyne import spectanalysis as sa

from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import glob
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

"""
path="/mnt/hgfs/transfer/before.spe"
spec1=gs.read_dollar_spe_file(path)
spec2=sa.five_point_smooth(spec1)
spec2=sa.five_point_smooth(spec2)
spec2=sa.five_point_smooth(spec2)
spec2=sa.five_point_smooth(spec2)
spec2=sa.five_point_smooth(spec2)

diff_list=[]
diff_list.append(spec2.counts[0])
diff_list.append(spec2.counts[1])
diff_list.append(spec2.counts[2])
sd_list = []
sd_list.append(np.sqrt(spec2.counts[0]))
sd_list.append(np.sqrt(spec2.counts[1]))
sd_list.append(np.sqrt(spec2.counts[2]))

i=3
while i<len(spec2.counts)-2:
    diff=(spec2.counts[i-1]-2.0*spec2.counts[i]+spec2.counts[i+1])
    diff=np.sqrt(diff*diff)
    if diff < 0.001:
        diff = 0.0
    diff_list.append(diff)

    sd = np.sqrt(spec2.counts[i-1]+4.0*spec2.counts[i]+spec2.counts[i+1])
    sd_list.append(sd)
    i=i+1
diff_list.append(spec2.counts[-2])
diff_list.append(spec2.counts[-1])
sd_list.append(np.sqrt(spec2.counts[-2]))
sd_list.append(np.sqrt(spec2.counts[-1]))

peak_list=[]
ucert_list = []
tol=0.10
i=0
print "peaks"
while i < len(diff_list):
    uncert = np.sqrt(spec2.counts[i]) 
    ucert_list.append(uncert)
    if diff_list[i] > 0.0 and diff_list[i] < tol * sd_list[i]:
        erg=gs.channel_to_erg(spec2, i)

        peak_list.append(erg)
    i=i+1

# print peak_list
print len(peak_list)

"""

def peak_fit1(peak_en, spect, nchan=20):
    """Peak fit with gaussian using curve fit 
       
       assumes that peak energy is close to peak and that n channel
       does not contain a higher peak
    """

    peak_pos = gs.erg_to_channel(spect, peak_en)
    print "erg="+ str(peak_en)
    print "peak_pos="+str(peak_pos)
    
    ch1 = peak_pos - (nchan / 2)
    ch2 = ch1 + nchan-1

    print "chanel 1="+ str(ch1)
    print "chanel 2="+ str(ch2)
    
    xdata = spect.ebin[ch1:ch2]
    ydata = spect.counts[ch1:ch2]
    mean=peak_en


    # perform a check if peak pos is actually the peak
    # reposition if not
    maxy=max(ydata)
    peak_en_temp=xdata[np.where(ydata==maxy)]
    peak_pos_temp=gs.erg_to_channel(spect, peak_en_temp[0])
    if peak_pos_temp!=peak_pos:
       
        peak_pos=peak_pos_temp
        ch1 = peak_pos - (nchan / 2)
        ch2 = ch1 + nchan - 1
        xdata = spect.ebin[ch1:ch2]
        ydata = spect.counts[ch1:ch2]
        mean=peak_en_temp[0]
   
    # remove background before fitting
    bg=sa.calc_bg(spect, ch1, ch2)
    ave_bg=bg/(nchan*1.0)
    stripped_ydata=[]
    for i in ydata:
        stripped_ydata.append(i-ave_bg)
    ydata=stripped_ydata
    
    sig = sum((xdata - mean)**2) / (nchan*1.0)
    
    popt, pcov = curve_fit(sa.gauss,xdata,ydata,p0 = [max(ydata), mean, sig])
    area = sum(sa.gauss(xdata, *popt))

    return area, popt, pcov


def sum_spect(path):
    files = glob.glob(path+"/*.Spe")
    sum_spec = np.zeros( (8192))
    lt = 0

    for f in files:
        spec=gs.read_dollar_spe_file(f)
        new_spec=spec
        lt=lt + spec.live_time
        i=0
        while i < len(sum_spec):
            sum_spec[i] = sum_spec[i] + spec.counts[i]
            
            i = i + 1

    new_spec.counts = sum_spec
    new_spec.live_time = lt
    return new_spec

def plot_peak_area(erg, path):
    files = glob.glob(path+"/*.Spe")
    area_list = []
    for f in files:
        spec=gs.read_dollar_spe_file(f)
        spec=sa.five_point_smooth(spec)  
        a, popt, pcov = spec_anal.peak_fit1(erg, spec, nchan=10) 
        area_list.append(a) 

    plt.plot(area_list)
    plt.show()


def plot_lt(path, title = ""):
    files = glob.glob(path+"/*.Spe")
    lt= []

    for f in files:
        spec=gs.read_dollar_spe_file(f)
        lt.append(spec.live_time)
    plt.plot(lt)
    plt.title(title)
    plt.xlabel("Spec num")
    plt.ylabel("Live time (s)")
    plt.show()



"""
print diff_list[2314:2319]
print spec2.counts[2314:2319]

# fitting testing
# print "fitting"
# a, pop, pcov = peak_fit1(661, spec2)
# print a
# print pop
# print pcov


#plt.plot(spec1.channels, spec1.counts)
plt.clf()
plt.plot(spec2.channels,spec2.counts)


plt.plot(spec2.channels, diff_list, 'g+')
plt.plot(spec2.channels, sd_list, 'r+')

plt.xlabel("channel num")
plt.ylabel("counts")
plt.yscale('log')

plt.show()

"""
