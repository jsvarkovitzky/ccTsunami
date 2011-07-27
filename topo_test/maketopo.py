
"""
Download the Monai Valley model bathymetry and massage the data to
produce a topo file with topotype=2 for use in GeoClaw.

Note:
The data file has a first row that must be skipped and the data in the wrong
order for standard GeoClaw input styles described at
begin_html
[http://www.clawpack.org/users/topo.html]
end_html

"""
import os, numpy
from pyclaw.geotools import topotools
import urllib

def maketopo():
    infile = '../1_arc_sec_MHW/CCtopo/CC-B6s04-5853.asc'
        
    print "Fixing topo file"
    z = numpy.loadtxt(infile, skiprows=6, unpack=True)
    Z = -z*0.0001 #negate data for clawpack formating 

    # create output file:
    outfile = 'coast.tt2'
    xlower = -125.25
    xupper = -123.88
    ylower = 41.42
    yupper = 42.53
    mx = 601
    my = 1801
    dx = (xupper - xlower) / mx
    dy = (yupper - ylower) / my
    if abs(dx-dy) > 1e-6:
        print "*** dx and dy are not equal!"
        print "*** dx = %s,  dy = %s" %(dx,dy)
    cellsize = dx
    
    ofile = open(outfile, 'w')
    ofile.write('%s ncols\n' % mx)
    ofile.write('%s nrows\n' % my)
    ofile.write('%s xll\n' % xlower)
    ofile.write('%s yll\n' % ylower)
    ofile.write('%s cellsize\n' % cellsize)
    ofile.write('9999 nodata_value\n')

    for jj in range(my):
        j = my-1-jj
        for i in range(mx):
            ofile.write('%20.12e\n' % Z[i,j])

    ofile.close()
    print "Created ",outfile


if __name__=="__main__":
    maketopo()
