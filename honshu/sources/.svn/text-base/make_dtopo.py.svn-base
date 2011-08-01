"""
Create dtopo files (seafloor displacement) needed for the Honshu simulations.
Uses the Okada model with fault parameters and mesh specified in the .txt
files.

Make sure appropriate lines are un-commented in the main program at the end
to make all desired dtopo files.
    
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


def make_dz_honshu(fname_subfaults, fname_dtopo, faultparams={}):
    """
    Creates a dtopo file over a region appropriate for the 11 March 2011
    Honshu quake.

    Improved from the above versions by choosing the mesh spacing to align
    properly with bathy grids (spacing 1 minute).
    
    Reads subfault model from fname_subfaults
    Output dtopo file as fname_dtopo

    """

    if faultparams == {}:
        # If this dictionary was not passed in, set default values:
        faultparams['mx'] = 241
        faultparams['my'] = 361  
        faultparams['xlower'] = 140
        faultparams['xupper'] = 144
        faultparams['ylower'] = 35
        faultparams['yupper'] = 41
    fm = subfaults.read_subfault_model(fname_subfaults)
    print "Making deformation file %s using Okada model" % fname_dtopo
    print "  with input %s" % fname_subfaults
    X,Y,dZ = subfaults.make_okada_dz(fm, faultparams)
    subfaults.write_dz(fname_dtopo, X,Y,dZ)
    return X,Y,dZ


if __name__ == "__main__":
    """
    Commands executed as main program.
    """

    # append names to fnames for the models to be used:
    fnames = []
    #fnames.append('honshu-usgs')
    #fnames.append('honshu-ucsb')
    #fnames.append('honshu-ucsb3')
    fnames.append('honshu-ucsb3-subset')

    for fname in fnames:
        fname_subfaults = fname + '.txt'
        fname_dtopo = fname + '-1min.tt1'
        make_dz_honshu(fname_subfaults, fname_dtopo)


