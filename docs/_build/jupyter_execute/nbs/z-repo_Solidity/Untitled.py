#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import numpy.random as npr

from scipy.optimize import fsolve # finding roots

get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import mpl, plt
from mpl_toolkits.mplot3d import Axes3D # surface plot
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (10, 6)


# ---

# In[2]:


from scipy import optimize
dir(optimize)


# In[3]:


help(optimize)


# In[4]:


# Coin Flip
iterations = 100
np.array([np.sum(npr.random(iterations) < 0.5) for _ in range(100)])


# In[5]:


def get_mean (flips=int(1e3), num_experiments=100):
    return np.mean(np.array([np.sum(npr.random(flips) < 0.5) for _ in range(num_experiments)]))

means = []
for i in range(1, int(1e3)):
    means.append(get_mean(num_experiments=i))
plt.plot(means);


# In[6]:


counts, bin_edges, _ = plt.hist(npr.random(100), bins=int(1e2))


# In[7]:


bin_size = bin_edges[1] - bin_edges[0]
new_widths = bin_size * counts / counts.max()
plt.bar(bin_edges[:-1], counts, width=new_widths, color=['r', 'g', 'b']);


# In[8]:


log2bins = np.logspace(-8, 0, num=9, base=2)
log2bins[0] = 0.0
counts, bin_edges, _ = plt.hist(npr.random(100), bins=log2bins)


# In[9]:


bin_size = bin_edges[1] - bin_edges[0]
plt.bar(bin_edges[:-1], counts, width=bin_size, align='edge');


# In[10]:


# Contour Plot
x_vals = np.linspace(-3, 3, 21)
y_vals = np.linspace(0, 10, 11)
X, Y = np.meshgrid(x_vals, y_vals)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(X) * np.sin(Y)
cs = plt.contourf(X, Y, Z, 10, cmap=None)
plt.clabel(cs, fontsize=10);


# In[11]:


# Surface Plot
ax = Axes3D(plt.figure())
ax.plot_surface(X, Y, Z, rstride=1, cstride=1);


# In[12]:


def find_roots (f, points=0):
    x = np.linspace(-10, 10, 1000)
    plt.plot(x, f(x));
    roots, infodict, ier, mesg = fsolve(f, points, full_output=True)
    plt.scatter(roots, np.zeros(len(roots)));
    if ier == 1:
        print('solution found')
    else:
        print('solution not found')


# In[13]:


def f (x): return x**2 - 1
find_roots(f, [-0.5, 0.5])


# In[14]:


def f (x): return np.sin(x)**10
find_roots(f)


# In[15]:


def f (x): return x * (1 + x**3) - 1
find_roots(f, [-1, 1])


# In[16]:


np.roots([1,0,0,1,-1])


# In[17]:


def f (x): return x**3.4 + x - 1
find_roots(f)

