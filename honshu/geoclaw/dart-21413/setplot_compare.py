
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

from pyclaw.geotools import topotools
from pyclaw.data import Data
import pylab
import os

dartdata = pylab.loadtxt('21413_notide.txt')

outdir1 = '_output_1min'
outdir2 = '_output_2min'
title1 = outdir1[-4:]  # last 4 characters
#title1 = '4min'
title2 = outdir2[-4:]  # last 4 characters
outdir1 = os.path.abspath(outdir1)
outdir2 = os.path.abspath(outdir2)

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
    plotfigure.kwargs = {'figsize':(16,9)}

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(121)'
    plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('%s at %4.2f hours' % (title1,t), fontsize=20)
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
        #pylab.plot([205],[19.7],'wo',markersize=10)
        #pylab.text(200,22,'Hilo',color='k',fontsize=25)
        pylab.plot([139.7],[35.6],'wo',markersize=10)
        pylab.text(138.2,35.9,'Tokyo',color='w',fontsize=25)
        addgauges(current_data)

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.outdir = outdir1
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.outdir = outdir1
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [138,155]
    plotaxes.ylimits = [25,42]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.outdir = outdir1
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-5000,-100,6)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]  
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0


    #-----------------------------------------
    # Comparison plot
    #-----------------------------------------

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.axescmd = 'subplot(122)'
    plotaxes.scaled = True

    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('%s at %4.2f hours' % (title2,t), fontsize=20)
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
        #pylab.plot([205],[19.7],'wo',markersize=10)
        #pylab.text(200,22,'Hilo',color='k',fontsize=25)
        pylab.plot([139.7],[35.6],'wo',markersize=10)
        pylab.text(138.2,35.9,'Tokyo',color='w',fontsize=25)
        addgauges(current_data)

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.outdir = outdir2
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.imshow_cmap = geoplot.tsunami_colormap
    plotitem.imshow_cmin = -1.0
    plotitem.imshow_cmax = 1.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.outdir = outdir2
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [138,155]
    plotaxes.ylimits = [25,42]

    # add contour lines of bathy if desired:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.outdir = outdir2
    plotitem.show = False
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = linspace(-5000,-100,6)
    plotitem.amr_contour_colors = ['y']  # color on each level
    plotitem.kwargs = {'linestyles':'solid','linewidths':2}
    plotitem.amr_contour_show = [1,0,0]  
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0



    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------

    def gaugetopo(current_data):
        q = current_data.q
        h = q[:,0]
        eta = q[:,3]
        topo = eta - h
        return topo
        
    def add_zeroline(current_data):
        from pylab import plot, legend, xticks, floor
        t = current_data.t
        #legend(('surface','topography'),loc='lower left')
        plot([0,10800],[0,0],'k')
        n = floor(t.max()/3600.) + 2
        xticks([3600*i for i in range(n)])

    def plot_dart(current_data):
        import pylab
        pylab.plot(dartdata[:,0],dartdata[:,1],'k')
        pylab.legend([title1, title2, 'DART data'])
        add_zeroline(current_data)
        pylab.xlim([0,10800.])

    plotfigure = plotdata.new_plotfigure(name='Surface & topo', figno=300, \
                    type='each_gauge')
    #plotfigure.kwargs = {'figsize':(16,9)}
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    #plotaxes.axescmd = 'subplot(121)'
    plotaxes.title = 'Surface'
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.outdir = outdir1
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'
    plotitem.kwargs = {'linewidth':2}

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.outdir = outdir1
    plotitem.show = False

    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'
    plotaxes.afteraxes = plot_dart


    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    #plotaxes.axescmd = 'subplot(122)'
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.outdir = outdir2
    plotitem.plot_var = 3
    plotitem.plotstyle = 'r-'
    plotitem.kwargs = {'linewidth':2}

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.outdir = outdir2
    plotitem.show = False

    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'

    plotaxes.afteraxes = plot_dart



    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'            # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

