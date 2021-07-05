#!/usr/bin/env python
# coding: utf-8

# # Algorithmic Number Theory

# ## Algorithmic Number Theory
# 
# An algorithm's running time is measured as a function of the length(s) of its input(s).<br>
# Integer inputs are always assumed to be represented in binary.<br>
# An algorithm's running time taking as input an integer $N$ is therefore measured in terms of $\vert\vert N \vert\vert = \lfloor\log N \rfloor + 1$, the _length of the binary representation of_ $N$.<br>
# 
# An integer $a$ provided as input is written using exactly $\vert\vert a \vert\vert$ bits; i.e., the high-order bit is 1.<br>
# 
# ### Integer Arithmetic
# Given integers $a$ and $b$, it is possible to perform the following operations in time polynomial in $\vert\vert a \vert\vert$ and $\vert\vert b \vert\vert$:
# 
# #### Addition
# Compute the sum $a + b$
# 
# #### Subtraction
# Compute the difference $a - b$
# 
# #### Multiplication
# Compute the product $ab$
# 
# #### Division with Remainder
# Compute the positive integers $q$ and $r \lt b$ s.t. $a = qb + r$
# 
# #### Euclid's Algorithm
# Compute $\gcd(a, b)$
# 
# #### Extended Euclid's Algorithm
# Compute $x, y$, where $xa + yb = \gcd(a, b)$
# 
# ### Modular Arithmetic
# Given integers $N \gt 1$, $a$, and $b$, it is possible to perform the following operations in time polynomial in $\vert\vert a \vert\vert$, $\vert\vert b \vert\vert$, and $\vert\vert N \vert\vert$:
# 
# #### Modular Reduction
# Compute the modular reduction $[a \mod N]$
# 
# #### Modular Addition
# Compute the sum $[(a + b) \mod N]$
# 
# #### Modular Subtraction
# Compute the difference $[(a - b) \mod N]$
# 
# #### Modular Multiplication
# Compute the product $[(ab) \mod N]$
# 
# #### Modular Inversion
# Determine whether $a$ is invertible modulo $N$
# 
# #### Montgomery Multiplication
# Compute the multiplicative inverse $[a^{-1} \mod N]$, assuming $a$ is invertible modulo $N$
# 
# #### Exponentiation Modulo N
# Compute the exponentiation $[a^b \mod N]$
# 
# #### Group Exponentiation
# Let $\mathbb{G}$ be a group, written multiplicatively.<br>
# Let $g$ be an element of the group.<br>
# Let $b$ be a non negative integer.<br>
# Then $g^b$ can be computed using $\text{poly}(\vert\vert b \vert\vert)$ group operations.<br>
# 
# #### Choosing a uniform element of $\mathbb{Z}_N$ or $\mathbb{Z}_N^*$
# There exists a randomized algorithm with the following properties: on input $N$
# * The algorithm runs in time polynomial in $\vert\vert N \vert\vert$
# * The algorithm outputs $\text{fail}$ with probability negligible in $\vert\vert N \vert\vert$
# * Conditioned on not outputting $\text{fail}$, the algorithm outputs a uniformly distributed element of $\mathbb{Z}_N$
# 
# An algorithm with analogous properties exists for $\mathbb{Z}_N^*$ as well.<br>
# 
# #### Choosing a uniform element from a finite group
# 
# #### Testing and Finding Generators
# Let $\mathbb{G}$ be a cyclic group of order $q$.<br>
# Assume that the group operation and selection of a uniform group element can be carried out in unit time.<br>
# 1. There is an algorithm that on input $q$, the prime factorization of $q$, and an element $g \in \mathbb{G}$, runs in $\text{poly}(\vert\vert q \vert\vert)$ time and decides whether $g$ is a generator of $\mathbb{G}$.
# 2. There is a randomzied algorithm that on input $q$ and the prime factorization of $q$, runs in $\text{poly}(\vert\vert q \vert\vert)$ time and outputs a generator of $\mathbb{G}$ except with probability negligible in $\vert\vert q \vert\vert$. Conditioned on the output being a generator, it is uniformly distributed among the generators of $\mathbb{G}$.

# ---
