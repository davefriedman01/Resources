#!/usr/bin/env python
# coding: utf-8

# # Complex Numbers

# ---

# ## What is a complex number?

# <span style="color: blue">**DEFINITION**</span><br>
# A complex number is an ordered pair $(a, b)$ where $a, b \in \mathbb{R}$.<br>
# A complex number may take the form $z = a + bi$ where $i$ is defined in the following way.<br>
# $i \overset{\text{def}}= \sqrt{-1}$<br>
# $i^2 = \sqrt{-1}\sqrt{-1} = -1$<br>
# $i^3 = ii^2 = -i$<br>
# $i^4 = ii^3 = -ii = -i^2 = 1 = i^0$<br>

# #### The set of complex numbers
# 
# $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$

# #### The real part of a complex number
# 
# Let $z = a + bi$ where $a, b \in \mathbb{R}$ be a complex number.<br>
# The real part of $z$, denoted Re $z$, is defined to be $a$.<br>
# $a + 0i = a$ where $a, 0 \in \mathbb{R}$<br>

# #### The imaginary part of a complex number
# 
# Let $z = a + bi$ where $a, b \in \mathbb{R}$ be a complex number.<br>
# The imaginary part of $z$, denoted Im $z$, is defined to be $b$.<br>
# $0 + bi = bi$ where $b, 0 \in \mathbb{R}$<br>

# ---

# ## Properties of complex numbers

# #### Commutativity
# $\alpha + \beta = \beta + \alpha$<br>
# $\alpha\beta = \beta\alpha$<br>
# $\forall \alpha, \beta \in \mathbb{C}$<br>
# 
# Proof of Multiplicative Commutativity<br>
# Let $\alpha = a + bi$ and $\beta = c + di$ where $a, b, c, d \in \mathbb{R}$.<br>
# 
# $
# \alpha\beta
# =
# (a + bi)(c + di)
# =
# ac + adi + bci + bdi^2
# =
# (c + di)a + (c + di)bi
# =
# (c + di)(a + bi)
# =
# \beta\alpha
# $

# #### Associativity
# $(\alpha + \beta) + \lambda = \alpha + (\beta + \lambda)$<br>
# $(\alpha\beta)\lambda = \alpha(\beta\lambda)$<br>
# $\forall \alpha, \beta, \lambda \in \mathbb{C}$<br>

# #### Existence of Identity Element
# $\lambda + 0 = \lambda$<br>
# $\lambda 1 = \lambda$<br>
# $\forall \lambda \in \mathbb{C}$<br>

# #### Existence of Inverse Elements
# $\forall \alpha \in \mathbb{C}$, $\exists \beta \in \mathbb{C}$ s.t. $\alpha + \beta = 0$<br>
# The additive inverse of an element $\alpha$ is denoted $-\alpha$.<br>
# $\forall \alpha \in \mathbb{C}$ with $\alpha \neq 0$, $\exists \beta \in \mathbb{C}$ s.t. $\alpha\beta = 1$<br>
# The multiplicative inverse of an element $\alpha \neq 0$ is denoted $\alpha^{-1}$.<br>

# #### Distributivity
# $\lambda(\alpha + \beta) = \lambda\alpha + \lambda\beta$<br>
# $\forall \lambda, \alpha, \beta \in \mathbb{C}$<br>

# ---

# ## Operations on complex numbers

# #### Complex Addition
# 
# $(a + bi) + (c + di) = (a + c) + (b + d)i$ where $a, b, c, d \in \mathbb{R}$<br>
# 
# Derivation<br>
# 
# $
# (a + bi) + (c + di)
# =
# a + c + bi + di
# =
# (a + c) + (b + d)i
# $

# #### Complex Multiplication
# $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$ where $a, b, c, d \in \mathbb{R}$<br>
# 
# Derivation<br>
# 
# $
# (a + bi)(c + di)
# =
# ac + adi + bci + bdi^2
# =
# ac + bdi^2 + adi + bci
# =
# ac - bd + adi + bci
# =
# (ac - bd) + (ad + bc)i
# $

# #### Complex Substraction
# $\beta - \alpha \equiv \beta + (-\alpha)$<br>

# #### Complex Division
# $\frac{\beta}{\alpha} \equiv \beta\alpha^{-1}$<br>

# ---

# ### Complex Conjugate of a complex number
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $z \in \mathbb{C}$.<br>
# The complex conjugate of $z$ is $\bar{z} \overset{\text{def}}= \,(\text{Re}\, z) - \,(\text{Im}\, z) i$.<br>
# If $z = a + bi$, then $\bar{z} = a - bi$.<br>

# ### Absolute Value of a complex number
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $z \in \mathbb{C}$.<br>
# The absolute value of $z$ is $|z| \overset{\text{def}}= \sqrt{\,(\text{Re}\, z)^2 + \,(\text{Im}\, z)^2}$.<br>
# If $z = a + bi$, then $|z| = \sqrt{a^2 + b^2}$.<br>

# __Claim__<br>
# $\forall z \in \mathbb{C}, |z| \ge 0$. (The absolute value of any complex number is nonnegative.)<br>
# 
# __Proof__<br>
# 
# This follows from the fact that the sum of squares of a collection of real numbers is nonnegative.<br>
# 
# $\blacksquare$<br>

# __Claim__<br>
# If $z \in \mathbb{R}$, then $z = \bar{z}$. (The complex conjugate of a real number is itself.)<br>
# 
# __Proof__<br>
# 
# $z = a + 0i = a = a - 0i = \bar{z}$<br>
# 
# $\blacksquare$<br>

# ### Operations on a complex number and its conjugate

# #### Sum of $z$ and $\bar{z}$
# 
# Let $z \in \mathbb{C}$.<br>
# $z + \bar{z} = 2a$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# z + \bar{z}
# &= (a + bi) + (a - bi) \\
# &= a + bi + a - bi \\
# &= 2a + bi - bi \\
# &= 2a
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Difference of $z$ and $\bar{z}$
# 
# Let $z \in \mathbb{C}$.<br>
# $z - \bar{z} = 2bi$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# z - \bar{z}
# &= (a + bi) - (a - bi) \\
# &= a + bi - a + bi \\
# &= 2bi + a - a \\
# &= 2bi
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Product of $z$ and $\bar{z}$
# 
# Let $z \in \mathbb{C}$.<br>
# $z \bar{z} = |z|^2$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# z \bar{z}
# &= (a + bi) (a - bi) \\
# &= a^2 - abi + abi - (bi)^2 \\
# &= a^2 - b^2 i^2 \\
# &= a^2 + b^2 \\
# &= (\sqrt{a^2 + b^2})^2 \\
# &= |z|^2
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# ### Properties of the complex conjugate and the absolute value of a complex number

# #### Additivity of the complex conjugate
# 
# Let $w, z \in \mathbb{C}$.<br>
# $\overline{w + z} = \bar{w} + \bar{z}$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# w + z
# &= (a + bi) + (c + di) \\
# &= (a + c) + (b + d)i \\
# \overline{w + z}
# &= (a + c) - (b + d)i \\
# &= a + c - bi - di \\
# &= (a - bi) + (c - di) \\
# &= \bar{w} + \bar{z} \\
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Multiplicativity of the complex conjugate
# 
# Let $w, z \in \mathbb{C}$.<br>
# $\overline{w z} = \bar{w} \bar{z}$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# w z
# &= (a + bi) (c + di) \\
# &= ac + adi + bci + bdi^2 \\
# &= (ac - bd) + (ad + bc)i \\
# \overline{w z}
# &= (ac - bd) - (ad + bc)i \\
# &= ac - bd - adi - bci \\
# &= ac - adi - bci + bdi^2 \\
# &= (a - bi) (c - di) \\
# &= \bar{w} \bar{z} \\
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Conjugate of the conjugate
# 
# Let $z \in \mathbb{C}$.<br>
# $\bar{\bar{z}} = z$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# \bar{z}
# &= a - bi \\
# &= (a) + (-b)i \\
# \bar{\bar{z}}
# &= (a) - (-b)i \\
# &= a + bi \\
# &= z \\
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Boundedness
# 
# Let $z \in \mathbb{C}$.<br>
# $|a| \le |z|$ and $|b| \le |z|$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# |a|
# &= \sqrt{a^2} \\
# &\le \sqrt{a^2 + b^2} \\
# &= |z|
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Absolute value of the complex conjugate
# 
# Let $z \in \mathbb{Z}$.<br>
# $|\bar{z}| = |z|$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# \bar{z}
# &= a - bi \\
# &= (a) + (-b)i \\
# |\bar{z}|
# &= \sqrt{(a)^2 + (-b)^2} \\
# &= \sqrt{a^2 + b^2} \\
# &= |z| \\
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Multiplicativity of the absolute value
# 
# Let $w, z \in \mathbb{Z}$.<br>
# $|w||z| = |wz|$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# wz
# &= (a + bi) (c + di) \\
# &= ac + adi + bci + bdi^2 \\
# &= (ac - bd) + (ad + bc)i \\
# |wz|
# &= \sqrt{(ac - bd)^2 + (ad + bc)^2} \\
# &= \sqrt{(ac)^2 - 2abcd + (bd)^2 + (ad)^2 + 2abcd + (bc)^2} \\
# &= \sqrt{(ac)^2 + (bd)^2 + (ad)^2 + (bc)^2} \\
# &= \sqrt{(ac)^2 + (ad)^2 + (bd)^2 + (bc)^2} \\
# &= \sqrt{a^2(c^2 + d^2) + b^2(c^2 + d^2)} \\
# &= \sqrt{(a^2 + b^2)(c^2 + d^2)} \\
# &= \sqrt{a^2 + b^2} \sqrt{c^2 + d^2} \\
# &= |w||z| \\
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# #### Triangle Inequality
# 
# Let $w, z \in \mathbb{Z}$.<br>
# $|w + z| \le |w| + |z|$<br>
# 
# __Proof__<br>
# 
# $
# \begin{align}
# |w + z|^2
# &= (w + z)(\bar{w} + \bar{z}) \\
# &= w \bar{w} + z \bar{z} + w \bar{z} + z \bar{w} \\
# &= |w|^2 + |z|^2 + w \bar{z} + \overline{w \bar{z}} \\
# &= |w|^2 + |z|^2 + w \bar{z} + 2 \,\text{Re}\, (w \bar{z}) \\
# &\le |w|^2 + |z|^2 + w \bar{z} + 2 |w \bar{z}| \\
# &= |w|^2 + |z|^2 + w \bar{z} + 2 |w| |z| \\
# &= (|w| + |z|)^2 \\
# |w + z|
# &\le |w| + |z| \\
# \end{align}
# $<br>
# 
# $\blacksquare$<br>

# ---
