
"""
Read in fort.hmax file with maximum depth at each point, and then
determine dry zone and plot it.
"""

import os
from pylab import *
from pyclaw.data import Data

def plot_dryzone(plotdata=None):
    if plotdata:
        outdir = plotdata.outdir
    else:
        outdir = '_output'
    figure(5)
    clf()

    rundata = Data(os.path.join(outdir, 'amr2ez.data'))
    hmax_file = os.path.join(outdir, 'fort.hmax')

    mx = rundata.mx
    my = rundata.my
    xlower = rundata.xlower
    ylower = rundata.ylower
    xupper = rundata.xupper
    yupper = rundata.yupper
    dx = (xupper - xlower) / mx
    dy = (yupper - ylower) / my
    x = linspace(xlower+dx/2., xupper-dx/2., mx)
    y = linspace(ylower+dy/2., yupper-dy/2., my)

    d = loadtxt(hmax_file)
    hmax = d[:,0].reshape((my,mx))
    B = d[:,1].reshape((my,mx))
    drycells = where(hmax==0, 0, 1)

    X,Y = meshgrid(x,y)

    contour(X,Y,drycells,[0.5],colors='r',linewidths=2)
    contour(X,Y,B,linspace(0,.5,6),colors='k')
    axis('scaled')
    axis([-5,5,-5,5])
    title("Island topography and dry zone")

if __name__=="__main__":
    plot_dryzone()
    savefig("dryzone.png")
    print "Created dryzone.png"

