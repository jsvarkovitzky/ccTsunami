
from pylab import *
from pyclaw.plotters.data import ClawPlotData
import glob

#-----------------------------------------------------
dartdata = {}
for gaugeno in [21401, 21414, 21415,  21418, 21419, 21413, 52402, 52403, \
                52405, 51407, 52406, 51425]:
    files = glob.glob('../../DART/%s*_notide.txt' % gaugeno)
    if len(files) != 1:
        raise Exception("*** found %s files for gauge number %s" \
                   % (len(files),gaugeno)   )
    fname = files[0]
    dartdata[gaugeno] = loadtxt(fname)

tlimits = {}
tlimits[21401] = [0,28800]
tlimits[21413] = [0,28800]
tlimits[21414] = [8000,28800]
tlimits[21415] = [7200,28800]
tlimits[21416] = [0,14400]
tlimits[21418] = [0,28800]
tlimits[21419] = [0,28800]
tlimits[52402] = [0,36000]
tlimits[51407] = [2100,40000]
tlimits[52403] = [8000,40000]
tlimits[52405] = [0,32400]
tlimits[52406] = [16000,40000]
tlimits[52425] = [25200,40000]

#-----------------------------------------------------
pd = ClawPlotData()
pd.outdir = '_output'

gd = {}
for gn in [51425, 21413, 52402, 52403, 52405, 52406]:
    gd[gn] = pd.getgauge(gn)


figure(3, figsize=[10,8])
clf()

gn = 21413
shift = 0.
plot(gd[gn].t, gd[gn].q[:,3] + shift, 'b', linewidth=2)
text(400, shift+0.05, "%s" % gn)
dart = dartdata[gn]
mask = (dart[:,0] > gd[gn].t.min()) & (dart[:,0] < gd[gn].t.max()) 
plot(dart[mask,0],dart[mask,1]+shift,'r')

def plotdart(gn, shift):
    plot(gd[gn].t, gd[gn].q[:,3] + shift, 'b', linewidth=2)
    text(gd[gn].t1, shift+0.05, "%s" % gn)
    dart = dartdata[gn]
    mask = (dart[:,0] > gd[gn].t.min()) & (dart[:,0] < gd[gn].t.max()) 
    plot(dart[mask,0],dart[mask,1]+shift,'r')

legend(['GeoClaw','DART data'], 'lower left')

plotdart(52402, -0.5)
plotdart(52403, 0.6)
plotdart(52405, 0.9)
plotdart(52406, 1.2)
plotdart(51425, 1.5)


#-----------------------------------------------------

tmax = 9
n = tmax + 2
xlabel("Hours post-quake", fontsize=15)
xticks([3600*i for i in range(n)],[str(i) for i in range(n)],\
  fontsize=15)

yticks([],fontsize=15)
#ylabel("meters",fontsize=15)

plot([0,0], [1.0,1.5], 'k', linewidth=2)
plot([-100,140], [1.0,1.0], 'k', linewidth=2)
plot([-100,140], [1.5,1.5], 'k', linewidth=2)
text(400,1.25,'50 cm')

title("Wave height at DART buoys")

xlim([-1800,36000])
ylim([-1.5,2])


