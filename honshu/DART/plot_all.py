
from pylab import *
import glob

files = glob.glob('*-detide.py')
#files = ['51425-detide.py']

for f in files:
    dartnum = f[:5]
    execfile(f)
    figure(60)
    savefig('%s_rawdata_plot.png' % dartnum)
    figure(70)
    savefig('%s_detide_plot.png' % dartnum)
    print "Created plots for ",dartnum

