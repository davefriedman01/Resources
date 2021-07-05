#!/usr/bin/env python
# coding: utf-8

# # Groups

# ---

# $\alpha^m = \alpha...\alpha$ $\}m$ times, where $\alpha \in \mathbb{F}$ and $m$ a positive integer, denotes the group operation applied to $\alpha$ $m$ times<br>
# $(\alpha^m)^n = a^{mn}$<br>
# $(\alpha\beta)^m = \alpha^m\beta^m$<br>
# $\forall \alpha, \beta \in \mathbb{F}$ and all positive integers $m, n$<br>

# ---

# In[1]:


class GroupElement:
    
    def __init__ (self, num, order):
        if order < 0:
            raise ValueError('Group order must be nonnegative.')
        if num < 0 or num >= order:
            raise ValueError(f'Group element must be between 0 and {order - 1}.')
            
        self.num   = num
        self.order = order
        
    def __repr__ (self):
        return f'GroupElement_{self.order}_({self.num})'

class AdditiveGroupElement (GroupElement):


# ---
