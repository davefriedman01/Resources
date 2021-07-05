#!/usr/bin/env python
# coding: utf-8

# # Modular Arithmetic

# ---

# ### Equivalence Class
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $R$ be an equivalence relation on $A$.<br>
# The equivalence class of $x \in A$ determined by $R$ is the set $x/R = \{y \in A : x R y\}$ which is read "x mod R".<br>
# The set of all equivalence classes determined by $R$ is $A/R = \{x/R : x \in A\}$ which is read "A mod R".<br>

# ---

# ### Congruence modulo $m$
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $\equiv_m$ (for a fixed integer $m \ne 0$) be the relation (not necessarily the _equivalence_ relation, which will be proved later) on $\mathbb{Z}$ given by
# 
# $$
# x \equiv_m y\,\,\text{iff}\,\, m \,\,\text{divides}\,\, (x - y)
# $$

# The equivalence class of $x \in \mathbb{Z}$ determined by $\equiv_m$ is the set $\bar{x} = \{y \in \mathbb{Z} : x \equiv_m y\}$.<br>
# The set of equivalence classes determined by $\equiv_m$ is $\mathbb{Z}_m = \{\bar{0}, \bar{1}, \bar{2}, ..., \overline{(m - 1)}\}$.<br>

# <span style="color: blue">Notation</span><br>
# $x \equiv_m y$ may be written $x \equiv y \,(\text{mod}\, m)$ or $x = y \,(\text{mod}\, m)$<br>
# In this context, we write $\bar{x}$ for the equivalence class of $x$ instead of $x/\equiv_m$.<br>
# An equivalence class may be called a congruence class or a residue, since $0, 1, 2, ..., (m - 1)$ are exactly all the possible remainders when integers are divided by $m$.<br>

# ---

# ### Theorem
# 
# $\equiv_m$ is an equivalence relation on $\mathbb{Z}$.<br>

# __Proof__<br>
# $\equiv_m$ is a set of ordered pairs of integers and is thus a relation on $\mathbb{Z}$.<br>
# 
# Let $x$be an integer.<br>
# $m \cdot 0 = 0 = x - x$.<br>
# Thus $m$ divides $x - x$.<br>
# Thus $x \equiv x \,(\text{mod}\, m)$ (by the definition of congruence modulo $m$).<br>
# Therefore, $\equiv_m$ is reflexive on $\mathbb{Z}$ (by the definition of reflexivity).<br>
# 
# Let $x \equiv y \,(\text{mod}\, m)$.<br>
# Thus $m$ divides $x - y$ (by the definition of congruence modulo $m$).<br>
# Thus there is an integer $k$ such that $x - y = km \leftrightarrow -(x - y) = -(km) \leftrightarrow y - x = (-k)m$<br>
# Thus $m$ divides $y - x$.<br>
# Thus $y \equiv x \,(\text{mod}\, m)$ (by the definition of congruence modulo $m$).<br>
# Therefore, $\equiv_m$ is symmetric on $\mathbb{Z}$ (by the definition of symmetry).<br>
# 
# Let $x \equiv y \,(\text{mod}\, m)$ and $y \equiv z \,(\text{mod}\, m)$.<br>
# Thus $m$ divides both $x - y$ and $y - z$ (by the definition of congruence modulo $m$).<br>
# Thus there exist integers $h$ and $k$ such that $x - y = hm$ and $y - z = km$.<br>
# $x - z = x - y + y - z = hm + km = (h + k)m$ where $(h + k)$ is an integer.<br>
# Thus $m$ divides $x - z$.<br>
# Thus $x \equiv z \,(\text{mod}\, m)$ (by the definition of congruence modulo $m$).<br>
# Therefore, $\equiv_m$ is transitive on $\mathbb{Z}$ (by the definition of transitivity).<br>
# 
# Therefore, $\equiv_m$ is an equivalence relation on $\mathbb{Z}$.<br>
# $\blacksquare$<br>

# ### Theorem
# 
# For all $x, y \in \mathbb{Z}$, $x \equiv_m y$ iff $\bar{x} = \bar{y}$.<br>
# 
# __Proof in the first direction__<br>
# First direction: If $x \equiv_m y$, then $\bar{x} = \bar{y}$.<br>
# Assumption: Let $x \equiv_m y$.<br>
# 
# Part I: It must be shown that $\bar{x} \subseteq \bar{y}$.<br>
# Let $z \in \bar{x}$.<br>
# Then $x \equiv_m z$.<br>
# $y \equiv_m x$ (by symmetry).<br>
# Then $y \equiv_m z$ (by transitivity).<br>
# Therefore, $z \in \bar{y}$.<br>
# 
# Part II: It must be shown that $\bar{y} \subseteq \bar{x}$.<br>
# 
# Therefore, $\bar{x} = \bar{y}$.<br>
# 
# __Proof in the second direction__<br>
# Second Direction: If $\bar{x} = \bar{y}$, then $x \equiv_m y$.<br>
# Assumption: Let $\bar{x} = \bar{y}$.<br>
# 
# Therefore, $x \equiv_m y$.<br>
# 
# Therefore, $x \equiv_m y$ iff $\bar{x} = \bar{y}$.<br>
# $\blacksquare$<br>

# ### Theorem
# 
# The set $\mathbb{Z}_m$ has $m$ distinct elements $\{\bar{0}, \bar{1}, \bar{2}, ..., \overline{(m - 1)}\}$.<br>

# __Proof__<br>
# Each $\bar{k}$ for $k = 0, 1, 2, ..., (m - 1)$ is an equivalence class and thus in $\mathbb{Z}_m$.<br>
# Let $\bar{x} \in \mathbb{Z}_m$.<br>
# There exist integers $q$ and $r$ such that $x = mq + r$ where $0 \le r \le m - 1$ (by the division algorithm).<br>
# Thus $mq = x - r$.<br>
# Thus $m$ divides $x - r$.<br>
# Thus $x \equiv r \,(\text{mod}\, m)$ (by the definition of congruence modulo $m$).<br>
# Thus $\bar{x} = \bar{r}$.<br>
# Thus $\bar{x} \in \{\bar{0}, \bar{1}, \bar{2}, ..., \overline{(m - 1)}\}$.<br>
# We will know that $\mathbb{Z}_m$ has exactly $m$ elements when we show that $\bar{0}, \bar{1}, \bar{2}, ..., \overline{(m - 1)}$ are all distinct.<br>
# Let $\bar{k} = \bar{r}$ where $0 \le r \le k \le (m - 1)$.<br>
# Then $k \equiv r \,(\text{mod}\, m)$.<br>
# Thus $m$ divides $k - r$ (by the definition of congruence modulo $m$).<br>
# But $0 \le k - r \le m - 1$, so $k - r = 0$.<br>
# Therefore, $k = r$ and the $m$ equivalence classes are distinct.<br>
# $\blacksquare$<br>

# ---

# #### Modular Additive Identity
# The sum of an integer $a$ mod $m$ and the additive identity element is congruent to the integer $a$ mod $m$.<br>
# 
# $$
# \exists 0 \in Z_m, \forall a \in Z_m, a + 0 \equiv a \,(\text{mod}\, m)
# $$
# 
# #### Modular Addition
# Modular addition is defined as the principal remainder when $a + b$ is divided by $m$.<br>
# 
# $$
# \begin{align}
# a \oplus b &\overset{\text{def}}{=} (a + b) \,\text{mod}\, m \\
# &= (a' + km + b' + lm) \,\text{mod}\, m \\
# &= ((k + l)m + (a' + b')) \,\text{mod}\, m \\
# &= (a' + b') \,\text{mod}\, m \\
# &= (a \,\text{mod}\, m + b \,\text{mod}\, m) \,\text{mod}\, m \\
# \end{align}
# $$
# 
# #### Modular Additive Inverse
# The sum of an integer $a$ mod $m$ and its additive inverse is congruent to the additive identity element.<br>
# 
# $$
# \forall a \in Z_m, \exists (-a) \in Z_m, a + (-a) \equiv 0 \,(\text{mod}\, m)
# $$
# 
# #### Modular Subtraction
# The difference of two integers $a, b$ mod $m$ is the sum of the first integer $a$ mod $m$ and the additive inverse of the second integer $b$ mod $m$.<br>
# 
# $$
# \begin{align}
# a \ominus b &\overset{\text{def}}{=} (a - b) \,\text{mod}\, m \\
# &= (a' + km - (b' + lm)) \,\text{mod}\, m \\
# &= ((k - l)m + (a' - b')) \,\text{mod}\, m \\
# &= (a' - b') \,\text{mod}\, m \\
# &= (a \,\text{mod}\, m - b \,\text{mod}\, m) \,\text{mod}\, m \\
# \end{align}
# $$
# 
# #### Modular Multiplicative Identity
# The product of an integer $a$ mod $m$ and the multiplicative identity element is congruent to the integer $a$ mod $m$.<br>
# 
# $$
# \exists 1 \in Z_m, \forall a \in Z_m, a \cdot 1 \equiv a \,(\text{mod}\, m)
# $$
# 
# #### Modular Multiplication
# Modular multiplication is defined as the principal remainder when $ab$ is divided by $m$.<br>
# 
# $$
# \begin{align}
# a \otimes b &\overset{\text{def}}{=} ab \,\text{mod}\, m \\
# \end{align}
# $$
# 
# #### Modular Multiplicative Inverse
# The product of an integer $a$ mod $m$ and its multiplicative inverse is congruent to the multiplicative identity element.<br>
# The additive identity element does not have a multiplicative inverse.<br>
# The remaining elements may or may not have multiplicative inverses.<br>
# 
# $$
# a \cdot a^{-1} \equiv 1 \,(\text{mod}\, m)
# $$
# 
# #### Determine whether an integer mod $m$ has a multiplicative inverse
# Any nonzero integer $a$ has a multiplicative inverse $a^{-1}$ iff it is relatively prime to $n$.<br>
# 
# Let an integer $a = cb$ and the modulus $m = cn$ share a common factor $c$.<br>
# $aa^{-1} \equiv 1 \,(\text{mod}\, m)$<br>
# $(cb)a^{-1} \equiv 1 \,(\text{mod}\, m)$<br>
# $(ncb)a^{-1} \equiv n \,(\text{mod}\, m)$<br>
# $(mb)a^{-1} \equiv n \,(\text{mod}\, m)$<br>
# Since $mb$ is a multiple of the modulus, the lefthand side is congruent to 0.<br>
# If $n$ is not congruent to 0, the relation and original expression are false: there is no value for $a^{-1}$ which can serve as the multiplicative inverse for $a$.<br>
# The relation and original expression are true when $n$ is congruent to 0.<br>
# $n$ can't be 0 since that would mean $m$ is 0.<br>
# $n$ can't be larger than $m$ since $c$ must be an integer and that would make $m$ greater than $m$.<br>
# $n$ must be equal to $m$ which means that $c$ must be equal to 1.<br>
# Since $c = 1$ is the common factor of $a$ and $m$, $a$ and $m$ are relatively prime.<br>
# 
# #### Modular Division
# The division of two integers $a, b$ mod $m$ is the product of the first integer $a$ mod $m$ and the multiplicative inverse of the second integer $b \ne 0$ mod $m$.<br>
# 
# $$
# \begin{align}
# a \oslash b &\overset{\text{def}}{=} (ab^{-1}) \,\text{mod}\, m \\
# \end{align}
# $$
# 
# #### Modular Exponentiation
# 
# $$a^b a^c \equiv a^{b + c} \,(\text{mod}\, m)$$
# 
# $$(a^b)^c \equiv a^{bc} \,(\text{mod}\, m)$$
# 
# $$
# \begin{align}
# a^2 \,\text{mod}\, m &= (aa) \,\text{mod}\, m \\
# &= ((a \,\text{mod}\, m)(a \,\text{mod}\, m)) \,\text{mod}\, m \\
# &= (a \,\text{mod}\, m)^2 \,\text{mod}\, m \\
# \end{align}
# $$
# 
# We can reduce the exponent mod $n$ where $n$ is the number of positive integers less than $m$ that are relatively prime to $m$.<br>
# 
# $$
# a^e \equiv a^{e \,\text{mod}\, n} \,(\text{mod}\, m)
# $$
# 
# #### Examples
# 
# Evaluate integer arithmetic first, modulo operator last.
# $$
# \begin{align}
# & (((4^2 + 20) - 45) \times 6 + 50) \,\text{mod}\, 7 \\
# &= (((16 + 20) - 45) \times 6 + 50) \,\text{mod}\, 7 \\
# &= ((36 - 45) \times 6 + 50) \,\text{mod}\, 7 \\
# &= (-9 \times 6 + 50) \,\text{mod}\, 7 \\
# &= (-54 + 50) \,\text{mod}\, 7 \\
# &= (-4) \,\text{mod}\, 7 \\
# &= 3
# \end{align}
# $$
# 
# "Distribute" modulo operator, then evaluate all modular expressions.
# $$
# \begin{align}
# & (((4^2 + 20) - 45) \times 6 + 50) \,\text{mod}\, 7 \\
# &= (((((16 + 20) - 45) \times 6) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= ((((((16 + 20) - 45) \,\text{mod}\, 7) \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((((((16 + 20) \,\text{mod}\, 7) - ((45) \,\text{mod}\, 7)) \,\text{mod}\, 7) \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((((((((16) \,\text{mod}\, 7) + ((20) \,\text{mod}\, 7)) \,\text{mod}\, 7) - ((45) \,\text{mod}\, 7)) \,\text{mod}\, 7) \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((((((2 + 6) \,\text{mod}\, 7) - ((45) \,\text{mod}\, 7)) \,\text{mod}\, 7) \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((((1 - ((45) \,\text{mod}\, 7)) \,\text{mod}\, 7) \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((((1 - 3) \,\text{mod}\, 7) \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((5 \times ((6) \,\text{mod}\, 7) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (((5 \times 6) \,\text{mod}\, 7) + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (2 + ((50) \,\text{mod}\, 7)) \,\text{mod}\, 7 \\
# &= (2 + 1) \,\text{mod}\, 7 \\
# &= 3 \\
# \end{align}
# $$
# 
# $$
# \begin{align}
# & 9^{11} \,\text{mod}\, m \\
# &= 31381059609 \,\text{mod}\, m \\
# \end{align}
# $$

# ---

# In[1]:


display(
    (44 + 33) % 57,
    (44 % 57 + 33 % 57) % 57,
    
    (9 - 29) % 57,
    (9 + (-29)) % 57,
    (9 % 57 + (-29) % 57) % 57,
    
    (17 + 42 + 49) % 57,
    (17 % 57 + 42 % 57 + 49 % 57) % 57,
    
    (52 - 30 - 38) % 57,
    (52 % 57 - 30 % 57 - 38 % 57) % 57,
)


# In[2]:


display(
    (95 * 45 * 31),
    (95 * 45 * 31) % 13,
    (95 % 13 * 45 % 13 * 31 % 13) % 13,
    
    (17 * 13 * 19 * 44),
    (17 * 13 * 19 * 44) % 13,
    (17 % 13 * 13 % 13 * 19 % 13 * 44 % 13) % 13,
    
    (12**7 * 77**49),
    (12**7 * 77**49) % 13,
    (12**7 % 13 * 77**49 % 13) % 13,
    (12 * 77) % 13,
)


# In[3]:


p = 31
display(
    # 3/24
    pow(24, p-2, p) * 3 % p,
    # 17^-3
    pow(17, p-4, p),
    # 4^-4 * 11
    pow(4, p-5, p) * 11 % p
)


# ---
