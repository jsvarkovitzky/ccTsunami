"""
Detide 21401 using data from
    http://www.ndbc.noaa.gov/station_history.php?station=21401
Run this from within python shell to see the plots.
"""

import sys, os
import pylab
sys.path.append('../../datatools')
import dart  # from the directory above

gaugeno = 21401
fname = '21401-03142011.txt'
t1fit = 15900.
t2fit = 17000.
t1out = 16100.
t2out = 16800.
degree = 15

fname_notide = os.path.splitext(fname)[0] + '_notide.txt'
t,eta = dart.plotdart(fname)    
t = pylab.flipud(t)
eta = pylab.flipud(eta)

c,t_notide,eta_notide = dart.fit_tide_poly(t,eta,degree,t1fit,t2fit, t1out,t2out)

# Time of quake:  05:48:15 UTC on March 12, 2011
# Convert to minutes after start of March:
t_quake = 11*24*60 + 5*60 + 48 + 15/60.  
#print "Time of quake = %7.2f minutes after start of March" % t_quake

t_sec = (t_notide-t_quake)*60.
d = pylab.vstack([t_sec,eta_notide]).T
pylab.savetxt(fname_notide,d)
print "Created file ",fname_notide

#dart.plot_postquake(t_notide,eta_notide,t_quake,gaugeno)


pylab.figure(70)
pylab.subplot(211)
pylab.title('DART %s' % gaugeno)

