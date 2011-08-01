"""
Retreive topo files needed for Honshu simulations.

"""

import os,sys

try:
    from pyclaw.geotools import topotools
except:
    print "*** Cannot find geotools module, make sure your PYTHONPATH"
    print "*** includes $CLAW/python directory."
    sys.exit()


# Set environment variable CLAW_TOPO_DOWNLOAD=True to avoid prompts
# before downloading.
force = os.environ.get('CLAW_TOPO_DOWNLOAD', False)
force = (force in [True,'True'])

remote_directory = 'http://kingkong.amath.washington.edu/topo/Honshu'

topo_fname = 'etopo1min139E148E36N45N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'etopo1min139E147E34N41N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

#----uncomment if available on king kong---------------
topo_fname = 'etopo1min200E210E18N22N.asc3'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'etopo4min122E160E20N50N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'etopo4min120E72W40S60N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

#----uncomment if available on king kong---------------
topo_fname = 'etopo4min100E300E65S65N.tt3'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'etopo4min122E160E20N50N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'etopo10min115E210E15N50N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

#--might want to remove ------ better file follows
topo_fname = 'jodc_141E143E36N38N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

#----uncomment if available on king kong---------------
topo_fname = 'jodc_20arcsec_140E142E36N38N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'ca_north36secm.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'ca_north6secm.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'cresc1secm_mod.asc'
topotools.get_topo(topo_fname, remote_directory, force)

#----uncomment below if available on king kong---------------
topo_fname = 'hilo_3s_E.asc'
topotools.get_topo(topo_fname, remote_directory, force)

#----uncomment below if available on king kong---------------
topo_fname = 'hilo_city_1_3s_E.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'WA3min124-20W123-40W46N47-04N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

topo_fname = 'PugetSound15sec126W122W47N49N.asc'
topotools.get_topo(topo_fname, remote_directory, force)

