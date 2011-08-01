
""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

import numpy as np
import matplotlib.pyplot as plt

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

    # ========================================================================
    #  Water Velocity Helper Functions
    # ========================================================================        
    def water_velocity(current_data,DRY_TOL=1e-6):
        r"""Calculate velocity from the momentum and depth
        
        Calculates the x and y velocities from the momenta.  A mask is 
        constructed so that division by a small depth is avoided, controlled
        by the optional keyword argument DRY_TOL (default = 1e-6).  A check
        for NaNs is also made.  Any point not satisfying either of these
        criteria is set to 0.0.
        
        returns numpy.ndarray, nump.ndarray
        """
        h = current_data.q[:,:,0]
        hu = current_data.q[:,:,1]
        hv = current_data.q[:,:,2]
        u = np.zeros(hu.shape)
        v = np.zeros(hv.shape)
        
        index = np.nonzero((np.abs(h) > DRY_TOL) * (h != np.nan))
        u[index[0],index[1]] = hu[index[0],index[1]] / h[index[0],index[1]]
        v[index[0],index[1]] = hv[index[0],index[1]] / h[index[0],index[1]]
        
        return u,v
        
    def vorticity(current_data):
        r"""Calculate vorticity of velocity field
        
        Using matrix operations, calculate u_y + v_x, note that second order,
        centered differences are used for interior points and forward and
        backward differences for the boundary values.
        
        returns numpy.ndarray of shape of u and v
        """
        u,v = water_velocity(current_data)
        dx = current_data.dx
        dy = current_data.dy
        
        u_y = np.zeros(u.shape)
        u_y[:,0] = (-3.0*u[:,0] + 4.0 * u[:,1] - u[:,2]) / (2.0 * dy)
        u_y[:,-1] = (u[:,-3] - 4.0 * u[:,-2] + 3.0 * u[:,-1]) / (2.0 * dy)
        u_y[:,1:-1] = (u[:,2:] - u[:,0:-2]) / (2.0 * dy)

        v_x = np.zeros(v.shape)
        v_x[0,:] = (-3.0*v[0,:] + 4.0 * v[1,:] - v[2,:]) / (2.0 * dx)
        v_x[-1,:] = (u[-3,:] - 4.0 * u[-2,:] + 3.0 * u[-1,:]) / (2.0 * dx)
        v_x[1:-1,:] = (v[2:,:] - v[0:-2,:]) / (2.0 * dx)
        
        return v_x - u_y
        
        
    def water_speed(current_data):
        u,v = water_velocity(current_data)
        return np.sqrt(u**2+v**2)
        
    def water_quiver(current_data):
        u = water_u(current_data)
        v = water_v(current_data)
            
        plt.hold(True)
        Q = plt.quiver(current_data.x[::2,::2],current_data.y[::2,::2],
                        u[::2,::2],v[::2,::2])
        max_speed = np.max(np.sqrt(u**2+v**2))
        label = r"%s m/s" % str(np.ceil(0.5*max_speed))
        plt.quiverkey(Q,0.15,0.95,0.5*max_speed,label,labelpos='W')
        plt.hold(False)    

    #-----------------------------------------
    # Figure for imshow plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='full domain', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('imshow')
    plotaxes.title = 'Surface'
    plotaxes.scaled = False

    def fixup(current_data):
        import pylab
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        pylab.xticks(fontsize=15)
        pylab.yticks(fontsize=15)
        pylab.plot([139.7],[35.6],'wo',markersize=10)
        pylab.text(138.2,35.9,'Tokyo',color='w',fontsize=25)
        x_airport = 140.9317
        y_airport = 38.1389
        pylab.plot([x_airport],[y_airport],'wo',markersize=4)
        pylab.text(x_airport-.15,y_airport+.04,'Airport',color='w',fontsize=15)

    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
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
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [138,148]
    plotaxes.ylimits = [34,42]

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
    # Figure for zoom plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Sendai Bay', figno=1)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('imshow')
    plotaxes.title = 'Surface'
    plotaxes.scaled = False

    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        x_airport = 140.9317
        y_airport = 38.1389
        pylab.plot([x_airport],[y_airport],'wo',markersize=10)
        pylab.text(x_airport-.05,y_airport+.04,'Airport',color='w',fontsize=25)
        #addgauges(current_data)
    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
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
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [140.8,141.8]
    plotaxes.ylimits = [37.3,38.6]

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
    # Figure for zoom plot
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Airport', figno=2)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes('imshow')
    plotaxes.title = 'Surface'
    plotaxes.scaled = False

    def fixup(current_data):
        import pylab
        #addgauges(current_data)
        t = current_data.t
        t = t / 3600.  # hours
        pylab.title('Surface at %4.2f hours' % t, fontsize=20)
        x_airport = 140.9317
        y_airport = 38.1389
        pylab.plot([x_airport],[y_airport],'wo',markersize=10)
        pylab.text(x_airport,y_airport+.01,'Airport',color='w',fontsize=25)
        addgauges(current_data)
    plotaxes.afteraxes = fixup

    # Water
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
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
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    plotitem.add_colorbar = False
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.gridedges_show = 1
    plotaxes.xlimits = [140.85,141.0]
    plotaxes.ylimits = [38.08,38.20]

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
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='Surface & topo', figno=300, \
                    type='each_gauge')
    plotfigure.clf_each_gauge = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
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

    plotaxes.afteraxes = add_zeroline

    # ========================================================================
    #  Water Current Plots
    # ========================================================================
    max_speed = 5.0
    
    #  Full figure
    plotfigure = plotdata.new_plotfigure(name='full_currents', figno=400)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Currents Full Domain'
    plotaxes.scaled = True
    plotaxes.xlimits = [138,148]
    plotaxes.ylimits = [34,42]

    # Speed
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = water_speed
    plotitem.imshow_cmap = plt.get_cmap('PuBu')
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = max_speed
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]
    # plotitem.aftergrid = water_quiver

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.add_colorbar = False
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    
    # ========================================================================
    #  Zoomed Figure - Sendai Bay
    plotfigure = plotdata.new_plotfigure(name='sendai_bay_currents', figno=401)
    plotfigure.show = False

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Currents Sendai Bay'
    plotaxes.scaled = True
    plotaxes.xlimits = [140.8,141.8]
    plotaxes.ylimits = [37.3,38.6]

    # Speed
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = water_speed
    plotitem.imshow_cmap = plt.get_cmap('PuBu')
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = max_speed
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.add_colorbar = False
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    
    # ========================================================================
    #  Zoomed Figure - Airport
    plotfigure = plotdata.new_plotfigure(name='airport_currents', figno=402)
    plotfigure.show = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Currents Airport'
    plotaxes.scaled = True
    plotaxes.xlimits = [140.85,141.0]
    plotaxes.ylimits = [38.08,38.20]

    # Speed
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = water_speed
    plotitem.imshow_cmap = plt.get_cmap('PuBu')
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = max_speed
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.add_colorbar = False
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0
    
    # ========================================================================
    #  Vorticity Plots
    # ========================================================================
    vorticity_limits = [-2,2]
    #  Full domain
    plotfigure = plotdata.new_plotfigure(name='full_vorticity', figno=500)
    plotfigure.show = True

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.title = 'Vorticity'
    plotaxes.scaled = True
    plotaxes.xlimits = [138,148]
    plotaxes.ylimits = [34,42]

    # Speed
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = vorticity
    plotitem.imshow_cmap = colormaps.make_colormap({1.0:'r',0.5:'w',0.0:'b'})
    plotitem.imshow_cmin = vorticity_limits[0]
    plotitem.imshow_cmax = vorticity_limits[1]
    plotitem.add_colorbar = True
    plotitem.amr_gridlines_show = [0,0,0]
    plotitem.amr_gridedges_show = [1]

    # Land
    plotitem = plotaxes.new_plotitem(plot_type='2d_imshow')
    plotitem.plot_var = geoplot.land
    plotitem.imshow_cmap = geoplot.land_colors
    plotitem.add_colorbar = False
    plotitem.imshow_cmin = 0.0
    plotitem.imshow_cmax = 100.0


    #-----------------------------------------
    
    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via pyclaw.plotters.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_gaugenos = 'all'          # list of gauges to print
    plotdata.print_fignos = [400,401,402]            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata

