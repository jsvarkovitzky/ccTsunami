"""
Detide Crescent City Gauge 19750
Raw data from
  ftp://ilikai.soest.hawaii.edu/ptwc/Honshu_Tsunami_Data/070/cres.pwl.070
Downloaded 19 March 2011.
Run this from within python shell to see the plots.
"""

import sys, os
import pylab
sys.path.append('../../datatools')
import dart  # from the directory above

gaugeno = 19750
fname = 'cres.pwl.070'
t1fit = 5000
t2fit = 100000.
t1out = 53000
t2out = 80000.
degree = 10

#fname_notide = os.path.splitext(fname)[0] + '_notide.txt'
fname_notide = '%s_notide.txt' % gaugeno
t,eta = pylab.loadtxt(fname, unpack=True)
t = (t-70) *24*3600  # convert to seconds since midnight on Julian Day 70

c,t_notide,eta_notide = dart.fit_tide_poly(t,eta,degree,t1fit,t2fit, t1out,t2out)

# Time of quake:  05:48:15 UTC on March 12, 2011
# Convert to seconds after midnight on March 12 
t_quake = 5*3600 + 48*60 + 15.
print "Time of quake = %7.2f seconds after start of March 12" % t_quake

t_sec = (t_notide-t_quake)
d = pylab.vstack([t_sec,eta_notide]).T
pylab.savetxt(fname_notide,d)
print "Created file ",fname_notide

#dart.plot_postquake(t_notide,eta_notide,t_quake,gaugeno)


pylab.figure(70)
pylab.subplot(211)
pylab.title('Tide Gauge %s' % gaugeno)

