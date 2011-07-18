
"""
Module to create topo for the CC area.

"""

from pyclaw.geotools import topotools
import numpy as np

infile = '../1_arc_sec_MHW/CCtopo/ca_north36secm.asc'

nypoints = 850
nxpoints = 1000
ylower = 0.0
yupper = 849.0
dy = (yupper-ylower)/(nypoints-1)
xlower = 0.0
xupper = 999.0
dx = (xupper-xlower)/(nxpoints-1)


def maketopo():
    """
    Output topography file for the entire domain
    """
    from pyclaw.geotools import topotools
    import numpy as np
    outfile= "ccTopofile"     
    topotools.topo2writer(outfile,topo,xlower,xupper,ylower,yupper,nxpoints,nypoints)



def topo(x,y):
    """
    reading in provided bathymetry
    """
    from pyclaw.geotools import topotools
    import numpy as np
    z = np.loadtxt(infile, skiprows=6, unpack=True)
    
    return z


if __name__=='__main__':
    maketopo()
