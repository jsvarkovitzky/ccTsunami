"""
Create topo files needed for this example:
    
"""

import os,sys

try:
    from pyclaw.geotools import topotools
except:
    print "*** Cannot find geotools module, make sure your PYTHONPATH"
    print "*** includes $CLAW/python directory."
    sys.exit()
try:
    import subfaults
except:
    print "*** Cannot find subfaults module, make sure your PYTHONPATH"
    print "*** includes tsunami-benchmarks/datatools directory."
    sys.exit()


def gettopo():
    """
    Retrieve the topo file from the GeoClaw repository.
    """

    # Set environment variable CLAW_TOPO_DOWNLOAD=True to avoid prompts
    # before downloading.
    force = os.environ.get('CLAW_TOPO_DOWNLOAD', False)
    force = (force in [True,'True'])

    remote_directory = 'http://kingkong.amath.washington.edu/topo/Honshu'
    topo_fname = 'etopo1min139E147E34N41N.asc'
    topotools.get_topo(topo_fname, remote_directory, force)

    remote_directory = 'http://kingkong.amath.washington.edu/topo/Honshu'
    topo_fname = 'etopo4min122E160E20N50N.asc'
    topotools.get_topo(topo_fname, remote_directory, force)

    remote_directory = 'http://kingkong.amath.washington.edu/topo/Honshu'
    topo_fname = 'etopo10min115E210E15N50N.asc'
    topotools.get_topo(topo_fname, remote_directory, force)

    
def makedtopo():
    """
    Create dtopo data file for deformation of sea floor due to earthquake.
    Uses the Okada model with fault parameters and mesh specified in the
    .cfg file.
    """
    print "Making deformation file using Okada model"
    #subfaults.make_dz_honshu_usgs()
    subfaults.make_dz_honshu_ucsb()


if __name__=='__main__':
    gettopo()
    makedtopo()
