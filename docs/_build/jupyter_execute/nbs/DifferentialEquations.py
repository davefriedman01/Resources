#!/usr/bin/env python
# coding: utf-8

# # Differential Equations

# ---

# ### First Order DE
# $\frac{dy}{dt} = f(t, y)$ where $f$ is a given function of two variables<br>
# * any differentiable function $y = \phi(t)$ that satisfies this equation for all $t$ in some interval is called a _solution_<br>
# * for an arbitrary function $f$, there is no general method for solving the equation in terms of elementary functions
# 
# #### Linear First Order DE
# 
# #### Separable First Order DE
# 
# #### Exact First Order DE

# Numerical Approximation
# 
# Existence and Uniqueness of solutions

# $y' + p(t) y = g(t)$
# 
# Autonomous System
# $y' = f(y)$ equilibirum
# $y(t) =$ constant
# $y' = 0$
# $y_0$ is equilibrium iff $f(y_0) = 0$

# $y' = f(y, t)$
# 
# $z(t)$ candidate solution: is it a solution or not?
# 
# can calculate $z'(t) = f(z(t), t)$ is this true?
# 
# find the antiderivative of this function
# 
# Euler's method: integrating the function $f$ in some sense
# 
# $\int_{t_0}^{t} f(z(s), s) ds$
# 
# equivalent to saying $z(t) = y(t_0) + \int_{t_0}^{t} f(z(s), s) ds$
# 
# limit of Euler's method
# 
# fundamental theorem of calculus<br>
# $z(t) - z(t_0) = \int_{t_0}^t$
# 
# start with z, construct $z_1(t) = y(t_0) + \int_{t_0}^{t} f(z(s), s) ds$<br>
# start with z1, construct $z_2$
# 
# converges to actual solution exponentially fast
# 
# given z(t), construct z(t) according to rule
# 
# IVP
# 
# y' = f(y, t)
# 
# y(t_0) = y_0
# 
# prove one and only one solution
# 
# given function, construct new function by generalizing Euler's method
# 
# Piccard's method

# Catastrophe Theory
# 
# critical points of functions of several variables
# 
# ---
# 
# differential equations can be reduced to finding fixed point
# 
# ---
# 
# E^3 is R^3 + dot product
# Hamiltonian space
# 
# Jordan normal form<br>
# easiest form of non diagonalizable matrix
# 
# inner product: a function or binary operation to assign a number to two vectors<br>
# * linearity properties
# * $v \cdot v \ge 0$; if $v\cdot v = 0$ then $v = 0$
# 
# ---
# 
# general theory of quadratic forms
# determinant is 0, then in some directions error is more important than approximation

# positive definite property and symmetric property
# 
# Cauchy-Schwartz inequality<br>
# triangle inequality<br>
# isometry, the length of vector is conserved<br>

# symmetric, than roots of characteristic polynomial are real: diagonalizable 

# dot product of two function is an integral
# 
# $f \cdot g = \int_a^b f(x)g(x) dx$
# 
# in one situation, you don't care about
# * length of vector
# * angle between vector
# 
# introduce inner product, R^n becomes E^n
# 
# if you understand $||x|| = \sqrt{x^2 + ... + x^2}$ you understand every Euclidean space

# ---
