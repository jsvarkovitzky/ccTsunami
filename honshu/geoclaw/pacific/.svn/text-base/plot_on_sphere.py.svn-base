
import os
from enthought.mayavi import mlab
from pyclaw.plotters.data import ClawPlotData
from pyclaw.plotters.colormaps import make_colormap
from setplot import setplot

try:
    linspace
except:
    from pylab import *

def plot_solid_sphere():

    #latitude = linspace(-pi/2, pi/2, 50)
    #longitude = linspace(0, 2*pi, 400)
    latitude = linspace(0, pi/2, 30)
    longitude = linspace(-pi/2, pi/2, 100)
    theta,phi = meshgrid(longitude,latitude)
    X = 0.97*cos(theta)*cos(phi)
    Y = 0.97*sin(theta)*cos(phi)
    Z = 0.97*sin(phi)

    #mlab.figure(3,bgcolor=(1,1,1))
    #mlab.clf()
    mlab.mesh(X,Y,Z,color=(1,1,1))

def plot_lat_long_lines():

    #latitude = linspace(-90,90,19) * pi/180.
    #longitude = linspace(0, 360, 37) * pi/180.
    latitude = linspace(-20,90,10) * pi/180.
    #longitude = linspace(-90,90,19) * pi/180.
    longitude = linspace(-270,-90,19) * pi/180.
    theta,phi = meshgrid(longitude,latitude)
    X = cos(theta)*cos(phi)
    Y = sin(theta)*cos(phi)
    Z = sin(phi)

    for i in range(X.shape[0]):
        mlab.plot3d(X[i,:],Y[i,:],Z[i,:],color=(0,0,0),tube_radius=None,line_width=1)
    for j in range(X.shape[1]):
        mlab.plot3d(X[:,j],Y[:,j],Z[:,j],color=(0,0,0),tube_radius=None,line_width=1)

def plot_eta(x,y,eta):

    theta = x * 2*pi / 360.
    phi = y * 2*pi / 360.
    X = 0.99*cos(theta)*cos(phi)
    Y = 0.99*sin(theta)*cos(phi)
    Z = 0.99*sin(phi)
    #import pdb; pdb.set_trace()
    Z = where(isnan(eta),nan,Z)

    if 0:
        # elevate according to eta:
        #X = X * (1. + 0.03*eta)
        #Y = Y * (1. + 0.03*eta)
        #Z = Z * (1. + 0.03*eta)
        # for big-radial-ocean:
        X = X * (1. + 0.3*eta)
        Y = Y * (1. + 0.3*eta)
        Z = Z * (1. + 0.3*eta)

    #cmap = make_colormap({0:[0,1,1], 1:[0,1,.5]})
    cmap = 'gist_earth'
    cmap = 'Blues'
    #cmap = 'Spectral'
    #mlab.mesh(X,Y,Z,scalars=eta,colormap=cmap, vmin = -1., vmax = 1.)
    # for big-radial-ocean:
    mlab.mesh(X,Y,Z,scalars=eta,colormap=cmap, vmin = -0.3, vmax = 0.3)
    V = (-3.4181052450711888, 74.940316958346571, 3.2320542851649994,\
          array([ 0.5,  0. ,  0.5]))
    mlab.view(*V)
    #mlab.view(0,40)

    mlab.figure(2,bgcolor=(1,1,1))
    mlab.clf()
    mlab.mesh(x,y,eta,colormap=cmap, vmin = -1., vmax = 1.)

    return X,Y,Z

def plotframe(frameno):

    plotdata = ClawPlotData()
    plotdata.outdir = "_output"
    plotdata = setplot(plotdata)
    frame = plotdata.getframe(frameno)
    x = frame.grids[0].c_center[0]
    y = frame.grids[0].c_center[1]
    q = frame.grids[0].q
    eta = q[:,:,3]
    eta = where(q[:,:,0] > 1.,eta,nan)
    #import pdb; pdb.set_trace()

    mlab.figure(3,bgcolor=(1,1,1))
    mlab.clf()
    #plot_solid_sphere()
    plot_lat_long_lines()
    #x = 360 - x
    X,Y,Z = plot_eta(x,y,eta)

def make_all_frames():
    for frameno in range(4):
        plotframe(frameno)
        mlab.savefig("sphere-frame%i.png" % frameno)
        os.system("convert sphere-frame%i.png sphere-frame%i.eps" \
             % (frameno,frameno))

def rotate():
    mlab.figure(3)
    for tt in linspace(30,160,14):
        mlab.view(0,tt)
        mlab.draw()
        mlab.savefig('sphere-rotate%s.png' % str(int(tt)).zfill(3))
    os.system("convert sphere-rotate*.png sphere.gif")

