
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 
from pylab import loadtxt
#gaugeData = loadtxt('ts2a.txt',skiprows=7)

#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of pyclaw.plotters.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 


    from pyclaw.plotters import colormaps, geoplot
    plotdata.clearfigures()  # clear any old figures,axes,items data
    #from pylab import loadtxt




    # To plot gauge locations on pcolor or contour plot, use this as
    # an afteraxis function:gaugeTime

    def addgauges(current_data):
        from pyclaw.plotters import gaugetools
        gaugetools.plot_gauge_locations(current_data.plotdata, \
             gaugenos='all', format_string='ko', add_labels=True)
    
#    if 0:
#        gaugeData = loadtxt('ts2a.txt',skiprows=7)
#        gaugeTime = gaugeData[:,0]
#        g1 = gaugeData[:,1]
#        g2 = gaugeData[:,2]
#        g3 = gaugeData[:,3]
#        g4 = gaugeData[:,4]
#        g6 = gaugeData[:,5]
#        g9 = gaugeData[:,6]
#        g16 = gaugeData[:,7]
#        g22 = gaugeData[:,8]

    #-----------------------------------------
    # Figure for pcolor plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='pcolor', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('pcolor')
    plotaxes.title = 'Surface'
    plotaxes.scaled = True
    plotaxes.afteraxes = addgauges

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = -8.0
    plotitem.pcolor_cmax = 8.0
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 1500.0 #This changes the topo colors
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 0
    #Domain for Geoclaw
    plotaxes.xlimits = [-125.25,-123.88]
    plotaxes.ylimits = [41.42,42.53]
    #Domain, arbitrary
    #plotaxes.xlimits = [0,1801]
    #plotaxes.ylimits = [0,601]

    # Add contour lines of bathymetry:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = linspace(-0.5,0,10)
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [1,1,1]
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add contour lines of topography:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = linspace(0., .5, 10)
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [1,1,1] 
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add dashed contour line for shoreline
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = [0.]
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'dashed'}
    plotitem.amr_contour_show = [1,1,1]
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True



    #-----------------------------------------
    # Figure for zoom
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Zoom', figno=10)
    plotfigure.show = False
    plotfigure.kwargs = {'figsize':[12,7]}

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('zoom')
    plotaxes.axescmd = 'axes([0.0,0.1,0.6,0.6])'
    plotaxes.title = 'Zoom1'
    plotaxes.scaled = True
    plotaxes.xlimits = [55,66]
    plotaxes.ylimits = [55,66]
    plotaxes.afteraxes = addgauges

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = -0.9
    plotitem.pcolor_cmax = 0.9
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [1,0,0]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 1000.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,0,0]

    # Add contour lines of bathymetry:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(-10., 0., 1.)
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add contour lines of topography:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(0., 11., 1.)
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add dashed contour line for shoreline
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = [0.]
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'dashed'}
    plotitem.amr_contour_show = [0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True



    #-----------------------------------------
    # Figure for zoom near axis
    #-----------------------------------------
    #plotfigure = plotdata.new_plotfigure(name='Zoom2', figno=11)
    #plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('zoom2')
    plotaxes.axescmd = 'axes([0.5,0.1,0.6,0.6])'
    plotaxes.title = 'Zoom2'
    plotaxes.scaled = True
    plotaxes.xlimits = [82,93]
    plotaxes.ylimits = [-5,6]
    plotaxes.afteraxes = addgauges

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    #plotitem.plot_var = geoplot.surface
    plotitem.plot_var = geoplot.surface_or_depth
    plotitem.pcolor_cmap = geoplot.tsunami_colormap
    plotitem.pcolor_cmin = -0.9
    plotitem.pcolor_cmax = 0.9
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,1,0]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_pcolor')
    plotitem.plot_var = geoplot.land
    plotitem.pcolor_cmap = geoplot.land_colors
    plotitem.pcolor_cmin = 0.0
    plotitem.pcolor_cmax = 3000.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [1,1,0]


    # Add contour lines of bathymetry:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(-10., 0., 1.)
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add contour lines of topography:
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    from numpy import arange, linspace
    plotitem.contour_levels = arange(0., 11., 1.)
    plotitem.amr_contour_colors = ['g']  # color on each level
    plotitem.kwargs = {'linestyles':'solid'}
    plotitem.amr_contour_show = [0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True

    # Add dashed contour line for shoreline
    plotitem = plotaxes.new_plotitem(plot_type='2d_contour')
    plotitem.plot_var = geoplot.topo
    plotitem.contour_levels = [0.]
    plotitem.amr_contour_colors = ['k']  # color on each level
    plotitem.kwargs = {'linestyles':'dashed'}
    plotitem.amr_contour_show = [0,0,1]  # show contours only on finest level
    plotitem.gridlines_show = 0
    plotitem.gridedges_show = 0
    plotitem.show = True



    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface & topo', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = [-1, 1]
    plotaxes.title = 'Surface'

    # Plot surface as blue curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 3
    plotitem.plotstyle = 'b-'

    # Plot topo as green curve:
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')

    def gaugetopo(current_data):
        q = current_data.q
        h = q[:,0]
        eta = q[:,3]
        topo = eta - h
        return topo
        
    plotitem.plot_var = gaugetopo
    plotitem.plotstyle = 'g-'
    def add_zeroline(current_data):
        from pylab import plot, legend
        t = current_data.t
        legend(('surface','topography'),loc='lower left')
        plot(t, 0*t, 'k')

    plotaxes.afteraxes = add_zeroline
    
    def plot_labData(current_data):
        import pylab
        gaugeno = current_data.gaugeno
        pylab.plot(gaugeTime,g1,'k')
        gaugeTime
#    plotaxes.afteraxes = plot_labData

    #-----------------------------------------
    # Figure for grids alone
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='grids', figno=215)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0,1]
    plotaxes.ylimits = [0,1]
    plotaxes.title = 'grids'
    plotaxes.scaled = True

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='2d_grid')
    plotitem.amr_grid_bgcolor = ['#ffeeee', '#eeeeff', '#eeffee']
    plotitem.amr_gridlines_show = [1,1,0]   
    plotitem.amr_gridedges_show = [1]     

    #-----------------------------------------
    # Scatter plot of surface for radially symmetric
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Scatter', figno=200)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = [0., 100.]
    plotaxes.ylimits = [-.5, 1.]
    plotaxes.title = 'Scatter plot of surface'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type='1d_from_2d_data')
    plotitem.plot_var = geoplot.surface
    def q_vs_radius(current_data):
        from numpy import sqrt
        x = current_data.x
        y = current_data.y
        r = sqrt(x**2 + y**2)
        q = current_data.var
        return r,q
    plotitem.map_2d_to_1d = q_vs_radius
    plotitem.plotstyle = 'o'
    plotitem.amr_color=['b','r','g']
    plotaxes.afteraxes = "pylab.legend(['Level 1','Level 2'])"

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

    
