"""
Module to set up run time parameters for Clawpack.

The values set in the function setrun are then written out to data files
that will be read in by the Fortran code.

"""

import os
from pyclaw import data
import numpy as np


#------------------------------
def setrun(claw_pkg='geoclaw'):
#------------------------------

    """
    Define the parameters used for running Clawpack.

    INPUT:
        claw_pkg expected to be "geoclaw" for this setrun.

    OUTPUT:
        rundata - object of class ClawRunData

    """

    assert claw_pkg.lower() == 'geoclaw',  "Expected claw_pkg = 'geoclaw'"

    ndim = 2
    rundata = data.ClawRunData(claw_pkg, ndim)

    #------------------------------------------------------------------
    # Problem-specific parameters to be written to setprob.data:
    #------------------------------------------------------------------

    #probdata = rundata.new_UserData(name='probdata',fname='setprob.data')

    #------------------------------------------------------------------
    # GeoClaw specific parameters:
    #------------------------------------------------------------------

    rundata = setgeo(rundata)   # Defined below

    #------------------------------------------------------------------
    # Standard Clawpack parameters to be written to claw.data:
    #   (or to amr2ez.data for AMR)
    #------------------------------------------------------------------

    clawdata = rundata.clawdata  # initialized when rundata instantiated


    # Set single grid parameters first.
    # See below for AMR parameters.


    # ---------------
    # Spatial domain:
    # ---------------

    # Number of space dimensions:
    clawdata.ndim = ndim

    # Lower and upper edge of computational domain:
    clawdata.xlower = 140
    clawdata.xupper = 145

    clawdata.ylower = 34
    clawdata.yupper = 40


    # Number of grid cells:
    clawdata.mx = 15
    clawdata.my = 18


    # ---------------
    # Size of system:
    # ---------------

    # Number of equations in the system:
    clawdata.meqn = 3

    # Number of auxiliary variables in the aux array (initialized in setaux)
    clawdata.maux = 3

    # Index of aux array corresponding to capacity function, if there is one:
    clawdata.mcapa = 2



    # -------------
    # Initial time:
    # -------------

    clawdata.t0 = 0.0


    # -------------
    # Output times:
    #--------------

    # Specify at what times the results should be written to fort.q files.
    # Note that the time integration stops after the final output time.
    # The solution at initial time t0 is always written in addition.

    clawdata.outstyle = 1

    if clawdata.outstyle==1:
        # Output nout frames at equally spaced times up to tfinal:
        clawdata.nout = 50
        clawdata.tfinal = 5.e3

    elif clawdata.outstyle == 2:
        # Specify a list of output times.
        clawdata.tout =  [0.5, 1.0]   # used if outstyle == 2
        clawdata.nout = len(clawdata.tout)

    elif clawdata.outstyle == 3:
        # Output every iout timesteps with a total of ntot time steps:
        iout = 2
        ntot = 6
        clawdata.iout = [iout, ntot]



    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 1



    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = 1

    # Initial time step for variable dt.
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 0.016

    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1e+99

    # Desired Courant number if variable dt used, and max to allow without
    # retaking step with a smaller dt:
    clawdata.cfl_desired = 0.75
    clawdata.cfl_max = 1.0

    # Maximum number of time steps to allow between output times:
    clawdata.max_steps = 5000




    # ------------------
    # Method to be used:
    # ------------------

    # Order of accuracy:  1 => Godunov,  2 => Lax-Wendroff plus limiters
    clawdata.order = 2

    # Transverse order for 2d or 3d (not used in 1d):
    clawdata.order_trans = 2

    # Number of waves in the Riemann solution:
    clawdata.mwaves = 3

    # List of limiters to use for each wave family:
    # Required:  len(mthlim) == mwaves
    clawdata.mthlim = [3,3,3]

    # Source terms splitting:
    #   src_split == 0  => no source term (src routine never called)
    #   src_split == 1  => Godunov (1st order) splitting used,
    #   src_split == 2  => Strang (2nd order) splitting used,  not recommended.
    clawdata.src_split = 1


    # --------------------
    # Boundary conditions:
    # --------------------

    # Number of ghost cells (usually 2)
    clawdata.mbc = 2

    # Choice of BCs at xlower and xupper:
    #   0 => user specified (must modify bcN.f to use this option)
    #   1 => extrapolation (non-reflecting outflow)
    #   2 => periodic (must specify this at both boundaries)
    #   3 => solid wall for systems where q(2) is normal velocity

    clawdata.mthbc_xlower = 1
    clawdata.mthbc_xupper = 1

    clawdata.mthbc_ylower = 1
    clawdata.mthbc_yupper = 1


    # ---------------
    # AMR parameters:
    # ---------------


    # max number of refinement levels:
    mxnest = 5

    clawdata.mxnest = -mxnest   # negative ==> anisotropic refinement in x,y,t

    # List of refinement ratios at each level (length at least mxnest-1)
    clawdata.inratx = [5,4,3,5]
    clawdata.inraty = [5,4,3,5]
    clawdata.inratt = [5,4,1,1]


    # Specify type of each aux variable in clawdata.auxtype.
    # This must be a list of length maux, each element of which is one of:
    #   'center',  'capacity', 'xleft', or 'yleft'  (see documentation).

    clawdata.auxtype = ['center','capacity','yleft']


    clawdata.tol = -1.0     # negative ==> don't use Richardson estimator
    clawdata.tolsp = 0.5    # used in default flag2refine subroutine
                            # (Not used in geoclaw!)

    clawdata.kcheck = 3     # how often to regrid (every kcheck steps)
    clawdata.ibuff  = 2     # width of buffer zone around flagged points

    # More AMR parameters can be set -- see the defaults in pyclaw/data.py

    return rundata
    # end of function setrun
    # ----------------------


#-------------------
def setgeo(rundata):
#-------------------
    """
    Set GeoClaw specific runtime parameters.
    For documentation see ....
    """

    try:
        geodata = rundata.geodata
    except:
        print "*** Error, this rundata has no geodata attribute"
        raise AttributeError("Missing geodata attribute")

    # == setgeo.data values ==
    geodata.variable_dt_refinement_ratios = True

    geodata.igravity = 1
    geodata.gravity = 9.81
    geodata.icoordsys = 2
    geodata.Rearth = 6367.5e3
    geodata.icoriolis = 0

    # == settsunami.data values ==
    geodata.sealevel = 0.
    geodata.drytolerance = 1.e-3
    geodata.wavetolerance = 1.e-1
    geodata.depthdeep = 1.e2
    geodata.maxleveldeep = 3
    geodata.ifriction = 1
    geodata.coeffmanning =.025
    geodata.frictiondepth = 1.e6

    # == settopo.data values ==
    geodata.topofiles = []
    # for topography, append lines of the form
    #   [topotype, minlevel, maxlevel, t1, t2, fname]
    geodata.topofiles.append([3, 1, 1, 0., 1.e10, \
                              '../../topo/etopo1min139E147E34N41N.asc'])
    geodata.topofiles.append([3, 1, 1, 0., 1.e10, \
                              '../../topo/etopo4min122E160E20N50N.asc'])
    geodata.topofiles.append([3, 1, 1, 0., 1.e10, \
                              '../../jodc_141E143E36N38N.asc'])

    # == setdtopo.data values ==
    geodata.dtopofiles = []
    # for moving topography, append lines of the form:  (<= 1 allowed for now!)
    #   [topotype, minlevel,maxlevel,fname]
    geodata.dtopofiles.append([1,3,3,'../../sources/honshu-ucsb3-1min.tt1'])

    # == setqinit.data values ==
    geodata.iqinit = 0
    geodata.qinitfiles = []
    # for qinit perturbations, append lines of the form: (<= 1 allowed for now!)
    #   [minlev, maxlev, fname]
    #geodata.qinitfiles.append([1, 1, 'hump.xyz'])

    # == setregions.data values ==
    geodata.regions = []
    # to specify regions of refinement append lines of the form
    #  [minlevel,maxlevel,t1,t2,x1,x2,y1,y2]
    geodata.regions.append([1, 1, 0., 10000., 120, 160, 20, 50])
    geodata.regions.append([1, 3, 0., 10000., 140,145,34,42])
    geodata.regions.append([1, 4, 1000., 10000., 140.5,143,36.0,38.])
    geodata.regions.append([1, 5, 2000., 10000,  140.9,141.1,37.3,37.5])

    # == setgauges.data values ==
    geodata.gauges = []
    # for gauges append lines of the form  [gaugeno, x, y, t1, t2]
    # Place gauges on a transect orthogonal to coast out from nuclear plant
    x_fukushima = 141.0325
    y_fukushima = 37.421389
    x_coast = 141.036
    y_coast = 37.421389
    from numpy import linspace
    for gaugeno,s in enumerate(linspace(0,4,10)):
        xg = x_fukushima + s*(-x_fukushima + x_coast)
        yg = y_fukushima + s*(-y_fukushima + y_coast)
        geodata.gauges.append([gaugeno, xg, yg,  0., 1.e10])


    # == setfixedgrids.data values ==
    geodata.fixedgrids = []
    # for fixed grids append lines of the form
    # [t1,t2,noutput,x1,x2,y1,y2,xpoints,ypoints,\
    #  ioutarrivaltimes,ioutsurfacemax]

    return rundata
    # end of function setgeo
    # ----------------------



if __name__ == '__main__':
    # Set up run-time parameters and write all data files.
    import sys
    if len(sys.argv) == 2:
	rundata = setrun(sys.argv[1])
    else:
	rundata = setrun()

    rundata.write()

