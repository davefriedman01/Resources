#!/usr/bin/env python
# coding: utf-8

# # Linear Algebra

# ---

# Linear algebra is the study of linear maps on finite-dimensional vector spaces.

# ---

# In[1]:


import numpy as np
import scipy
from sympy import *
init_printing()


# ---

# Solve the linear system
# $$
# \begin{align}
# 3x_1-2x_2+18x_3-19x_4&=5\\
# 2x_1+3x_2-x_3-4x_4&=-1\\
# 4x_1+5x_2+x_3-10x_4&=-1\\
# \end{align}
# \text{.}
# $$

# ---

# $$
# \begin{bmatrix}
# 3 & -2 & 18 & -19 & 5\\
# 2 & 3 & -1 & -4 & -1\\
# 4 & 5 & 1 & -10 & -1\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & -\frac{2}{3} & 6 & -\frac{19}{3} & \frac{5}{3}\\
# 2 & 3 & -1 & -4 & -1\\
# 4 & 5 & 1 & -10 & -1\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & -\frac{2}{3} & 6 & -\frac{19}{3} & \frac{5}{3}\\
# 0 & \frac{13}{3} & -13 & \frac{26}{3} & -\frac{13}{3}\\
# 4 & 5 & 1 & -10 & -1\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & -\frac{2}{3} & 6 & -\frac{19}{3} & \frac{5}{3}\\
# 0 & 1 & -3 & 2 & -1\\
# 4 & 5 & 1 & -10 & -1\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & -\frac{2}{3} & 6 & -\frac{19}{3} & \frac{5}{3}\\
# 0 & 1 & -3 & 2 & -1\\
# 0 & \frac{23}{3} & -23 & \frac{46}{3} & -\frac{23}{3}\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & -\frac{2}{3} & 6 & -\frac{19}{3} & \frac{5}{3}\\
# 0 & 1 & -3 & 2 & -1\\
# 0 & 1 & -3 & 2 & -1\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & -\frac{2}{3} & 6 & -\frac{19}{3} & \frac{5}{3}\\
# 0 & 1 & -3 & 2 & -1\\
# 0 & 0 & 0 & 0 & 0\\
# \end{bmatrix}
# \rightarrow
# \begin{bmatrix}
# 1 & 0 & 4 & -5 & 1\\
# 0 & 1 & -3 & 2 & -1\\
# 0 & 0 & 0 & 0 & 0\\
# \end{bmatrix}
# $$

# $$
# \begin{split}
# x_1&=-4s+5t+1\\
# x_2&=3s-2t-1\\
# x_3&=s\\
# x_4&=t\\
# \end{split}
# \rightarrow
# \begin{bmatrix}
# x_1\\
# x_2\\
# x_3\\
# x_4\\
# \end{bmatrix}
# =
# s
# \begin{bmatrix}
# -4\\
# 3\\
# 1\\
# 0\\
# \end{bmatrix}
# +
# t
# \begin{bmatrix}
# 5\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# +
# \begin{bmatrix}
# 1\\
# -1\\
# 0\\
# 0\\
# \end{bmatrix}
# $$

# In[2]:


M = Matrix(3, 5, [3, -2, 18, -19, 5, 2, 3, -1, -4, -1, 4, 5, 1, -10, -1])
M.rref()


# ---

# Find a $3\times 3$ matrix $T$ satisfying the following properties:
# * $\begin{bmatrix}1\\0\\0\\\end{bmatrix}$ is an eigenvector of $T$ associated with the eigenvalue $1$;
# * $\begin{bmatrix}1\\1\\0\\\end{bmatrix}$ is an eigenvector of $T$ associated with the eigenvalue $2$;
# * $\begin{bmatrix}1\\1\\1\\\end{bmatrix}$ is an eigenvector of $T$ associated with the eigenvalue $3$.

# ---

# $$
# T
# =
# \begin{bmatrix}
# 1 & 1 & 1\\
# 0 & 2 & 1\\
# 0 & 0 & 3\\
# \end{bmatrix}
# $$
# 
# $$
# T\mathbf{v_1}=
# \begin{bmatrix}
# 1 & 1 & 1\\
# 0 & 2 & 1\\
# 0 & 0 & 3\\
# \end{bmatrix}
# \begin{bmatrix}1\\0\\0\\\end{bmatrix}
# =
# \begin{bmatrix}1\\0\\0\\\end{bmatrix}
# =
# 1\begin{bmatrix}1\\0\\0\\\end{bmatrix}
# =
# \lambda_1\mathbf{v_1}
# $$
# 
# $$
# T\mathbf{v_2}=
# \begin{bmatrix}
# 1 & 1 & 1\\
# 0 & 2 & 1\\
# 0 & 0 & 3\\
# \end{bmatrix}
# \begin{bmatrix}1\\1\\0\\\end{bmatrix}
# =
# \begin{bmatrix}2\\2\\0\\\end{bmatrix}
# =
# 2\begin{bmatrix}1\\1\\0\\\end{bmatrix}
# =
# \lambda_2\mathbf{v_2}
# $$
# 
# $$
# T\mathbf{v_3}=
# \begin{bmatrix}
# 1 & 1 & 1\\
# 0 & 2 & 1\\
# 0 & 0 & 3\\
# \end{bmatrix}
# \begin{bmatrix}1\\1\\1\\\end{bmatrix}
# =
# \begin{bmatrix}3\\3\\3\\\end{bmatrix}
# =
# 3\begin{bmatrix}1\\1\\1\\\end{bmatrix}
# =
# \lambda_3\mathbf{v_3}
# $$

# In[3]:


T = np.array([1, 1, 1, 0, 2, 1, 0, 0, 3]).reshape(3, 3)
v1 = np.array([1, 0, 0])
v2 = np.array([1, 1, 0])
v3 = np.array([1, 1, 1])
print(np.dot(T, v1))
print(np.dot(T, v2))
print(np.dot(T, v3))


# ---

# The volume of the parallelotope built on the columns of a matrix $M$ is $\sqrt{det(M^TM)}$. Compute $\sqrt{det(M^TM)}$ for
# $$
# M=
# \begin{bmatrix}
# 3 & 5 & -1\\
# -1 & -2 & 1\\
# 2 & 4 & -2\\
# -4 & 1 & 5\\
# \end{bmatrix}
# \text{.}
# $$

# ---

# $$
# M^TM
# =
# \begin{bmatrix}
# 3 & -1 & 2 & -4\\
# 5 & -2 & 4 & 1\\
# -1 & 1 & -2 & 5\\
# \end{bmatrix}
# \begin{bmatrix}
# 3 & 5 & -1\\
# -1 & -2 & 1\\
# 2 & 4 & -2\\
# -4 & 1 & 5\\
# \end{bmatrix}
# $$

# $$
# \begin{align}
# (3)(3)+(-1)(-1)+(2)(2)+(-4)(-4) &= 30\\
# (3)(5)+(-1)(-2)+(2)(4)+(-4)(1) &= 21\\
# (3)(-1)+(-1)(1)+(2)(-2)+(-4)(5) &= -28\\
# (5)(3)+(-2)(-1)+(4)(2)+(1)(-4) &= 21\\
# (5)(5)+(-2)(-2)+(4)(4)+(1)(1) &= 46\\
# (5)(-1)+(-2)(1)+(4)(-2)+(1)(5) &= -10\\
# (-1)(3)+(1)(-1)+(-2)(2)+(5)(-4) &= -28\\
# (-1)(5)+(1)(-2)+(-2)(4)+(5)(1) &= -10\\
# (-1)(-1)+(1)(1)+(-2)(-2)+(5)(5) &= 31\\
# \end{align}
# $$

# $$
# =
# \begin{bmatrix}
# 30 & 21 & -28\\
# 21 & 46 & -10\\
# -28 & -10 & 31\\
# \end{bmatrix}
# $$

# $$
# \begin{vmatrix}
# 30 & 21 & -28\\
# 21 & 46 & -10\\
# -28 & -10 & 31\\
# \end{vmatrix}
# =
# 30
# \begin{vmatrix}
# 46 & -10\\
# -10 & 31\\
# \end{vmatrix}
# -
# 21
# \begin{vmatrix}
# 21 & -10\\
# -28 & 31\\
# \end{vmatrix}
# +
# -28
# \begin{vmatrix}
# 21 & 46\\
# -28 & -10\\
# \end{vmatrix}\\
# =
# 30((46)(31)-(-10)(-10))-21((21)(31)-(-10)(-28))-28((21)(-10)-(46)(-28))\\
# =
# 30(1426-100)-21(651-280)-28(-210+1288)\\
# =
# 30(1326)-21(371)-28(1078)\\
# =
# 1805\\
# $$
# 
# $$
# \sqrt{1805}\approx 42.5
# $$

# In[4]:


M3 = np.array([3, 5, -1, -1, -2, 1, 2, 4, -2, -4, 1, 5]).reshape(4, 3)
M3TM3 = np.dot(M3.T, M3)
M3TM3


# In[5]:


np.sqrt(np.linalg.det(M3TM3))


# ---

# Compute the orthogonal projection of the vector $\begin{bmatrix}17\\3\\-14\\6\\\end{bmatrix}$ onto the linear subspace $\mathbb{R}^4$ spanned by the vectors $\begin{bmatrix}2\\3\\-1\\-4\\\end{bmatrix}$ and $\begin{bmatrix}4\\5\\-2\\1\\\end{bmatrix}$.

# ---

# See attached

# ---

# Find the matrix representing the linear transformation $L : \mathbb{R}^3\rightarrow\mathbb{R}^3$ which reflects the points of $\mathbb{R}^3$ through the plane $2x-y+3z=0$.

# ---

# $$
# 2x-y+3z=0
# \rightarrow
# \left\{
# \begin{bmatrix}
# x_1\\
# x_2\\
# x_3\\
# \end{bmatrix}
# \text{s.t.}
# \begin{bmatrix}
# 2\\
# -1\\
# 3\\
# \end{bmatrix}
# \perp
# \begin{bmatrix}
# x_1\\
# x_2\\
# x_3\\
# \end{bmatrix}
# \right\}
# $$

# Norm of the vector normal to the plane of reflection.

# $$
# \left\Vert
# \begin{bmatrix}
# 2\\
# -1\\
# 3\\
# \end{bmatrix}
# \right\Vert
# =\sqrt{2^2+(-1)^2+3^2}
# =\sqrt{4+1+9}
# =\sqrt{14}
# $$

# Unit vector of the vector normal to the plane of reflection.

# $$
# \frac{
# \begin{bmatrix}
# 2\\
# -1\\
# 3\\
# \end{bmatrix}
# }
# {
# \left\Vert
# \begin{bmatrix}
# 2\\
# -1\\
# 3\\
# \end{bmatrix}
# \right\Vert
# }
# =
# \frac{1}{\sqrt{14}}
# \begin{bmatrix}
# 2\\
# -1\\
# 3\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# \frac{2}{\sqrt{14}}\\
# -\frac{1}{\sqrt{14}}\\
# \frac{3}{\sqrt{14}}\\
# \end{bmatrix}
# $$

# __Orthogonal Decomposition Theorem__ Given a two-dimensional linear subspace $W$ in $\mathbb{R}^3$ (i.e., a plane), a point $\mathbf{y}\in\mathbb{R}^3$ consists of the sum of a unique orthogonal projection $\mathbf{y_{||}}$ of $\mathbf{y}$ onto $W$ and the unique component $\mathbf{y_{\perp}}$ of $\mathbf{y}$ orthogonal to $W$. In other words, $\mathbf{y}=\mathbf{y_{||}}+\mathbf{y_{\perp}}$
# 
# $L$ reverses the orthogonal component of a point $\mathbf{y}\in\mathbb{R}^3$.
# 
# $$
# M\mathbf{y}
# $$
# $$
# =I(\mathbf{y_{||}}-\mathbf{y_{\perp}})
# $$
# $$
# =I\mathbf{y_{||}}-I\mathbf{y_{\perp}}
# $$
# $$
# =I(\mathbf{y}-\mathbf{y_{\perp}})-I\mathbf{y_{\perp}}
# $$
# $$
# =I\mathbf{y}-I\mathbf{y_{\perp}}-I\mathbf{y_{\perp}}
# $$
# $$
# =I\mathbf{y}-2I\mathbf{y_{\perp}}
# $$

# $$
# \mathbf{y_{\perp}}
# =r\mathbf{n}\,\text{where}\,\mathbf{n}\,\text{is the unit vector normal to the plane of reflection and}\,r\,\text{is some scalar}
# $$
# $$
# (\mathbf{y}-r\mathbf{n})\cdot\mathbf{n}=0
# $$
# $$
# \mathbf{y}\cdot\mathbf{n}-(r\mathbf{n})\cdot\mathbf{n}=0
# $$
# $$
# \mathbf{y}\cdot\mathbf{n}=r(\mathbf{n}\cdot\mathbf{n})
# $$
# $$
# r=\frac{\mathbf{y}\cdot\mathbf{n}}{\mathbf{n}\cdot\mathbf{n}}
# $$

# $$
# =I\mathbf{y}-2I\mathbf{y_{\perp}}
# $$
# $$
# =I\mathbf{y}-2I(r\mathbf{n})
# $$
# $$
# =I\mathbf{y}-2I\left(\frac{\mathbf{y}\cdot\mathbf{n}}{\mathbf{n}\cdot\mathbf{n}}\mathbf{n}\right)
# $$
# $$
# =I\mathbf{y}-2I(\mathbf{y}\cdot\mathbf{n})\mathbf{n}
# $$
# $$
# =I\mathbf{y}-2I\mathbf{y}\mathbf{n^T}\mathbf{n}
# $$
# $$
# =(I-2I\mathbf{n^T}\mathbf{n})\mathbf{y}
# $$

# $$
# I-2
# \begin{bmatrix}
# \frac{2}{\sqrt{14}}\\
# -\frac{1}{\sqrt{14}}\\
# \frac{3}{\sqrt{14}}\\
# \end{bmatrix}
# \begin{bmatrix}
# \frac{2}{\sqrt{14}} & -\frac{1}{\sqrt{14}} & \frac{3}{\sqrt{14}}\\
# \end{bmatrix}
# $$
# $$
# =
# I-2
# \begin{bmatrix}
# \frac{2}{\sqrt{14}}\frac{2}{\sqrt{14}} & \frac{2}{\sqrt{14}}\left(-\frac{1}{\sqrt{14}}\right) & \frac{2}{\sqrt{14}}\frac{3}{\sqrt{14}}\\
# \left(-\frac{1}{\sqrt{14}}\right)\frac{2}{\sqrt{14}} & \left(-\frac{1}{\sqrt{14}}\right)\left(-\frac{1}{\sqrt{14}}\right) & \left(-\frac{1}{\sqrt{14}}\right)\frac{3}{\sqrt{14}}\\
# \frac{3}{\sqrt{14}}\frac{2}{\sqrt{14}} & \frac{3}{\sqrt{14}}\left(-\frac{1}{\sqrt{14}}\right) & \frac{3}{\sqrt{14}}\frac{3}{\sqrt{14}}\\
# \end{bmatrix}
# $$
# $$
# =
# I-2
# \begin{bmatrix}
# \frac{4}{14} & -\frac{2}{14} & \frac{6}{14}\\
# -\frac{2}{14} & \frac{1}{14} & -\frac{3}{14}\\
# \frac{6}{14} & -\frac{3}{14} & \frac{9}{14}\\
# \end{bmatrix}
# $$
# $$
# =
# I-
# \begin{bmatrix}
# \frac{8}{14} & -\frac{4}{14} & \frac{12}{14}\\
# -\frac{4}{14} & \frac{2}{14} & -\frac{6}{14}\\
# \frac{12}{14} & -\frac{6}{14} & \frac{18}{14}\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & 0 & 0\\
# 0 & 1 & 0\\
# 0 & 0 & 1\\
# \end{bmatrix}
# -
# \begin{bmatrix}
# \frac{8}{14} & -\frac{4}{14} & \frac{12}{14}\\
# -\frac{4}{14} & \frac{2}{14} & -\frac{6}{14}\\
# \frac{12}{14} & -\frac{6}{14} & \frac{18}{14}\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1-\frac{8}{14} & \frac{4}{14} & -\frac{12}{14}\\
# \frac{4}{14} & 1-\frac{2}{14} & \frac{6}{14}\\
# -\frac{12}{14} & \frac{6}{14} & 1-\frac{18}{14}\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# \frac{6}{14} & \frac{4}{14} & -\frac{12}{14}\\
# \frac{4}{14} & \frac{12}{14} & \frac{6}{14}\\
# -\frac{12}{14} & \frac{6}{14} & -\frac{4}{14}\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# \frac{3}{7} & \frac{2}{7} & -\frac{6}{7}\\
# \frac{2}{7} & \frac{6}{7} & \frac{3}{7}\\
# -\frac{6}{7} & \frac{3}{7} & -\frac{2}{7}\\
# \end{bmatrix}
# $$

# In[6]:


N = np.array([[2], [-1], [3]])
n = np.multiply(np.divide(1, np.sqrt(np.square(N).sum())), N)
assert np.divide(1, np.sqrt((n**2).sum())) == 1
assert np.dot(n.T, n)
n


# In[7]:


M = np.array([[3/7, 2/7, -6/7], [2/7, 6/7, 3/7], [-6/7, 3/7, -2/7]])
M


# In[8]:


y = np.array([[1], [2], [3]])
ref = np.dot(M, y)
ref


# In[9]:


y_orth = np.multiply(np.dot(y.T, n), n)
y_orth


# In[10]:


y-2*y_orth


# ---

# Consider the matrix
# $$
# H=
# \begin{bmatrix}
# 2 & -1 & 1 & -3 & -3\\
# -3 & 1 & -2 & 2 & 1\\
# 0 & 2 & 2 & 2 & 6\\
# \end{bmatrix}
# \text{.}
# $$
# (a) Find the reduced row echelon matrix which is row equivalent to $H$.<br>
# (b) Obtain a basis for the nullspace of $H$.<br>
# (c) Compute the rank of $H$.<br>

# ---

# $$
# \begin{bmatrix}
# 2 & -1 & 1 & -3 & -3\\
# -3 & 1 & -2 & 2 & 1\\
# 0 & 2 & 2 & 2 & 6\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & -\frac{1}{2} & \frac{1}{2} & -\frac{3}{2} & -\frac{3}{2}\\
# -3 & 1 & -2 & 2 & 1\\
# 0 & 2 & 2 & 2 & 6\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & -\frac{1}{2} & \frac{1}{2} & -\frac{3}{2} & -\frac{3}{2}\\
# 0 & -\frac{1}{2} & -\frac{1}{2} & -\frac{5}{2} & -\frac{7}{2}\\
# 0 & 2 & 2 & 2 & 6\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & -\frac{1}{2} & \frac{1}{2} & -\frac{3}{2} & -\frac{3}{2}\\
# 0 & 1 & 1 & 5 & 7\\
# 0 & 2 & 2 & 2 & 6\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & -\frac{1}{2} & \frac{1}{2} & -\frac{3}{2} & -\frac{3}{2}\\
# 0 & 1 & 1 & 5 & 7\\
# 0 & 0 & 0 & -8 & -8\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & -\frac{1}{2} & \frac{1}{2} & -\frac{3}{2} & -\frac{3}{2}\\
# 0 & 1 & 1 & 5 & 7\\
# 0 & 0 & 0 & 1 & 1\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & -\frac{1}{2} & \frac{1}{2} & 0 & 0\\
# 0 & 1 & 1 & 0 & 2\\
# 0 & 0 & 0 & 1 & 1\\
# \end{bmatrix}
# $$
# $$
# =
# \begin{bmatrix}
# 1 & 0 & 1 & 0 & 1\\
# 0 & 1 & 1 & 0 & 2\\
# 0 & 0 & 0 & 1 & 1\\
# \end{bmatrix}
# $$

# $Nul(H)$ is found by solving the homogeneous system $H\mathbf{x}=\mathbf{0}$ which is done by row reduction of the augmented matrix.

# $$
# x_1+x_3+x_5=0\rightarrow x_1=-x_3-x_5\\
# x_2+x_3+2x_5=0\rightarrow x_2=-x_3-2x_5\\
# x_4+x_5=0\rightarrow x_4=-x_5
# $$

# $$
# \begin{split}
# x_1&=-s-t\\
# x_2&=-s-2t\\
# x_4&=-t\\
# x_3&=s\\
# x_5&=t\\
# \end{split}
# \rightarrow
# \begin{bmatrix}
# x_1\\
# x_2\\
# x_3\\
# x_4\\
# x_5\\
# \end{bmatrix}
# =
# s
# \begin{bmatrix}
# -1\\
# -1\\
# 0\\
# 1\\
# 0\\
# \end{bmatrix}
# +
# t
# \begin{bmatrix}
# -1\\
# -2\\
# -1\\
# 0\\
# 1\\
# \end{bmatrix}
# $$

# $$
# Nul(H)=span
# \left\{
# \begin{bmatrix}
# -1\\
# -1\\
# 0\\
# 1\\
# 0\\
# \end{bmatrix}
# ,
# \begin{bmatrix}
# -1\\
# -2\\
# -1\\
# 0\\
# 1\\
# \end{bmatrix}
# \right\}
# \rightarrow
# basis(H)=
# \left\{
# \begin{bmatrix}
# -1\\
# -1\\
# 0\\
# 1\\
# 0\\
# \end{bmatrix}
# ,
# \begin{bmatrix}
# -1\\
# -2\\
# -1\\
# 0\\
# 1\\
# \end{bmatrix}
# \right\}
# $$

# By the rank theorem,
# $
# rk(H)+dim(Nul(H))=num\_cols(H)
# \rightarrow rk(H)=num\_cols(H)-dim(Nul(H))
# =5-2
# =3
# $

# In[11]:


M6 = Matrix(3, 5, [2, -1, 1, -3, -3, -3, 1, -2, 2, 1, 0, 2, 2, 2, 6])
M6


# In[12]:


M6.rref()


# ---

# Consider the matrix
# $$
# F=
# \begin{bmatrix}
# -6 & 3 & -2 & 2\\
# -1 & 2 & 0 & 1\\
# -3 & 0 & -1 & 1\\
# 5 & 8 & 3 & -3\\
# \end{bmatrix}
# $$
# (a) Compute $F^{-1}$, the inverse of $F$.<br>
# (b) Compute $det(F)$.<br>

# ---

# $F\rightarrow I$ and $I\rightarrow F^{-1}$
# 1. $r_1,r_2\leftarrow r_2,r_1$
# 2. $r_1\leftarrow -r_1$
# 3. $r_2\leftarrow r_2+6r_1$
# 4. $r_3\leftarrow r_3+3r_1$
# 5. $r_4\leftarrow r_4-5r_1$
# 6. $r_2\leftarrow -\frac{1}{9}r_2$
# 7. $r_3\leftarrow r_3+6r_2$
# 8. $r_4\leftarrow r_4-18r_2$
# 9. $r_3\leftarrow 3r_3$
# 10. $r_4\leftarrow r_4+r_3$
# 11. $r_4\leftarrow -\frac{1}{4}r_4$
# 12. $r_3\leftarrow r_3-2r_4$
# 13. $r_2\leftarrow r_2-\frac{4}{9}r_4$
# 14. $r_1\leftarrow r_1+r_4$
# 15. $r_2\leftarrow r_2-\frac{2}{9}r_3$
# 16. $r_1\leftarrow r_1+2r_2$

# $$
# \begin{bmatrix}
# -6 & 3 & -2 & 2\\
# -1 & 2 & 0 & 1\\
# -3 & 0 & -1 & 1\\
# 5 & 8 & 3 & -3\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# -1 & 2 & 0 & 1\\
# -6 & 3 & -2 & 2\\
# -3 & 0 & -1 & 1\\
# 5 & 8 & 3 & -3\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# -6 & 3 & -2 & 2\\
# -3 & 0 & -1 & 1\\
# 5 & 8 & 3 & -3\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & -9 & -2 & -4\\
# -3 & 0 & -1 & 1\\
# 5 & 8 & 3 & -3\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & -9 & -2 & -4\\
# 0 & -6 & -1 & -2\\
# 5 & 8 & 3 & -3\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & -9 & -2 & -4\\
# 0 & -6 & -1 & -2\\
# 0 & 18 & 3 & 2\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & -6 & -1 & -2\\
# 0 & 18 & 3 & 2\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & 0 & \frac{1}{3} & \frac{2}{3}\\
# 0 & 18 & 3 & 2\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & 0 & \frac{1}{3} & \frac{2}{3}\\
# 0 & 0 & -1 & -6\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & 0 & 1 & 2\\
# 0 & 0 & -1 & -6\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & 0 & 1 & 2\\
# 0 & 0 & 0 & -4\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & 0 & 1 & 2\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & \frac{4}{9}\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & -1\\
# 0 & 1 & \frac{2}{9} & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & 0\\
# 0 & 1 & \frac{2}{9} & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & -2 & 0 & 0\\
# 0 & 1 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 1 & 0 & 0 & 0\\
# 0 & 1 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# $$

# $$
# \begin{bmatrix}
# 1 & 0 & 0 & 0\\
# 0 & 1 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & 1 & 0 & 0\\
# 1 & 0 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# 1 & 0 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# 1 & -6 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# 1 & -6 & 0 & 0\\
# 0 & -3 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# 1 & -6 & 0 & 0\\
# 0 & -3 & 1 & 0\\
# 0 & 5 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{3} & 0 & 0\\
# 0 & -3 & 1 & 0\\
# 0 & 5 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{3} & 0 & 0\\
# -\frac{2}{3} & 1 & 1 & 0\\
# 0 & 5 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{3} & 0 & 0\\
# -\frac{2}{3} & 1 & 1 & 0\\
# 2 & -7 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{3} & 0 & 0\\
# -2 & 3 & 3 & 0\\
# 2 & -7 & 0 & 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{3} & 0 & 0\\
# -2 & 3 & 3 & 0\\
# 0 & 1 & -\frac{3}{4} & -\frac{1}{4}\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{3} & 0 & 0\\
# -2 & 1 & \frac{9}{2} & \frac{1}{2}\\
# 0 & 1 & -\frac{3}{4} & -\frac{1}{4}\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & -1 & 0 & 0\\
# -\frac{1}{9} & \frac{2}{9} & \frac{1}{3} & \frac{1}{9}\\
# -2 & 1 & \frac{9}{2} & \frac{1}{2}\\
# 0 & 1 & -\frac{3}{4} & -\frac{1}{4}\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & 0 & -\frac{3}{4} & -\frac{1}{4}\\
# -\frac{1}{9} & \frac{2}{9} & \frac{1}{3} & \frac{1}{9}\\
# -2 & 1 & \frac{9}{2} & \frac{1}{2}\\
# 0 & 1 & -\frac{3}{4} & -\frac{1}{4}\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0 & 0 & -\frac{3}{4} & -\frac{1}{4}\\
# \frac{1}{3} & 0 & -\frac{2}{3} & 0\\
# -2 & 1 & \frac{9}{2} & \frac{1}{2}\\
# 0 & 1 & -\frac{3}{4} & -\frac{1}{4}\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# \frac{2}{3} & 0 & -\frac{25}{12} & -\frac{1}{4}\\
# \frac{1}{3} & 0 & -\frac{2}{3} & 0\\
# -2 & 1 & \frac{9}{2} & \frac{1}{2}\\
# 0 & 1 & -\frac{3}{4} & -\frac{1}{4}\\
# \end{bmatrix}
# $$

# $$
# \begin{vmatrix}
# -6 & 3 & -2 & 2\\
# -1 & 2 & 0 & 1\\
# -3 & 0 & -1 & 1\\
# 5 & 8 & 3 & -3\\
# \end{vmatrix}
# =
# -6
# \begin{vmatrix}
# 2 & 0 & 1\\
# 0 & -1 & 1\\
# 8 & 3 & -3\\
# \end{vmatrix}
# -
# 3
# \begin{vmatrix}
# -1 & 0 & 1\\
# -3 & -1 & 1\\
# 5 & 3 & -3\\
# \end{vmatrix}
# +
# -2
# \begin{vmatrix}
# -1 & 2 & 1\\
# -3 & 0 & 1\\
# 5 & 8 & -3\\
# \end{vmatrix}
# -
# 2
# \begin{vmatrix}
# -1 & 2 & 0\\
# -3 & 0 & -1\\
# 5 & 8 & 3\\
# \end{vmatrix}
# $$

# $$
# =-6[(2)(-1)(-3)+(0)(1)(8)+(1)(0)(-3)-(1)(-1)(8)-(2)(1)(3)-(0)(0)(-3)]
# -3[(-1)(-1)(-3)+(0)(1)(5)+(1)(-3)(3)-(1)(-1)(5)-(-1)(1)(3)-(0)(-3)(-3)]
# -2[(-1)(0)(-3)+(2)(1)(5)+(1)(-3)(8)-(1)(0)(5)-(-1)(1)(8)-(2)(-3)(-3)]
# -2[(-1)(0)(3)+(2)(-1)(5)+(0)(-3)(8)-(0)(0)(5)-(-1)(-1)(8)-(2)(-3)(3)]
# $$
# $$
# =-6[6+0+0+8-6+0]
# -3[-3+0-9+5+3+0]
# -2[0+10-24+0+8-18]
# -2[0-10+0+0-8+18]
# $$
# $$
# =-6[8]
# -3[-4]
# -2[-24]
# -2[0]
# $$
# $$
# =-48+12+48
# $$
# $$
# =12
# $$

# In[13]:


M7 = Matrix(4, 4, [-6, 3, -2, 2, -1, 2, 0, 1, -3, 0, -1, 1, 5, 8, 3, -3])
M7


# In[14]:


M7.rref()


# In[15]:


M7.inv()


# In[16]:


M7.det()


# ---

# Consider the symmetric matrix
# $$
# S=
# \begin{bmatrix}
# -3 & 6 & -2 & 0\\
# 6 & 3 & 0 & 2\\
# -2 & 0 & 3 & 6\\
# 0 & 2 & 6 & -3\\
# \end{bmatrix}
# $$
# (a) Compute the characteristic polynomial of $S$.<br>
# (b) Find the eigenvalues of $S$ and their algebraic multiplicities.<br>
# (c) Obtain an orthonormal basis for each eigenspace of $S$.<br>
# (d) Find an orthogonal matrix $Q$ such that $Q^TSQ$ is diagonal.<br>
# (e) Write the vector $\begin{bmatrix}-8\\10\\0\\9\\\end{bmatrix}$ as a sum of eigenvectors of S.<br>

# In[17]:


S = Matrix(4, 4, [-3, 6, -2, 0, 6, 3, 0, 2, -2, 0, 3, 6, 0, 2, 6, -3])
S


# ---

# $$
# det(S-\lambda I)
# =
# \begin{vmatrix}
# -3-\lambda & 6 & -2 & 0\\
# 6 & 3-\lambda & 0 & 2\\
# -2 & 0 & 3-\lambda & 6\\
# 0 & 2 & 6 & -3-\lambda\\
# \end{vmatrix}
# $$

# $$
# =
# (-3-\lambda)
# \begin{vmatrix}
# 3-\lambda & 0 & 2\\
# 0 & 3-\lambda & 6\\
# 2 & 6 & -3-\lambda\\
# \end{vmatrix}
# -
# 6
# \begin{vmatrix}
# 6 & 0 & 2\\
# -2 & 3-\lambda & 6\\
# 0 & 6 & -3-\lambda\\
# \end{vmatrix}
# +
# -2
# \begin{vmatrix}
# 6 & 3-\lambda & 2\\
# -2 & 0 & 6\\
# 0 & 2 & -3-\lambda\\
# \end{vmatrix}
# -
# 0
# \begin{vmatrix}
# 6 & 3-\lambda & 0\\
# -2 & 0 & 3-\lambda\\
# 0 & 2 & 6\\
# \end{vmatrix}
# $$

# $$
# =
# (-3-\lambda)
# \begin{vmatrix}
# 3-\lambda & 0 & 2\\
# 0 & 3-\lambda & 6\\
# 2 & 6 & -3-\lambda\\
# \end{vmatrix}
# -
# 6
# \begin{vmatrix}
# 6 & 0 & 2\\
# -2 & 3-\lambda & 6\\
# 0 & 6 & -3-\lambda\\
# \end{vmatrix}
# +
# -2
# \begin{vmatrix}
# 6 & 3-\lambda & 2\\
# -2 & 0 & 6\\
# 0 & 2 & -3-\lambda\\
# \end{vmatrix}
# $$

# $$
# =
# (-3-\lambda)[(3-\lambda)^2(-3-\lambda)-4(3-\lambda)-36(3-\lambda)]
# $$
# $$
# -6[6(3-\lambda)(-3-\lambda)-24-216]
# $$
# $$
# -2[-8-72+2(3-\lambda)(-3-\lambda)]
# $$

# $$
# =
# (-3-\lambda)[(9-6\lambda+\lambda^2)(-3-\lambda)-4(3-\lambda)-36(3-\lambda)]
# $$
# $$
# -6[6(-9+\lambda^2)-240]
# $$
# $$
# -2[-80+2(-9+\lambda^2)]
# $$

# $$
# =
# (-3-\lambda)[-27-9\lambda+18\lambda+6\lambda^2-3\lambda^2-\lambda^3-12+4\lambda-108+36\lambda]
# $$
# $$
# -6[-54+6\lambda^2-240]
# $$
# $$
# -2[-80-18+2\lambda^2]
# $$

# $$
# =
# (-3-\lambda)[-\lambda^3+3\lambda^2+49\lambda-147]
# $$
# $$
# -6[6\lambda^2-298]
# $$
# $$
# -2[2\lambda^2-98]
# $$

# $$
# =
# \lambda^4-3\lambda^3-49\lambda^2+147\lambda+3\lambda^3-9\lambda^2-147\lambda+441
# $$
# $$
# -36\lambda^2+1788
# $$
# $$
# -4\lambda^2+196
# $$

# $$
# =
# \lambda^4-58\lambda^2+441
# $$
# $$
# -36\lambda^2+1788
# $$
# $$
# -4\lambda^2+196
# $$

# $$
# =
# \lambda^4-98\lambda^2+2425
# $$

# $$
# 0
# =
# (\lambda^2-49)^2
# $$
# 
# $$
# 0
# =
# (\lambda^2-49)(\lambda^2-49)
# $$
# 
# $$
# \lambda^2
# =
# 49
# $$
# 
# $$
# \lambda
# =
# \sqrt{49}
# $$
# 
# $$
# \lambda
# =
# \pm 7
# $$
# $7$ has multiplicity $2$ and $-7$ has multiplicity $2$.

# In[18]:


p = S.charpoly().as_expr()
factor(p)


# In[19]:


S.eigenvals()


# $\lambda=7$
# 
# $$
# \begin{bmatrix}
# -3-7 & 6 & -2 & 0 & 0\\
# 6 & 3-7 & 0 & 2 & 0\\
# -2 & 0 & 3-7 & 6 & 0\\
# 0 & 2 & 6 & -3-7 & 0\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# -10 & 6 & -2 & 0 & 0\\
# 6 & -4 & 0 & 2 & 0\\
# -2 & 0 & -4 & 6 & 0\\
# 0 & 2 & 6 & -10 & 0\\
# \end{bmatrix}
# =
# ...
# =
# \begin{bmatrix}
# 1 & 0 & 2 & -3 & 0\\
# 0 & 1 & 3 & -5 & 0\\
# 0 & 0 & 0 & 0 & 0\\
# 0 & 0 & 0 & 0 & 0\\
# \end{bmatrix}
# $$
# 
# $$
# x_1+2x_3-3x_4=0\rightarrow x_1=-2x_3+3x_4\\
# x_2+3x_3-5x_4=0\rightarrow x_2=-3x_3+5x_4\\
# $$
# 
# $$
# \begin{split}
# x_1&=-2s+3t\\
# x_2&=-3s+5t\\
# x_3&=s\\
# x_4&=t\\
# \end{split}
# \rightarrow
# \begin{bmatrix}
# x_1\\
# x_2\\
# x_3\\
# x_4\\
# \end{bmatrix}
# =
# s
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0\\
# \end{bmatrix}
# +
# t
# \begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# $$
# 
# $$
# Nul(S-\lambda I)=span
# \left\{
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0\\
# \end{bmatrix}
# ,
# \begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# \right\}
# \rightarrow
# basis(S-\lambda I)=
# \left\{
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0\\
# \end{bmatrix}
# ,
# \begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# \right\}
# $$

# In[20]:


(S-7*eye(4)).nullspace()


# $$
# \mathbf{v_1}
# =
# \mathbf{x_1}
# =
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# $$
# 
# $$
# \mathbf{v_2}
# =
# \mathbf{x_2}-\frac{\mathbf{x_2}\cdot\mathbf{v_1}}{\mathbf{v_1}\cdot\mathbf{v_1}}\mathbf{v_1}
# =
# \begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# -
# \frac{\begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# \cdot
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}}
# {\begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# \cdot
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}}
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# +
# \frac{3}{2}
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# 3\\
# 5\\
# 0\\
# 1\\
# \end{bmatrix}
# +
# \begin{bmatrix}
# -3\\
# -\frac{9}{2}\\
# \frac{3}{2}\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0\\
# \frac{1}{2}\\
# \frac{3}{2}\\
# 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0\\
# 1\\
# 3\\
# 2\\
# \end{bmatrix}
# $$

# In[21]:


GramSchmidt((S-7*eye(4)).nullspace())


# $$
# \left\Vert
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# \right\Vert
# =
# \sqrt{(-2)^2+(-3)^2+1^2+0^2}
# =
# \sqrt{4+9+1}
# =
# \sqrt{14}
# $$
# 
# $$
# \frac{
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}}{
# \left\Vert
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# \right\Vert}
# =
# \frac{1}{\sqrt{14}}
# \begin{bmatrix}
# -2\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}}\\
# -\frac{3}{\sqrt{14}}\\
# \frac{1}{\sqrt{14}}\\
# 0
# \end{bmatrix}
# $$
# 
# $$
# \left\Vert
# \begin{bmatrix}
# 0\\
# \frac{1}{2}\\
# \frac{3}{2}\\
# 1\\
# \end{bmatrix}
# \right\Vert
# =
# \sqrt{0^2+\left(\frac{1}{2}\right)^2+\left(\frac{3}{2}\right)^2+1^2}
# =
# \sqrt{\frac{1}{4}+\frac{9}{4}+1}
# =
# \sqrt{\frac{14}{4}}
# =
# \sqrt{\frac{7}{2}}
# $$
# 
# $$
# \frac{
# \begin{bmatrix}
# 0\\
# \frac{1}{2}\\
# \frac{3}{2}\\
# 1\\
# \end{bmatrix}}{
# \left\Vert
# \begin{bmatrix}
# 0\\
# \frac{1}{2}\\
# \frac{3}{2}\\
# 1\\
# \end{bmatrix}
# \right\Vert}
# =
# \frac{1}{\sqrt{\frac{7}{2}}}
# \begin{bmatrix}
# 0\\
# \frac{1}{2}\\
# \frac{3}{2}\\
# 1\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0\\
# \frac{1}{2\sqrt{\frac{7}{2}}}\\
# \frac{3}{2\sqrt{\frac{7}{2}}}\\
# \frac{1}{\sqrt{\frac{7}{2}}}\\
# \end{bmatrix}
# $$

# Therefore, an orthonormal basis for the eigenspace of $S$ associatd with the eigenvalue $\lambda=7$ is
# 
# $$
# \left\{
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}}\\
# -\frac{3}{\sqrt{14}}\\
# \frac{1}{\sqrt{14}}\\
# 0
# \end{bmatrix}
# ,
# \begin{bmatrix}
# 0\\
# \frac{1}{2\sqrt{\frac{7}{2}}}\\
# \frac{3}{2\sqrt{\frac{7}{2}}}\\
# \frac{1}{\sqrt{\frac{7}{2}}}\\
# \end{bmatrix}
# \right\}
# $$

# In[22]:


v1 = np.array([-2, -3, 1, 0])
x2 = np.array([3, 5, 0, 1])
v2 = x2 - np.dot((np.dot(x2, v1)/np.dot(v1, v1)), v1)

v1u = v1/np.linalg.norm(v1)
v2u = v2/np.linalg.norm(v2)

print(v1)
print(v1u)
print(v2)
print(v2u)
print(np.dot(v1u, v1u))
print(np.dot(v2u, v2u))
print(np.dot(v1u, v2u))


# $\lambda=-7$
# 
# $$
# \begin{bmatrix}
# -3+7 & 6 & -2 & 0 & 0\\
# 6 & 3+7 & 0 & 2 & 0\\
# -2 & 0 & 3+7 & 6 & 0\\
# 0 & 2 & 6 & -3+7 & 0\\
# \end{bmatrix}
# =
# \begin{bmatrix}
# 4 & 6 & -2 & 0 & 0\\
# 6 & 10 & 0 & 2 & 0\\
# -2 & 0 & 10 & 6 & 0\\
# 0 & 2 & 6 & 4 & 0\\
# \end{bmatrix}
# =
# ...
# =
# \begin{bmatrix}
# 1 & 0 & -5 & -3 & 0\\
# 0 & 1 & 3 & 2 & 0\\
# 0 & 0 & 0 & 0 & 0\\
# 0 & 0 & 0 & 0 & 0\\
# \end{bmatrix}
# $$
# 
# $$
# x_1-5x_3-3x_4=0\rightarrow x_1=5x_3+3x_4\\
# x_2+3x_3+2x_4=0\rightarrow x_2=-3x_3-2x_4\\
# $$
# 
# $$
# \begin{split}
# x_1&=5s+3t\\
# x_2&=-3s-2t\\
# x_3&=s\\
# x_4&=t\\
# \end{split}
# \rightarrow
# \begin{bmatrix}
# x_1\\
# x_2\\
# x_3\\
# x_4\\
# \end{bmatrix}
# =
# s
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0\\
# \end{bmatrix}
# +
# t
# \begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# $$
# 
# $$
# Nul(S-\lambda I)=span
# \left\{
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0\\
# \end{bmatrix}
# ,
# \begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# \right\}
# \rightarrow
# basis(S-\lambda I)=
# \left\{
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0\\
# \end{bmatrix}
# ,
# \begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# \right\}
# $$

# In[23]:


(S+7*eye(4)).nullspace()


# $$
# \mathbf{v_1}
# =
# \mathbf{x_1}
# =
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# $$
# 
# $$
# \mathbf{v_2}
# =
# \mathbf{x_2}-\frac{\mathbf{x_2}\cdot\mathbf{v_1}}{\mathbf{v_1}\cdot\mathbf{v_1}}\mathbf{v_1}
# =
# \begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# -
# \frac{\begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# \cdot
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}}
# {\begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# \cdot
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}}
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# -
# \frac{3}{5}
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# 3\\
# -2\\
# 0\\
# 1\\
# \end{bmatrix}
# -
# \begin{bmatrix}
# 3\\
# -\frac{9}{5}\\
# \frac{3}{5}\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0\\
# -\frac{1}{5}\\
# -\frac{3}{5}\\
# 1
# \end{bmatrix}
# $$

# In[24]:


GramSchmidt((S+7*eye(4)).nullspace())


# $$
# \left\Vert
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# \right\Vert
# =
# \sqrt{(5)^2+(-3)^2+1^2+0^2}
# =
# \sqrt{25+9+1}
# =
# \sqrt{35}
# $$
# 
# $$
# \frac{
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}}{
# \left\Vert
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# \right\Vert}
# =
# \frac{1}{\sqrt{35}}
# \begin{bmatrix}
# 5\\
# -3\\
# 1\\
# 0
# \end{bmatrix}
# =
# \begin{bmatrix}
# \frac{5}{\sqrt{35}}\\
# -\frac{3}{\sqrt{35}}\\
# \frac{1}{\sqrt{35}}\\
# 0
# \end{bmatrix}
# $$
# 
# $$
# \left\Vert
# \begin{bmatrix}
# 0\\
# -\frac{1}{5}\\
# -\frac{3}{5}\\
# 1
# \end{bmatrix}
# \right\Vert
# =
# \sqrt{0^2+\left(-\frac{1}{5}\right)^2+\left(-\frac{3}{5}\right)^2+1^2}
# =
# \sqrt{0+\frac{1}{25}+\frac{9}{25}+1}
# =
# \sqrt{\frac{7}{5}}
# $$
# 
# $$
# \frac{
# \begin{bmatrix}
# 0\\
# -\frac{1}{5}\\
# -\frac{3}{5}\\
# 1
# \end{bmatrix}}{
# \left\Vert
# \begin{bmatrix}
# 0\\
# -\frac{1}{5}\\
# -\frac{3}{5}\\
# 1
# \end{bmatrix}
# \right\Vert}
# =
# \frac{1}{\sqrt{\frac{7}{5}}}
# \begin{bmatrix}
# 0\\
# -\frac{1}{5}\\
# -\frac{3}{5}\\
# 1
# \end{bmatrix}
# =
# \begin{bmatrix}
# 0\\
# -\frac{1}{5\sqrt{\frac{7}{5}}}\\
# -\frac{3}{5\sqrt{\frac{7}{5}}}\\
# \frac{1}{\sqrt{\frac{7}{5}}}
# \end{bmatrix}
# $$

# Therefore, an orthonormal basis for the eigenspace of $S$ associated with the eigenvalue $\lambda=-7$ is
# 
# $$
# \left\{
# \begin{bmatrix}
# \frac{5}{\sqrt{35}}\\
# -\frac{3}{\sqrt{35}}\\
# \frac{1}{\sqrt{35}}\\
# 0
# \end{bmatrix}
# ,
# \begin{bmatrix}
# 0\\
# -\frac{1}{5\sqrt{\frac{7}{5}}}\\
# -\frac{3}{5\sqrt{\frac{7}{5}}}\\
# \frac{1}{\sqrt{\frac{7}{5}}}
# \end{bmatrix}
# \right\}
# $$

# In[25]:


v1 = np.array([5, -3, 1, 0])
x2 = np.array([3, -2, 0, 1])
v2 = x2 - np.dot((np.dot(x2, v1)/np.dot(v1, v1)), v1)

v1u = v1/np.linalg.norm(v1)
v2u = v2/np.linalg.norm(v2)

print(v1)
print(v1u)
print(v2)
print(v2u)
print(np.dot(v1u, v1u))
print(np.dot(v2u, v2u))
print(np.isclose(np.dot(v1u, v2u), 0))


# $$
# Q^TQ
# =
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}} & -\frac{3}{\sqrt{14}} & \frac{1}{\sqrt{14}} & 0\\
# 0 & \frac{1}{2\sqrt{\frac{7}{2}}} & \frac{3}{2\sqrt{\frac{7}{2}}} & \frac{1}{\sqrt{\frac{7}{2}}}\\
# \frac{5}{\sqrt{35}} & -\frac{3}{\sqrt{35}} & \frac{1}{\sqrt{35}} & 0\\
# 0 & -\frac{1}{5\sqrt{\frac{7}{5}}} & -\frac{3}{5\sqrt{\frac{7}{5}}} & \frac{1}{\sqrt{\frac{7}{5}}}\\
# \end{bmatrix}
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}} & 0 & \frac{5}{\sqrt{35}} & 0\\
# -\frac{3}{\sqrt{14}} & \frac{1}{2\sqrt{\frac{7}{2}}} & -\frac{3}{\sqrt{35}} & -\frac{1}{5\sqrt{\frac{7}{5}}}\\
# \frac{1}{\sqrt{14}} & \frac{3}{2\sqrt{\frac{7}{2}}} & \frac{1}{\sqrt{35}} & -\frac{3}{5\sqrt{\frac{7}{5}}}\\
# 0 & \frac{1}{\sqrt{\frac{7}{2}}} & 0 & \frac{1}{\sqrt{\frac{7}{5}}}\\
# \end{bmatrix}
# $$

# $$
# \begin{align}
# \left(-\frac{2}{\sqrt{14}}\right)\left(-\frac{2}{\sqrt{14}}\right)+\left(-\frac{3}{\sqrt{14}}\right)\left(-\frac{3}{\sqrt{14}}\right)+\frac{1}{\sqrt{14}}\frac{1}{\sqrt{14}}+0 &= 1\\
# 0+\left(-\frac{3}{\sqrt{14}}\right)\frac{1}{2\sqrt{\frac{7}{2}}}+\frac{1}{\sqrt{14}}\frac{3}{2\sqrt{\frac{7}{2}}}+0 &= 0\\
# \left(-\frac{2}{\sqrt{14}}\right)\frac{5}{\sqrt{35}}+\left(-\frac{3}{\sqrt{14}}\right)\left(-\frac{3}{\sqrt{35}}\right)+\frac{1}{\sqrt{14}}\frac{1}{\sqrt{35}}+0 &= 0\\
# 0+\left(-\frac{3}{\sqrt{14}}\right)\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+\frac{1}{\sqrt{14}}\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+0 &= 0\\
# 0+\frac{1}{2\sqrt{\frac{7}{2}}}\left(-\frac{3}{\sqrt{14}}\right)+\frac{3}{2\sqrt{\frac{7}{2}}}\frac{1}{\sqrt{14}}+0 &= 0\\
# 0+\frac{1}{2\sqrt{\frac{7}{2}}}\frac{1}{2\sqrt{\frac{7}{2}}}+\frac{3}{2\sqrt{\frac{7}{2}}}\frac{3}{2\sqrt{\frac{7}{2}}}+\frac{1}{\sqrt{\frac{7}{2}}}\frac{1}{\sqrt{\frac{7}{2}}} &= 1\\
# 0+\frac{1}{2\sqrt{\frac{7}{2}}}\left(-\frac{3}{\sqrt{35}}\right)+\frac{3}{2\sqrt{\frac{7}{2}}}\frac{1}{\sqrt{35}}+0 &= 0\\
# 0+\frac{1}{2\sqrt{\frac{7}{2}}}\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+\frac{3}{2\sqrt{\frac{7}{2}}}\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+\frac{1}{\sqrt{\frac{7}{2}}}\frac{1}{\sqrt{\frac{7}{5}}} &= 0\\
# \end{align}
# $$

# $$
# \begin{align}
# \frac{5}{\sqrt{35}}\left(-\frac{2}{\sqrt{14}}\right)+\left(-\frac{3}{\sqrt{35}}\right)\left(-\frac{3}{\sqrt{14}}\right)+\frac{1}{\sqrt{35}}\frac{1}{\sqrt{14}}+0 &= 0\\
# 0+\left(-\frac{3}{\sqrt{35}}\right)\frac{1}{2\sqrt{\frac{7}{2}}}+\frac{1}{\sqrt{35}}\frac{3}{2\sqrt{\frac{7}{2}}}+0 &= 0\\
# \frac{5}{\sqrt{35}}\frac{5}{\sqrt{35}}+\left(-\frac{3}{\sqrt{35}}\right)\left(-\frac{3}{\sqrt{35}}\right)+\frac{1}{\sqrt{35}}\frac{1}{\sqrt{35}}+0 &= 1\\
# 0+\left(-\frac{3}{\sqrt{35}}\right)\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+\frac{1}{\sqrt{35}}\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+0 &= 0\\
# 0+\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)\left(-\frac{3}{\sqrt{14}}\right)+\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)\frac{1}{\sqrt{14}}+0 &= 0\\
# 0+\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)\frac{1}{2\sqrt{\frac{7}{2}}}+\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)\frac{3}{2\sqrt{\frac{7}{2}}}+\frac{1}{\sqrt{\frac{7}{5}}}\frac{1}{\sqrt{\frac{7}{2}}} &= 0\\
# 0+\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)\left(-\frac{3}{\sqrt{35}}\right)+\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)\frac{1}{\sqrt{35}}+0 &= 0\\
# 0+\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+\frac{1}{\sqrt{\frac{7}52}}\frac{1}{\sqrt{\frac{7}{5}}} &= 1\\
# \end{align}
# $$

# $$
# =
# \begin{bmatrix}
# 1 & 0 & 0 & 0\\
# 0 & 1 & 0 & 0\\
# 0 & 0 & 1 & 0\\
# 0 & 0 & 0 & 1\\
# \end{bmatrix}
# $$

# $$
# Q^TSQ
# =
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}} & -\frac{3}{\sqrt{14}} & \frac{1}{\sqrt{14}} & 0\\
# 0 & \frac{1}{2\sqrt{\frac{7}{2}}} & \frac{3}{2\sqrt{\frac{7}{2}}} & \frac{1}{\sqrt{\frac{7}{2}}}\\
# \frac{5}{\sqrt{35}} & -\frac{3}{\sqrt{35}} & \frac{1}{\sqrt{35}} & 0\\
# 0 & -\frac{1}{5\sqrt{\frac{7}{5}}} & -\frac{3}{5\sqrt{\frac{7}{5}}} & \frac{1}{\sqrt{\frac{7}{5}}}\\
# \end{bmatrix}
# \begin{bmatrix}
# -3 & 6 & -2 & 0\\
# 6 & 3 & 0 & 2\\
# -2 & 0 & 3 & 6\\
# 0 & 2 & 6 & -3\\
# \end{bmatrix}
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}} & 0 & \frac{5}{\sqrt{35}} & 0\\
# -\frac{3}{\sqrt{14}} & \frac{1}{2\sqrt{\frac{7}{2}}} & -\frac{3}{\sqrt{35}} & -\frac{1}{5\sqrt{\frac{7}{5}}}\\
# \frac{1}{\sqrt{14}} & \frac{3}{2\sqrt{\frac{7}{2}}} & \frac{1}{\sqrt{35}} & -\frac{3}{5\sqrt{\frac{7}{5}}}\\
# 0 & \frac{1}{\sqrt{\frac{7}{2}}} & 0 & \frac{1}{\sqrt{\frac{7}{5}}}\\
# \end{bmatrix}
# $$

# $$
# \begin{align}
# (-3)\left(- \frac{2}{\sqrt{14}}\right)+6\left(-\frac{3}{\sqrt{14}}\right)+(-2)\frac{1}{\sqrt{14}}+0 &= \left(-\frac{14}{\sqrt{14}}\right)\\
# 6\left(-\frac{2}{\sqrt{14}}\right)+3\left(-\frac{3}{\sqrt{14}}\right)+0+0 &= \left(-\frac{21}{\sqrt{14}}\right)\\
# (-2)\left(-\frac{2}{\sqrt{14}}\right)+0+3\frac{1}{\sqrt{14}}+0 &= \frac{7}{\sqrt{14}}\\
# 0+2\left(-\frac{3}{\sqrt{14}}\right)+6\frac{1}{\sqrt{14}}+0 &= 0\\
# 0+6\frac{1}{2\sqrt{\frac{7}{2}}}+(-2)\frac{3}{2\sqrt{\frac{7}{2}}}+0 &= 0\\
# 0+3\frac{1}{2\sqrt{\frac{7}{2}}}+0+2\frac{1}{\sqrt{\frac{7}{2}}} &= \frac{7}{2\sqrt{\frac{7}{2}}}\\
# 0+0+3\frac{3}{2\sqrt{\frac{7}{2}}}+6\frac{1}{\sqrt{\frac{7}{2}}} &= \frac{21}{2\sqrt{\frac{7}{2}}}\\
# 0+2\frac{1}{2\sqrt{\frac{7}{2}}}+6\frac{3}{2\sqrt{\frac{7}{2}}}+(-3)\frac{1}{\sqrt{\frac{7}{2}}} &= \frac{7}{\sqrt{\frac{7}{2}}}\\
# (-3)\frac{5}{\sqrt{35}}+6\left(-\frac{3}{\sqrt{35}}\right)+(-2)\frac{1}{\sqrt{35}}+0 &= \left(-\frac{35}{\sqrt{35}}\right)\\
# 6\frac{5}{\sqrt{35}}+3\left(-\frac{3}{\sqrt{35}}\right)+0+0 &= \frac{21}{\sqrt{35}}\\
# (-2)\frac{5}{\sqrt{35}}+0+3\frac{1}{\sqrt{35}}+0 &= \left(-\frac{7}{\sqrt{35}}\right)\\
# 0+2\left(-\frac{3}{\sqrt{35}}\right)+6\frac{1}{\sqrt{35}}+0 &= 0\\
# 0+6\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+(-2)\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+0 &= 0\\
# 0+3\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+0+2\frac{1}{\sqrt{\frac{7}{5}}} &= \frac{7}{5\sqrt{\frac{7}{5}}}\\
# 0+0+3\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+6\frac{1}{\sqrt{\frac{7}{5}}} &= \frac{21}{5\sqrt{\frac{7}{5}}}\\
# 0+2\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+6\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+(-3)\frac{1}{\sqrt{\frac{7}{5}}} &= \left(-\frac{7}{\sqrt{\frac{7}{5}}}\right)\\
# \end{align}
# $$

# $$
# =
# \begin{bmatrix}
# -\frac{14}{\sqrt{14}} & -\frac{21}{\sqrt{14}} & \frac{7}{\sqrt{14}} & 0\\
# 0 & \frac{7}{2\sqrt{\frac{7}{2}}} & \frac{21}{2\sqrt{\frac{7}{2}}} & \frac{7}{\sqrt{\frac{7}{2}}}\\
# -\frac{35}{\sqrt{35}} & \frac{21}{\sqrt{35}} & -\frac{7}{\sqrt{35}} & 0\\
# 0 & \frac{7}{5\sqrt{\frac{7}{5}}} & \frac{21}{5\sqrt{\frac{7}{5}}} & -\frac{7}{\sqrt{\frac{7}{5}}}\\
# \end{bmatrix}
# \begin{bmatrix}
# -\frac{2}{\sqrt{14}} & 0 & \frac{5}{\sqrt{35}} & 0\\
# -\frac{3}{\sqrt{14}} & \frac{1}{2\sqrt{\frac{7}{2}}} & -\frac{3}{\sqrt{35}} & -\frac{1}{5\sqrt{\frac{7}{5}}}\\
# \frac{1}{\sqrt{14}} & \frac{3}{2\sqrt{\frac{7}{2}}} & \frac{1}{\sqrt{35}} & -\frac{3}{5\sqrt{\frac{7}{5}}}\\
# 0 & \frac{1}{\sqrt{\frac{7}{2}}} & 0 & \frac{1}{\sqrt{\frac{7}{5}}}\\
# \end{bmatrix}
# $$

# $$
# \begin{align}
# \left(-\frac{14}{\sqrt{14}}\right)\left(-\frac{2}{\sqrt{14}}\right)+\left(-\frac{21}{\sqrt{14}}\right)\left(-\frac{3}{\sqrt{14}}\right)+\frac{7}{\sqrt{14}}\frac{1}{\sqrt{14}}+0 &= 7\\
# 0+\left(-\frac{21}{\sqrt{14}}\right)\frac{1}{2\sqrt{\frac{7}{2}}}+\frac{7}{\sqrt{14}}\frac{3}{2\sqrt{\frac{7}{2}}}+0 &= 0\\
# \left(-\frac{14}{\sqrt{14}}\right)\frac{5}{\sqrt{35}}+\left(-\frac{21}{\sqrt{14}}\right)\left(-\frac{3}{\sqrt{35}}\right)+\frac{7}{\sqrt{14}}\frac{1}{\sqrt{35}}+0 &= 0\\
# 0+\left(-\frac{21}{\sqrt{14}}\right)\left(-\frac{1}{5\sqrt{\frac{7}{5}}}\right)+\frac{7}{\sqrt{14}}\left(-\frac{3}{5\sqrt{\frac{7}{5}}}\right)+0 &= 0\\
# 0+\frac{7}{2\sqrt{\frac{7}{2}}}+\frac{21}{2\sqrt{\frac{7}{2}}}+0 &= 0\\
# 0+\frac{7}{2\sqrt{\frac{7}{2}}}+\frac{21}{2\sqrt{\frac{7}{2}}}+\frac{7}{\sqrt{\frac{7}{2}}} &= 7\\
# 0+\frac{7}{2\sqrt{\frac{7}{2}}}+\frac{21}{2\sqrt{\frac{7}{2}}}+0 &= 0\\
# 0+\frac{7}{2\sqrt{\frac{7}{2}}}+\frac{21}{2\sqrt{\frac{7}{2}}}+\frac{7}{\sqrt{\frac{7}{2}}} &= 0\\
# ... &= 0\\
# ... &= 0\\
# ... &= -7\\
# ... &= 0\\
# ... &= 0\\
# ... &= 0\\
# ... &= 0\\
# ... &= -7\\
# \end{align}
# $$

# $$
# =
# \begin{bmatrix}
# 7 & 0 & 0 & 0\\
# 0 & 7 & 0 & 0\\
# 0 & 0 & -7 & 0\\
# 0 & 0 & 0 & -7\\
# \end{bmatrix}
# $$

# In[26]:


Q = Matrix(4, 4, [
    -2/np.sqrt(14), 0, 5/np.sqrt(35), 0,
    -3/np.sqrt(14), 1/(2*np.sqrt(7/2)), -3/np.sqrt(35), -1/(5*np.sqrt(7/5)),
    1/np.sqrt(14), 3/(2*np.sqrt(7/2)), 1/np.sqrt(35), -3/(5*np.sqrt(7/5)),
    0, 1/np.sqrt(7/2), 0, 1/np.sqrt(7/5)
])
Q*Q.transpose()


# In[27]:


Sn = np.array([-3, 6, -2, 0, 6, 3, 0, 2, -2, 0, 3, 6, 0, 2, 6, -3]).reshape(4, 4)
Qn = np.array([-2/np.sqrt(14), 0, 5/np.sqrt(35), 0,
              -3/np.sqrt(14), 1/(2*np.sqrt(7/2)), -3/np.sqrt(35), -1/(5*np.sqrt(7/5)),
              1/np.sqrt(14), 3/(2*np.sqrt(7/2)), 1/np.sqrt(35), -3/(5*np.sqrt(7/5)),
              0, 1/np.sqrt(7/2), 0, 1/np.sqrt(7/5),
             ]).reshape(4, 4)
np.round(np.dot(Qn, Qn.transpose()))


# In[28]:


np.dot(Qn.T, Sn)


# In[29]:


np.round(np.dot(np.dot(Qn.T, Sn), Qn), 0)


# ---

# In[30]:


S.eigenvects()


# In[31]:


P, D = S.diagonalize()


# In[32]:


P


# In[33]:


D


# ---

# In[34]:


l = symbols('l')
M = Matrix(4, 4, [-3-l, 6, -2, 0, 6, 3-l, 0, 2, -2, 0, 3-l, 6, 0, 2, 6, -3-l])
M


# In[35]:


M.det()


# In[36]:


np.roots(np.array([1, 0, -98, 0, 2401]))


# In[37]:


M8_p7 = Matrix(4, 5, [-3-7, 6, -2, 0, 0, 6, 3-7, 0, 2, 0, -2, 0, 3-7, 6, 0, 0, 2, 6, -3-7, 0])
M8_p7


# In[38]:


M8_p7.rref()


# In[39]:


M8_n7 = Matrix(4, 5, [-3+7, 6, -2, 0, 0, 6, 3+7, 0, 2, 0, -2, 0, 3+7, 6, 0, 0, 2, 6, -3+7, 0])
M8_n7


# In[40]:


M8_n7.rref()


# ---
