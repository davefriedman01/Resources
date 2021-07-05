#!/usr/bin/env python
# coding: utf-8

# # Fields

# ---

# ### Abelian Ring with Identity
# An abelian ring with identity that is not also a field satisfies all the properties of a field except for the existence of multiplicative inverse elements.<br>
# 
# Infinite Rings
# * $\mathbb{Z}$ the set of integers (is not a field because, for example, 2 does not have a multiplicative inverse in Z)
# * $F[x]$ the set of polynomials in x with coefficients belonging to a field F

# ---

# ### Field
# A field is a tuple $(F, +, \cdot)$ that consists of a set and two operations called _addition_ and _multiplication_ satisfying the following properties:<br>
# 
# * Additive Closure
# $a, b \in F \rightarrow a + b \in F$
# * Additive Commutativity
# $a + b = b + a$
# * Additive Associativity
# $a + (b + c) = (a + b) + c$
# * Existence of the Additive Identity Element
# $\exists 0 \in F, \forall a \in F, a + 0 = a$
# * Existence of Additive Inverse Elements
# $\forall a \in F, \exists -a \in F, a + (-a) = 0$
# * Multiplicative Closure
# $a, b \in F \rightarrow a \cdot b \in F$
# * Multiplicative Commutativity
# $a \cdot b = b \cdot a$
# * Multiplicative Associativity
# $a \cdot (b \cdot c) = (a \cdot b) \cdot c$
# * Existence of the Multiplicative Identity Element
# $\exists 1 \in F, \forall a \in F, a \cdot 1 = a$
# * Existence of Multiplicative Inverse Elements
# $\forall a \ne 0 \in F, \exists a^{-1} \in F, a \cdot a^{-1} = 1$
# * Distributivity
# $a \cdot (b + c) = a \cdot b + a \cdot c$
# 
# In other words, a field
# * is an abelian group under addition
# * the nonzero elements are an abelian group under multiplication
# * the distributive law holds
# 
# Subtraction<br>
# $a - b \equiv a + (-b)$<br>
# 
# Division<br>
# $a \div b \equiv a \cdot b^{-1}$<br>
# 
# Additional properties of fields:
# * $a0 = 0 \,\,\,\forall a \in F$
# * $(ab = 0) \rightarrow (a = 0 \lor b = 0)$ (if the product ab is zero, then at least one of a or b is zero)
# * $(a \ne 0 \land b \ne 0) \rightarrow (ab \ne 0)$ (the product of two nonzero elements is nonzero)
# 
# Infinite Fields
# * $\mathbb{R}$ the set of real numbers
# * $\mathbb{C}$ the set of complex numbers

# ---

# ### Theorem
# 
# $\mathbb{Z}_m$ is a field iff $m$ is prime.<br>

# ---

# ### Finite Field $F_q$ or Galois Field $\text{GF}(q)$
# A finite field $F_q$ is a field with a finite number of elements $q$, called the order of the field.<br>
# 
# Galois' Theorem<br>
# There exists a field of order $q$ iff $q$ is a prime power $q = p^h$ where $p$ is prime and $h$ is a positive integer. Further, if $q$ is a prime power then there is, up to relabelling, only one field of that order.<br>
# 
# __Prime Field__ $\text{GF}(p) = \{0, 1, ..., p - 1\}$ is a Galois field of order $q = p$ (i.e., where $h = 1$) that consists of the set $\{0, 1, ..., p - 1\}$ with arithmetic carried out modulo $p$.<br>

# ### $\text{GF}(2) = \mathbb{Z}_2 = \{0, 1\}$
# 
# $$
# \begin{align}
# & f_0x^0 & \\
# & 0x^0 & 0 \\
# & 1x^0 & 1 \\
# \end{align}
# $$
# 
# <table>
#     <tr>
#         <td>+</td><td>0</td><td>1</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>1</td>
#     </tr>
#     <tr>
#         <td>1</td><td>1</td><td>0</td>
#     </tr>
# </table>
# 
# <table>
#     <tr>
#         <td>$\cdot$</td><td>0</td><td>1</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>0</td>
#     </tr>
#     <tr>
#         <td>1</td><td>0</td><td>1</td>
#     </tr>
# </table>

# In[1]:


zer = FieldElement(0, 2)
one = FieldElement(1, 2)

display(
    zer + zer,
    zer + one,
    one + zer,
    one + one,
    zer * zer,
    zer * one,
    one * zer,
    one * one,
)


# ### $\text{GF}(3) = \mathbb{Z}_3 = \{0, 1, 2\}$
# 
# $$
# \begin{align}
# & f_0x^0 & \\
# & 0x^0 & 0 \\
# & 1x^0 & 1 \\
# & 2x^0 & 2 \\
# \end{align}
# $$
# 
# <table>
#     <tr>
#         <td>+</td><td>0</td><td>1</td><td>2</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>1</td><td>2</td>
#     </tr>
#     <tr>
#         <td>1</td><td>1</td><td>2</td><td>0</td>
#     </tr>
#     <tr>
#         <td>2</td><td>2</td><td>0</td><td>1</td>
#     </tr>
# </table>
# 
# <table>
#     <tr>
#         <td>$\cdot$</td><td>0</td><td>1</td><td>2</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>0</td><td>0</td>
#     </tr>
#     <tr>
#         <td>1</td><td>0</td><td>1</td><td>2</td>
#     </tr>
#     <tr>
#         <td>2</td><td>0</td><td>2</td><td>1</td>
#     </tr>
# </table>

# In[24]:


zer = FieldElement(0, 3)
one = FieldElement(1, 3)
two = FieldElement(2, 3)

display(
    zer + zer,
    zer + one,
    zer + two,
    one + zer,
    one + one,
    one + two,
    two + zer,
    two + one,
    two + two,
    zer * zer,
    zer * one,
    zer * two,
    one * zer,
    one * one,
    one * two,
    two * zer,
    two * one,
    two * two,
)


# ### $\mathbb{Z}_4 = \{0, 1, 2, 3\}$ not a field
# 
# <table>
#     <tr>
#         <td>+</td><td>0</td><td>1</td><td>2</td><td>3</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>1</td><td>2</td><td>3</td>
#     </tr>
#     <tr>
#         <td>1</td><td>1</td><td>2</td><td>3</td><td>0</td>
#     </tr>
#     <tr>
#         <td>2</td><td>2</td><td>3</td><td>0</td><td>1</td>
#     </tr>
#     <tr>
#         <td>3</td><td>3</td><td>0</td><td>1</td><td>2</td>
#     </tr>
# </table>
# 
# <table>
#     <tr>
#         <td>$\cdot$</td><td>0</td><td>1</td><td>2</td><td>3</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>0</td><td>0</td><td>0</td>
#     </tr>
#     <tr>
#         <td>1</td><td>0</td><td>1</td><td>2</td><td>3</td>
#     </tr>
#     <tr>
#         <td>2</td><td>0</td><td>2</td><td>0</td><td>2</td>
#     </tr>
#     <tr>
#         <td>3</td><td>0</td><td>3</td><td>2</td><td>1</td>
#     </tr>
# </table>

# ### $\text{GF}(4 = 2^2) = \{0, 1, x, x + 1\}$
# 
# $$
# \begin{align}
# f_0x^0 + f_1x^1 & \\
# 0x^0 + 0x^1     && 0      && 0 \\
# 0x^0 + 1x^1     && x      && a \\
# 1x^0 + 0x^1     && 1      && 1 \\
# 1x^0 + 1x^1     && 1 + x  && b \\
# \end{align}
# $$
# 
# <table>
#     <tr>
#         <td>+</td><td>0</td><td>1</td><td>a</td><td>b</td>
#     </tr>
#     <tr>
#         <td>0</td><td>0</td><td>1</td><td>a</td><td>b</td>
#     </tr>
#     <tr>
#         <td>1</td><td>1</td><td>0</td><td>b</td><td>a</td>
#     </tr>
#     <tr>
#         <td>a</td><td>a</td><td>b</td><td>0</td><td>1</td>
#     </tr>
#     <tr>
#         <td>b</td><td>b</td><td>a</td><td>1</td><td>0</td>
#     </tr>
# </table>
# 
# <table>
#     <tr>
#         <td>$\cdot$</td><td>0</td><td>1</td><td>a</td><td>b</td>
#     </tr>
#     <tr>
#         <td>0</td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>1</td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>a</td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>b</td><td></td><td></td><td></td><td></td>
#     </tr>
# </table>

# ### $\text{GF}(5) = \mathbb{Z}_5 = \{0, 1, 2, 3, 4\}$
# 
# $$
# \begin{align}
# & f_0x^0 & \\
# & 0x^0 & 0 \\
# & 1x^0 & 1 \\
# & 2x^0 & 2 \\
# & 3x^0 & 3 \\
# & 4x^0 & 4 \\
# \end{align}
# $$
# 
# <table>
#     <tr>
#         <td>+</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
#     </tr>
#     <tr>
#         <td>0</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>1</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>2</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>3</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>4</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
# </table>
# 
# <table>
#     <tr>
#         <td>$\cdot$</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td>
#     </tr>
#     <tr>
#         <td>0</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>1</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>2</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>3</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>4</td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
# </table>

# ### $\text{GF}(7) = \mathbb{Z}_7 = \{0, 1, 2, 3, 4, 5, 6\}$
# 
# $$
# \begin{align}
# & f_0x^0 & \\
# & 0x^0 & 0 \\
# & 1x^0 & 1 \\
# & 2x^0 & 2 \\
# & 3x^0 & 3 \\
# & 4x^0 & 4 \\
# & 5x^0 & 5 \\
# & 6x^0 & 6 \\
# \end{align}
# $$
# 
# <table>
#     <tr>
#         <td>+</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
#     </tr>
#     <tr>
#         <td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
# </table>
# 
# <table>
#     <tr>
#         <td>$\cdot$</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td>
#     </tr>
#     <tr>
#         <td>0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
#     <tr>
#         <td>6</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
#     </tr>
# </table>

# ### $\mathbb{Z}_8$ not a field
# ### $\text{GF}(8 = 2^3) = \{0, 1, x, x + 1, x^2, x^2 + 1, x^2 + x, x^2 + x + 1\}$
# 
# $$
# \begin{align}
# & f_0x^0 + f_1x^1 + f_2x^2 & \\
# & 0x^0 + 0x^1 + 0x^2       & 0 \\
# & 0x^0 + 0x^1 + 1x^2       & x^2 \\
# & 0x^0 + 1x^1 + 0x^2       & x \\
# & 0x^0 + 1x^1 + 1x^2       & x + x^2 \\
# & 1x^0 + 0x^1 + 0x^2       & 1 \\
# & 1x^0 + 0x^1 + 1x^2       & 1 + x^2 \\
# & 1x^0 + 1x^1 + 0x^2       & 1 + x \\
# & 1x^0 + 1x^1 + 1x^2       & 1 + x + x^2 \\
# \end{align}
# $$

# ### $\mathbb{Z}_9$ not a field
# ### $\text{GF}(9 = 3^2) = \{0, 1, 2, x, x + 1, x + 2, 2x, 2x + 1, 2x + 2\}$
# 
# $$
# \begin{align}
# & f_0x^0 + f_1x^1 & \\
# & 0x^0 + 0x^1     & 0 \\
# & 0x^0 + 1x^1     & x \\
# & 0x^0 + 2x^1     & 2x \\
# & 1x^0 + 0x^1     & 1 \\
# & 1x^0 + 1x^1     & 1 + x \\
# & 1x^0 + 2x^1     & 1 + 2x \\
# & 2x^0 + 0x^1     & 2 \\
# & 2x^0 + 1x^1     & 2 + x \\
# & 2x^0 + 2x^1     & 2 + 2x \\
# \end{align}
# $$

# ### $\text{GF}(11) = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$

# ### $\text{GF}(13)= \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$

# ### $\text{GF}(16 = 2^4)$

# ---
