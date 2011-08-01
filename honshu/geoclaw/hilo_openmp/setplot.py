
"""
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.

"""

from pyclaw.geotools import topotools
from pyclaw.data import Data


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


    # To plot gauge locations on imshow or contour plot, use this as
    # an afteraxis function:

    def addgauges(current_data):
        from pyclaw.plotters import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)


    #-----------------------------------------
    # Figure for imshow plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='full domain', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('imshow')
    plotaxes.title = 'Surface'
    plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
        pylab.plot([139.7],[35.6],'wo',markersize=7)
        pylab.text(138.2,35.9,'Tokyo',color='w',fontsize=15)
        x_airport = 141.0325
        y_airport = 37.421389
        pylab.plot([x_airport],[y_airport],'wo',markersize=7)
        pylab.text(x_airport-.75,y_airport+.14,'Fukushima',color='w',fontsize=15)

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -4.0
    plotitem.imshow_cmax = 4.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [140,145]
    plotaxes.ylimits = [34,40]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-3000,-3000,1)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0



    #-----------------------------------------
    # Figure for zoom
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Fukushima region', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('imshow')
    plotaxes.title = 'Surface'
    plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
        pylab.plot([139.7],[35.6],'wo',markersize=10)
        pylab.text(138.2,35.9,'Tokyo',color='w',fontsize=25)
        x_fukushima = 141.0325
        y_fukushima = 37.421389
        pylab.plot([x_fukushima],[y_fukushima],'wo',markersize=6)
        pylab.text(x_fukushima-.15,y_fukushima+.04,'Fukushima',color='w',fontsize=15)

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -4.0
    plotitem.imshow_cmax = 4.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [140.8,141.3]
    plotaxes.ylimits = [37,37.8]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-3000,-3000,1)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0






    #-----------------------------------------

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

