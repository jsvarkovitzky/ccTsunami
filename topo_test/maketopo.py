
"""
Module to create topo and qinit data files for this example.
"""

from pyclaw.geotools.topotools import topo1writer, topo2writer
from numpy import *

def maketopo():
    """
    Output topography file for the entire domain
    """
    nxpoints=1000
    nypoints=850
    xupper=999.e0
    yupper=849.e0
    xll = 0.e0
    yll = 0.e0
    #outfile= "island.topotype1"
    #topo1writer(outfile,topo,xll,xupper,yll,yupper,nxpoints,nypoints)
    outfile= "island.topotype2"
    topo2writer(outfile,topo,xll,xupper,yll,yupper,nxpoints,nypoints)

def makeqinit():
    """
    Create qinit data file
    """
    nxpoints=1000
    nypoints=850
    xupper=10.e0
    yupper=10.e0
    xll = -10.e0
    yll = -10.e0
    outfile= "wave.xyz"
    topo1writer(outfile,qinit,xll,xupper,yll,yupper,nxpoints,nypoints)

def topo(x,y):
    """
    Topography/Bathymetry provided by infile
    """
    from numpy import *
    infile = '../1_arc_sec_MHW/CCtopo/ca_north36secm.asc'
    z = loadtxt(infile, skiprows=6, unpack=True)
    z = z - 10.0
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
