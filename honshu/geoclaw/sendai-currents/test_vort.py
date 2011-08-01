import numpy as np
import matplotlib.pyplot as plt

# Matrix version
# (-3 f_k + 4 f_{k+1} - f_{k+2}) / (2 dx)
# (f_{k-1} - 4 f_{k-1} + 3 f_k) / (2 dx)
def vorticity(u,v,dx,dy):
    u_y = np.zeros(u.shape)
    u_y[:,0] = (-3.0*u[:,0] + 4.0 * u[:,1] - u[:,2]) / (2.0 * dy)
    u_y[:,-1] = (u[:,-3] - 4.0 * u[:,-2] + 3.0 * u[:,-1]) / (2.0 * dy)
    u_y[:,1:-1] = (u[:,2:] - u[:,0:-2]) / (2.0 * dy)

    v_x = np.zeros(v.shape)
    v_x[0,:] = (-3.0*v[0,:] + 4.0 * v[1,:] - v[2,:]) / (2.0 * dx)
    v_x[-1,:] = (u[-3,:] - 4.0 * u[-2,:] + 3.0 * u[-1,:]) / (2.0 * dx)
    v_x[1:-1,:] = (v[2:,:] - v[0:-2,:]) / (2.0 * dx)
    
    return v_x - u_y

# ============================================================================
#  Domain parameters 
# ============================================================================
lower = (-50.0,-50.0)
upper = (50.0,50.0)

# ============================================================================
#  Exact solution functions and parameters
# ============================================================================
M = 0.5
g = 1.0
c_1 = 0.04
c_2 = 0.02
x0 = -20.0
y0 = -10.0
alpha = np.pi / 6.0
f = lambda x,y,t: -c_2 * ((x - x0 - M*t*np.cos(alpha))**2 + (y - y0 - M*t*np.sin(alpha))**2)
h = lambda x,y,t: 1.0 - c_1**2 / (4.0 * c_2 * g) * np.exp(2*f(x,y,t))
u = lambda x,y,t: M * np.cos(alpha) + c_1 * (y - y0 - M*t*np.sin(alpha)) * np.exp(f(x,y,t))
v = lambda x,y,t: M * np.sin(alpha) - c_1 * (x - x0 - M*t*np.cos(alpha)) * np.exp(f(x,y,t))

N = 100
x = np.linspace(lower[0],upper[0],N)
y = np.linspace(lower[1],upper[1],N)
dx = x[1] - x[0]
dy = dx
X,Y = np.meshgrid(x,y)

u_vort = u(X.T,Y.T,0)
v_vort = v(X.T,Y.T,0)


omega = -vorticity(u_vort,v_vort,dx,dy)

plt.figure(1)
plt.hold(True)
for i in xrange(N):
    plt.plot(x,omega[:,i],'x')
    plt.plot(x,omega[:,i])
plt.hold(False)
plt.figure(2)
plt.subplot(1,3,1)
plt.pcolor(x,y,u_vort)
plt.colorbar()
plt.subplot(1,3,2)
plt.pcolor(x,y,v_vort)
plt.colorbar()
plt.subplot(1,3,3)
plt.pcolor(x,y,omega)
plt.colorbar()
plt.show()
