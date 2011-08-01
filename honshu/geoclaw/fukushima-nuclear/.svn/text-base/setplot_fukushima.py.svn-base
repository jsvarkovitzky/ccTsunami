
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
    plotaxes.title = 'Fukushima'
    plotaxes.scaled = True

    def addgauges(current_data,fnt=14):
        from pyclaw.plotters import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
                gaugenos=[], format_string='ko', add_labels=True,markersize=8,fontsize=fnt)

    def fixup(current_data):
        import pylab
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=14)
        pylab.xticks([141.0325-.03,141.0325,141.0325+.03],fontsize=15)
        pylab.yticks(fontsize=15)
        pylab.plot([139.7],[35.6],'wo',markersize=10)
        #pylab.text(138.2,35.9,'Tokyo',color='w',fontsize=25)
        x_fukushima = 141.0325
        y_fukushima = 37.421389
        pylab.plot([x_fukushima],[y_fukushima],'wo',markersize=8)
        pylab.text(x_fukushima-.015,y_fukushima+.004,'Fukushima',color='w',fontsize=15)
        addgauges(current_data)

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
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface & topo', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0.,4000.]
    plotaxes.ylimits = [-2,11.]
    plotaxes.title = 'Surface'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.show = False

    def gaugetopo(current_data):
        q = current_data.q
        h = q[:,0]
        eta = q[:,3]
        topo = eta - h
        return topo

    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'

    def add_zeroline(current_data):
        from pylab import plot, legend, xticks, floor
        t = current_data.t
        #legend(('surface','topography'),loc='lower left')
        plot(t, 0*t, 'k')
        n = floor(t.max()/3600.) + 2
        xticks([3600*i for i in range(n)])
        add_timebar(current_data)

    def add_timebar(current_data):
        from pylab import plot,linspace,ones
        t = 54.*60.*ones(50)
        y = linspace(-2,12)
        plot(t,y,'k-')

    plotaxes.afteraxes = add_zeroline
    #plotaxes.afteraxes = add_timebar

    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = [33]#'all'        # list of frames to print
    plotdata.print_gaugenos = [1,2,3,4,5,6]         # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = False                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

