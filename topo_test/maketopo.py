
"""
Module to create topo and qinit data files for this example.
"""

from pyclaw.geotools.topotools import topo1writer, topo2writer
from numpy import *

def maketopo():
    """
    Output topography file for the entire domain
    """
    nxpoints=300
    nypoints=300
    xupper=15.e0
    yupper=15.e0
    xll = -15.e0
    yll = -15.e0
    #outfile= "island.topotype1"
    #topo1writer(outfile,topo,xll,xupper,yll,yupper,nxpoints,nypoints)
    outfile= "island.topotype2"
    topo2writer(outfile,topo,xll,xupper,yll,yupper,nxpoints,nypoints)

def makeqinit():
    """
    Create qinit data file
    """
    nxpoints=100
    nypoints=100
    xupper=10.e0
    yupper=10.e0
    xll = -10.e0
    yll = -10.e0
    outfile= "wave.xyz"
    topo1writer(outfile,qinit,xll,xupper,yll,yupper,nxpoints,nypoints)

def topo(x,y):
    """
    Conical island
    """
    # Depth of water: 0.32 or 0.42 meters for benchmarks.
    depth = 0.32   #According to USACE benchmark site
    r = sqrt(x**2 + y**2) 
    z = where(r < 1.1, 0.625, 0.625 - 0.25*(r-1.1))
    z = where(r < 3.6, z, 0.)
    z = z - depth
    return z


def qinit(x,y):
    """
    Wave approaching from left.
    (Used as initial test problem)
    """
    hjump = 0.3
    z = where((x > -9.) & (x < -7.), hjump, 0.)
    return z

if __name__=='__main__':
    maketopo()
    #makeqinit()
