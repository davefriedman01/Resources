#!/usr/bin/env python
# coding: utf-8

# # Random Walks

# ---

# In[1]:


import numpy as np
import numpy.random as npr

import matplotlib.pyplot as plt
plt.style.use('seaborn-pastel')
plt.rcParams['figure.figsize'] = (10, 6)


# In[2]:


def get_trajectory (num_steps=500):
    x_step = np.cumsum(np.where(npr.random(500) < 0.5, -1, 1))
    y_step = np.cumsum(np.where(npr.random(500) < 0.5, -1, 1))
    return x_step, y_step

plt.plot(*get_trajectory());


# In[3]:


points = np.array([(1, 0) if outcome == 0 else   (-1, 0) if outcome == 1 else   (0, 1) if outcome == 2 else   (0, -1) for outcome in npr.choice(4, int(1e3))]).T

plt.plot(*points.cumsum(1));


# ---
