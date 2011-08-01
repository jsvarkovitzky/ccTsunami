
"""
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.

Dave George's version.

"""

from pyclaw.geotools import topotools
from pyclaw.data import Data
import matplotlib
#matplotlib.rc('text', usetex=True)
#import pdb

#--------------------------
def setplot(plotdata):
#--------------------------

    """
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.

    """


    from pyclaw.plotters import colormaps, geoplot
    from numpy import linspace

    plotdata.clearfigures()  # clear any old figures,axes,items data


    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:

    #figkwargs = dict(figsize=(18,9),dpi=1200)
    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='pcolor', figno=0)
    plotfigure.show = True
    #plotfigure.kwargs = figkwargs
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Domain'
    plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=14)

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.show = True
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = -10.
    plotitem.pcolor_cmax = 10.
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [1,1,1,1,0]
    plotitem.gridedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.show = True
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land1_colormap
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 40.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,1,1,1,0]
    plotitem.gridedges_show = 1
    dx2 = .04
    dy2 = .08
    plotaxes.xlimits = [141.0325-dx2,141.0325+dx2]
    plotaxes.ylimits = [37.421389-dy2,37.421389+dy2]

    #-----------------------------------------
    # Figures for zooming
    #-----------------------------------------


    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'        # list of frames to print
    plotdata.print_gaugenos = [1,2,3,4,5,6]         # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = False                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

