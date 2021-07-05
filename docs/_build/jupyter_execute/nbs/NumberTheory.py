#!/usr/bin/env python
# coding: utf-8

# # Number Theory

# #### Divisibility
# $\forall a, b \in \mathbb{Z}$, $a$ divides $b$, $a \mid b$, if $\exists c \in \mathbb{Z}$ s.t. $ac = b$<br>
# $a \nmid b$ when $a$ does not divide $b$<br>
# if $a \mid b$ and $a \mid c$ then $a \mid (xb + yc)$ for any $x, y \in \mathbb{Z}$<br>
# 
# #### Divisor, Factor
# If $a \mid b$ and $a$ is positive, then $a$ is a _divisor_ of $b$.<br>
# If, in addition, $a \notin \{1, b\}$, then $a$ is a _nontrivial divisor_ or _factor_ of $b$.<br>
# 
# #### Prime Number
# A positive integer $p > 1$ is _prime_ if it has no factors (i.e., it has only two divisors: 1 and itself).<br>
# 
# #### Composite Number
# A positive integer greater than 1 that is not prime is _composite_.<br>
# By convention, the number 1 is neither prime nor composite.<br>
# 
# #### Fundamental Theorem of Arithmetic (Unique Factorization)
# Every integer greater than 1 can be expressed uniquely, up to ordering, as a product of primes. That is, any positive integer $N > 1$ can be written as $N = \prod_i p_i^{e_i}$, where the $\{p_i\}$ are distinct primes and $e_i \ge 1$ for all $i$; further, the $\{p_i\}$ and $\{e_i\}$ are uniquely determined up to ordering.<br>
# 
# #### Division with Remainder
# Let $a$ be an integer and let $b$ be a positive integer.<br>
# Then there exist unique integers $q, r$ for which $a = qb + r$ and $0 \le r \lt b$.<br>
# Further, given integers $a$ and $b$ it is possible to compute $q$ and $r$ in polynomial time.<br>
# 
# #### GCD Greatest Common Divisor gcd$(a, b)$
# The GCD of two integers $a$ and $b$, gcd$(a, b)$, is the largest integer $c$ s.t. $c \mid a$ and $c \mid b$.<br>
# gcd$(0, 0)$ is undefined<br>
# gcd$(a, b) =$ gcd($\vert a \vert$, $\vert b \vert$)<br>
# gcd$(b, 0) =$ gcd$(0, b) = b$<br>
# if $p$ is prime, then gcd$(a, p)$ is either equal to 1 or $p$<br>
# if gcd$(a, b) = 1$, then $a$ and $b$ are _relatively prime_<br>
# 
# #### Proposition
# Let $a, b$ be positive integers.<br>
# Then there exist integers $x, y$ s.t. $xa + yb = \gcd(a, b)$.<br>
# Further, $\gcd(a, b)$ is the smallest positive integer that can be expressed in this way.<br>
# ##### Proof
# Let $I \overset{\text{def}}{=} \{\hat{x}a + \hat{y}b \mid \hat{x}, \hat{y} \in \mathbb{Z}\}$.<br>
# Note that $a, b \in I$ and so $I$ contains some positive integers.<br>
# Let $d$ be the smallest positive integer in $I$.<br>
# $d$ can be written as $d = xa + yb$ for some $x, y \in \mathbb{Z}$ because $d \in I$.<br>
# Let's show that $d = \gcd(a, b)$ by proving that
# * $d \mid a$
# * $d \mid b$
# * $d$ is the largest integer with this property (in fact, $d$ divides every element in $I$)
# 
# Let $c \in I = x'a + y'b$ for some $x', y' \in \mathbb{Z}$.<br>
# $c = qd + r$ with $q, r$ integers and $0 \le r \lt d$.<br>
# $r = c - qd = x'a + y'b - q(xa + yb) = (x' - qx)a + (y' - qy)b \in I$.<br>
# if $r \ne 0$, this contradicts our choice of d as the smallest positive integer in $I$ because $r \lt d$<br>
# therefore, $r = 0$, $d \mid c$, and $d$ divides every element of $I$<br>
# $a, b \in I$, so $d \mid a$ and $d \mid b$, so $d$ is a common divisor of $a$ and $b$<br>
# Let there be an integer $d' \gt d$ s.t. $d' \mid a$ and $d' \mid b$.<br>
# Then $d' \mid xa + by$. Since the latter is equal to $d$, this means $d' \mid d$.<br>
# Contradiction, if $d'$ is larger than $d$.<br>
# Therefore, $d$ is the largest integer dividing both $a$ and $b$, and thus $d = \gcd(a, b)$<br>
# 
# #### Proposition
# If $c \mid ab$ and $\gcd(a, c) = 1$, then $c \mid b$.<br>
# Thus, if $p$ is prime and $p \mid ab$, then either $p \mid a$ or $p \mid b$.<br>
# 
# ##### Proof
# Since $c \mid ab$, $\gamma c = ab$ for some integer $\gamma$.<br>
# If $\gcd(a, c) = 1$, then there exist integers $x, y$ s.t. $1 = xa + yc$.<br>
# $b = xab + ycb = x \gamma c + ycb = c(x \gamma + yb)$<br>
# Since $x \gamma + yb$ is an integer, $c \mid b$.<br>
# The second part of the proposition follows from the fact that if $p \not\mid a$, then $\gcd(a, p) = 1$.<br>
# 
# #### Proposition
# If $a \mid N, b \mid N$, and $\gcd(a, b) = 1$, then $ab \mid N$.<br>
# 
# ##### Proof
# $ac = N$, $bd = N$, and $1 = xa + yb$, where $c, d, x, y \in \mathbb{Z}$<br>
# $N = xaN + ybN = xabd + ybac = ab(xd + yc)$<br>
# Thus, $ab \mid N$.<br>

# ---

# #### Modular Reduction and the Residue
# "What is the remainder of a divided by b?"<br>
# "What is the residue of a reduced modulo b?"<br>
# "What is a mod b?"<br>
# The residue $r$ of an integer $a$ reduced modulo $n$, written $r = a \mod n$ is that value of $r$ s.t. $0 \le r \lt n$ and $a = kn + r$ for some integer $k$, where $a$ can be negative and $n$ is greater than 1<br>
# 
# All integers that are mutually congruent modulo $n$ form a congruence class modulo $n$<br>
# Each integer belongs to one of $n$ congruence classes.<br>
# One integer from each congruence class is chosen as the representative of the congruence class, called the residue.<br>
# By convention, define the residues to be the first $n$ nonnegative integers.<br>
# Modular Reduction is defined as reducing an integer to the residue of its congruence class.<br>
# 
# #### Congruence mod m
# Let $m$ be a fixed positive integer.<br>
# Two integers $a$ and $b$ are _congruent mod $m$_
# * if $a - b$ is divisible by $m$ (i.e., if $a = km + b$ for some integer $k$)
# * iff they have the same principal remainders on division by $m$
# 
# $$a \equiv b \,(\text{mod}\, m)$$
# 
# $a \not\equiv b \,(\text{mod}\, m)$ when two integers $a$ and $b$ are _not_ congruent mod $m$<br>
# 
# #### Theorem
# Let $a \equiv a' \,\text{mod}\, m$ and $b \equiv b' \,\text{mod}\, m$.
# * (i) $a + b \equiv a' + b' \,(\text{mod}\, m)$
# * (ii) $ab \equiv a'b' \,(\text{mod}\, m)$
# 
# If $a \equiv a' \,\text{mod}\, m$, then for all positive integers $n$, $a^n \equiv (a')^n \,(\text{mod}\, m)$.<br>
# 
# ##### Proof
# $a = a' + km$ and $b = b' + lm$ for some integers $k$ and $l$<br>
# (i) $a + b = a' + b' + (k + l)m \therefore \frac{a + b - (a' + b')}{m} = k + l$<br>
# (ii) $ab = a'b' + (kb' + a'l + klm)m \therefore \frac{ab - a'b'}{m} = kb' + a'l + klm$<br>
# 
# #### Ring of Integers mod m $Z_m = \{0, 1, ..., m - 1\}, m \ge 2$
# Every integer when divided by $m$ has a unique principal remainder equal to one of the integers in the set $Z_m = \{0, 1, ..., m - 1\}$.<br>

# ---
