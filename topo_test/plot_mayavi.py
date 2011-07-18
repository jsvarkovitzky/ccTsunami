import os
from pylab import *
from enthought.mayavi import mlab
from pyclaw.plotters.data import ClawPlotData
from setplot import setplot
from html_movie import make_movie
import glob

outdir = "_output"


def plotframe(frameno,level=1, water_opacity=1.):

    plotdata = ClawPlotData()
    plotdata.outdir = outdir
    print "Plotting solution from ",plotdata.outdir
    plotdata = setplot(plotdata)
    try:
        frame = plotdata.getframe(frameno)
    except:
        print "Unable to get frame"
        return
    mlab.figure(1,bgcolor=(1,1,1),size=(700,600))
    mlab.clf()
    for grid in frame.grids:
        if grid.level == level:

            y = grid.c_center[1]
            x = grid.c_center[0]
            q = grid.q
            eta = q[:,:,3]
            h = q[:,:,0]
        
            topo = eta - h
            cutoff = 0.5
            #cutoff2 = -500.
            shift = 0.
            scale = 1.
            topo1 = scale*where(topo<cutoff, topo-shift, cutoff-shift)
            #topo1 = scale*where(topo>cutoff2, topo1, nan)
            eta1 = scale*where(eta<cutoff, eta-shift, cutoff-shift)
            water1 = where(h>=1.e-3, eta1, nan)
            scale = 12.
            #mlab.mesh(x,y,topo1,colormap='Greens',vmin=-1.0, vmax=0.8)
            #mlab.mesh(x,y,water1,colormap='Blues',vmin=-0.8, vmax=0.8)
            mlab.surf(x,y,topo1,colormap='YlGn',warp_scale=scale,\
                          vmin=-0.3,vmax=0.3)
            mlab.surf(x,y,water1,colormap='Blues',warp_scale=scale,\
                          vmin=-0.2,vmax=0.3, opacity=water_opacity)

    # set the view:  (Do V = view() to figure out the current view)
    V = (29.157490879985176,\
     67.560491214404507,\
     79.798910042690324,\
     array([ 0.        ,  1.        , -0.07500005]))

    mlab.view(*V)
    t = frame.t
    mlab.title('Time = %5.2f' % t,color=(0,0,0),height=0.1,size=0.5)
    
def make_all_frames(water_opacity):
  
    fortqfiles = glob.glob(os.path.join(outdir,'fort.q*'))
    frames = range(len(fortqfiles))
    print "Will make %s frames" % len(fortqfiles)
    plotfiles = []
    for frameno in frames:
        plotframe(frameno,1,water_opacity)
        frstring = str(int(frameno)).zfill(3)
        name = "movie-frame%s.png" % frstring
        plotfiles.append(name)
        mlab.savefig("movie-frame%s.png" % frstring)
    make_movie(plotfiles, moviename='movie.html')
        

