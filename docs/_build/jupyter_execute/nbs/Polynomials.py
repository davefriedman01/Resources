#!/usr/bin/env python
# coding: utf-8

# # Polynomials

# ### __Real Polynomial in one variable__<br>
# $$P(x) = \sum_{k = 0}^n a_k x^k = a_n x^n + a_{n - 1} x^{n - 1} + ... + a_2 x^2 + a_1 x + a_0$$
# where $n$ is a nonnegative integer and $a_0, a_1, a_2, ..., a_n \in \mathbb{R}$ are constants called the coefficients of the polynomial.<br>
# If the leading coefficient $a_n \ne 0$, then the degree of the polynomial is $n$.<br>
# $\text{dom}(P(x)) = \mathbb{R}$<br>
# 
# __Polynomial Addition__<br>
# Let $f(x) = \sum_{k = 0}^n a_k x^k$ and $g(x) = \sum_{k = 0}^n b_k x^k$ be polynomials.<br>
# 
# $$(f + g)(x) = \sum_{k = 0}^n (a_k + b_k) x^k$$
# 
# __Polynomial Subtraction__<br>
# Let $f(x) = \sum_{k = 0}^n a_k x^k$ and $g(x) = \sum_{k = 0}^n b_k x^k$ be polynomials.<br>
# 
# $$(f - g)(x) = \sum_{k = 0}^n (a_k - b_k) x^k$$
# 
# __Polynomial Differentiation__<br>
# Let $f(x) = \sum_{k = 0}^n a_k x^k$ be a polynomial.<br>
# 
# $$f'(x) = \sum_{k = 0}^n k a_k x^{k - 1}$$
# 
# ### __Real Polynomial in two variables__<br>
# $$P(x, y) = \sum a_{nm} x^n y^m$$
# where $a_i \in \mathbb{R}$ is a constant and $m$ and $n$ are nonnegative integers.<br>
# If the leading coefficient $a_{nm} \ne 0$, then the degree of the polynomial is $n + m$.<br>
# $\text{dom}(P(x)) = \mathbb{R}^2$<br>
# 
# __General Linear Function in two variables__<br>
# $$
# \begin{align}
# f(x, y)
# &= a_{10} x + a_{01} y + a_{00} \\
# &= A x + B y + C \\
# \end{align}
# $$
# 
# __General Quadratic Function in two variables__<br>
# $$
# \begin{align}
# f(x, y)
# &= a_{20} x^2 + a_{11} x y + a_{02} y^2 + a_{10} x + a_{01} y + a_{00} \\
# &= A x^2 + B x y + C y^2 + D x + E y + F \\
# \end{align}
# $$
# 
# __General Cubic Function in two variables__<br>
# $$
# \begin{align}
# f(x, y)
# &= a_{30} x^3 + a_{21} x^2 y + a_{12} x y^2 + a_{03} y^3 + a_{20} x^2 + a_{11} x y + a_{02} y^2 + a_{10} x + a_{01} y + a_{00} \\
# &= A x^3 + B x^2 y + C x y^2 + D y^3 + E x^2 + F x y + G y^2 + H x + I y + J \\
# \end{align}
# $$
# 
# ### Real Polynomial in several variables
# $$P(x_1, x_2, ..., x_z) = \sum a_{n_1 n_2 ... n_z} x_1^{n_1} x_2^{n_2} ... x_z^{n_z}$$

# ---

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-pastel')
plt.rcParams['figure.figsize'] = (10, 6)

from itertools import zip_longest


# In[2]:


class Polynomial:
    def __init__ (self, *coefficients):
        self.coefficients = list(coefficients)
        
    def __repr__ (self):
        return f"Polynomial {str(tuple(self.coefficients))}"
    
    def __str__ (self):
        def x_expr (degree):
            if degree == 0:
                out = ''
            elif degree == 1:
                out = 'x'
            else:
                out = f'x^{str(degree)}'
            return out
        degree = len(self.coefficients) - 1
        out = ''
        for i in range(len(self.coefficients)):
            coef = self.coefficients[i]
            if abs(coef) == 1 and i < degree:
                out += f"{'+' if coef > 0 else '-'}{x_expr(degree - i)}"
            elif coef != 0:
                out += f"{coef:+g}{x_expr(degree - i)}"
        return out.lstrip('+')
    
    def __call__ (self, x):
        #return [0 * x + coef for coef in self.coefficients]
        return sum([coef * x ** index for index, coef in enumerate(self.coefficients[::-1])])
    
    def degree (self):
        return len(self.coefficients)
    
    def __add__ (self, other):
        P1 = self.coefficients[::-1]
        P2 = other.coefficients[::-1]
        return self.__class__(*[sum(t) for t in zip_longest(P1, P2, fillvalue=0)][::-1])
    
    def __sub__ (self, other):
        P1 = self.coefficients[::-1]
        P2 = other.coefficients[::-1]
        return self.__class__(*[t1 - t2 for t1, t2 in zip_longest(P1, P2, fillvalue=0)][::-1])
    
    def derivative (self):
        derived_coefs = []
        exponent = len(self.coefficients) - 1
        for i in range(len(self.coefficients) - 1):
            derived_coefs.append(self.coefficients[i] * exponent)
            exponent -= 1
        return self.__class__(*derived_coefs)


# In[3]:


p1 = Polynomial(4, 0, -4, 3, 0)
p2 = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_sum = p1 + p2
p_dif = p1 - p2
x = np.linspace(-3, 3, 51)
y1 = p1(x)
y2 = p2(x)
y_sum = p_sum(x)
y_dif = p_dif(x)
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.plot(x, y_sum, label='y_sum')
plt.plot(x, y_dif, label='y_dif')
plt.legend();


# In[4]:


n = 5
display(
    (n + 1)**2,
    (n + 1)**2 - sum(range(n + 1)),
    sum(range(n + 2)),
    sum(range(n + 1)),
)


# In[5]:


p = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
dp = p.derivative()
x = np.linspace(-2, 3, 51)
y = p(x)
df = dp(x)
plt.plot(x, y, label='y')
plt.plot(x, df, label='dy')
plt.legend();
print(p)
print(dp)


# In[6]:


for count, poly in enumerate([p]):
    print(f'$p_{count} = {str(poly)}$')


# ---
