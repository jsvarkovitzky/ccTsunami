
def setgeo(rundata):
    """
    Set GeoClaw specific runtime parameters.
    For documentation see ....
    """

    try:
        geodata = rundata.geodata
    except:
        print "*** Error, this rundata has no geodata attribute"
        raise AttributeError("Missing geodata attribute")

    geodata.variable_dt_refinement_ratios = True

    # == setgeo.data values ==
    R1=6357.e3 #polar radius
    R2=6378.e3 #equatorial radius
    Rearth=.5*(R1+R2)
    geodata.igravity = 1
    geodata.gravity = 9.81
    geodata.icoordsys = 2
    geodata.icoriolis = 1
    geodata.Rearth = Rearth

    # == settsunami.data values ==
    geodata.sealevel = 0.
    geodata.drytolerance = 1.e-3
    geodata.wavetolerance = 5.e-2
    geodata.depthdeep = 1.e2
    geodata.maxleveldeep = 5
    geodata.ifriction = 1
    geodata.coeffmanning = 0.025
    geodata.frictiondepth = 100.0

    # == settopo.data values ==
    # set a path variable for the base topo directory for portability
    import os
    #topo=os.environ['TOPO']
    #topo = 'topo'
    topopath0 = os.path.join('etopo1min139E147E34N41N.asc')
    topopath1 = os.path.join('etopo4min100E300E65S65N.tt3')
    topopath2 = os.path.join('etopo1min200E210E18N22N.asc3')
    topopath3 = os.path.join('hilo_3s_E.asc')
    topopath4 = os.path.join('hilo_city_1_3s_E.asc')

    geodata.topofiles = []
    geodata.topofiles.append([3, 3, 3, 0.0, 5.e3, topopath0])
    geodata.topofiles.append([3, 1, 2, 0.0, 1e10, topopath1])
    geodata.topofiles.append([3, 1, 3, 0.0, 1e10, topopath2])
    #geodata.topofiles.append([3, 1, 4, 0.0, 1e10, topopath3])
    #geodata.topofiles.append([3, 1, 5, 0.0, 1e10, topopath4])


    # == setdtopo.data values ==
    # == setdtopo.data values ==
    geodata.dtopofiles = []
    # for moving topography, append lines of the form:
    #   [topotype, minlevel,maxlevel,fname]

    geodata.dtopofiles.append([1,3,3,'honshu-ucsb.tt1'])

    # == setqinit.data values ==
    geodata.qinitfiles = []
    # for qinit perturbations append lines of the form
    #   [minlev, maxlev, fname]

    # == setregions.data values ==
    geodata.regions = []
    # to specify regions of refinement append lines of the form
    #  [minlevel,maxlevel,t1,t2,x1,x2,y1,y2]

    # == setgauges.data values ==
    geodata.gauges = []
    # for gauges append lines of the form  [gaugeno, x, y, t0, tf]
    geodata.gauges.append([1, -155.056+360, 19.731, 25.e3, 40e3]) #Hilo
    geodata.gauges.append([2, -155.029+360, 19.732, 25.e3, 40e3]) #Hilo
    geodata.gauges.append([3, -155.075+360, 19.722, 25.e3, 40e3]) #Hilo
    geodata.gauges.append([4, 156.516, 19.642, 25.e3, 40e3])  #DART buoy 51407


    # == setfixedgrids.data values ==
    geodata.fixedgrids = []
    # for fixed grids append lines of the form
    # [t1,t2,noutput,x1,x2,y1,y2,xpoints,ypoints,\
    #  ioutarrivaltimes,ioutsurfacemax]
    #geodata.fixedgrids.append([54.e3,55.e3,100,-101.,-96.,14.,19.,1000,1000,0,0])

    return rundata


