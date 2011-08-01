
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
#pd.outdir = '_output'

gd = {}
for gn in [21413, 21418, 21419, 21414, 21415, 21416, 52402]:
    gd[gn] = pd.getgauge(gn)


figure(3, figsize=[10,8])
clf()

if 0:
    gn = 21418
    shift = 0.
    plot(gd[gn].t, gd[gn].q[:,3] + shift, 'b', linewidth=2)
    text(400, shift+0.05, "%s" % gn)
    dart = dartdata[gn]
    mask = (dart[:,0] > gd[gn].t.min()) & (dart[:,0] < gd[gn].t.max()) 
    plot(dart[mask,0],dart[mask,1]+shift,'r')

def plotdart(gn, shift):
    mask = (gd[gn].t >= tlimits[gn][0]) & (gd[gn].t <= tlimits[gn][1])
    t = gd[gn].t[mask]
    plot(t, gd[gn].q[mask,3] + shift, 'b', linewidth=2)
    text(t[0], shift+0.05, "%s" % gn)
    dart = dartdata[gn]
    mask = (dart[:,0] > t.min()) & (dart[:,0] < t.max()) 
    plot(dart[mask,0],dart[mask,1]+shift,'r')


plotdart(21414, 2.0)
legend(['GeoClaw','DART data'], 'lower left')
plotdart(21413, 0.)
plotdart(21419, 1.5)
plotdart(52402, -0.5)


#-----------------------------------------------------

tmax = 9
n = tmax + 2
xlabel("Hours post-quake", fontsize=15)
xticks([3600*i for i in range(n)],[str(i) for i in range(n)],\
  fontsize=15)

yticks([],fontsize=15)
#ylabel("meters",fontsize=15)

yb = 0.5
plot([0,0], [yb,yb+.5], 'k', linewidth=2)
plot([-100,140], [yb,yb], 'k', linewidth=2)
plot([-100,140], [yb+.5,yb+.5], 'k', linewidth=2)
text(400,yb+.25,'50 cm')

title("Wave height at selected DART buoys")

xlim([-1800,20000])
ylim([-1.2,2.5])


