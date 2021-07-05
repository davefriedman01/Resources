#!/usr/bin/env python
# coding: utf-8

# # Complex Numbers

# ---

# A complex number is an ordered pair $(a, b)$, where $a, b \in \mathbb{R}$. This is written $a + bi$ where $i \equiv \sqrt{-1}$ (Leonhard Euler, 1777) s.t. $0 + 1i = i$.<br>
# The set of all complex numbers is denoted $\mathbb{C} = \{a + bi : a, b \in \mathbb{R}\}$.<br>
# 
# $i \equiv \sqrt{-1}$<br>
# $i^2 = \sqrt{-1}\sqrt{-1} = -1$<br>
# $i^3 = ii^2 = -i$<br>
# $i^4 = ii^3 = -ii = -i^2 = 1$<br>
# 
# #### Real Numbers
# $\mathbb{R} \subset \mathbb{C}$<br>
# $a + 0i = a$ where $a \in \mathbb{R}$
# 
# #### Imaginary Numbers
# $\mathbb{I} \subset \mathbb{C}$<br>
# $0 + bi = bi$ where $b \in \mathbb{R}$
# 
# #### Complex Addition
# $(a + bi) + (c + di) = (a + c) + (b + d)i$ where $a, b, c, d \in \mathbb{R}$<br>
# 
# Derivation<br>
# $
# (a + bi) + (c + di)
# =
# a + c + bi + di
# =
# (a + c) + (b + d)i
# $
# 
# #### Complex Multiplication
# $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$ where $a, b, c, d \in \mathbb{R}$<br>
# 
# Derivation<br>
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
# 
# #### Commutativity
# $\alpha + \beta = \beta + \alpha$<br>
# $\alpha\beta = \beta\alpha$<br>
# $\forall \alpha, \beta \in \mathbb{C}$<br>
# 
# Proof of Multiplicative Commutativity<br>
# Let $\alpha = a + bi$ and $\beta = c + di$ where $a, b, c, d \in \mathbb{R}$.<br>
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
# 
# #### Associativity
# $(\alpha + \beta) + \lambda = \alpha + (\beta + \lambda)$<br>
# $(\alpha\beta)\lambda = \alpha(\beta\lambda)$<br>
# $\forall \alpha, \beta, \lambda \in \mathbb{C}$<br>
# 
# #### Existence of Identity Element
# $\lambda + 0 = \lambda$<br>
# $\lambda 1 = \lambda$<br>
# $\forall \lambda \in \mathbb{C}$<br>
# 
# #### Existence of Inverse Elements
# $\forall \alpha \in \mathbb{C}$, $\exists \beta \in \mathbb{C}$ s.t. $\alpha + \beta = 0$<br>
# The additive inverse of an element $\alpha$ is denoted $-\alpha$.<br>
# $\forall \alpha \in \mathbb{C}$ with $\alpha \neq 0$, $\exists \beta \in \mathbb{C}$ s.t. $\alpha\beta = 1$<br>
# The multiplicative inverse of an element $\alpha \neq 0$ is denoted $\alpha^{-1}$.<br>
# 
# #### Distributivity
# $\lambda(\alpha + \beta) = \lambda\alpha + \lambda\beta$<br>
# $\forall \lambda, \alpha, \beta \in \mathbb{C}$<br>
# 
# #### Complex Substraction
# $\beta - \alpha \equiv \beta + (-\alpha)$<br>
# 
# #### Complex Division
# $\frac{\beta}{\alpha} \equiv \beta\alpha^{-1}$<br>

# ---
