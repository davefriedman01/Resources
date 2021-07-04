#!/usr/bin/env python
# coding: utf-8

# # Structures

# ---

# ## What is an operation?

# <span style="color: blue">Note:</span><br>
# An operation may also be called a function or a computation.

# <span style="color: blue">**DEFINITION**</span><br>
# Let $A$ be a nonempty set.<br>
# A __unary operation__ on $A$ is a function from $A$ to $A$.<br>
# A __binary operation__ on $A$ is a function from $A \times A$ to $A$.<br>
# A __ternary operation__ on $A$ is a function from $A \times A \times A$ to $A$.<br>
# In general, an __$n$-ary operation__ on $A$ is a function from $\underbrace{A \times A \times ... \times A}_{n \,\text{times}}$ to $A$.<br>

# <span style="color: blue">Notation</span><br>
# __Infix notation__ is standard in integer arithmetic $2 + 2 = 4$<br>
# __Prefix notation__ places the operation before its operands like this $+ \, 2 \, 2 = 4$<br>
# __Function notation__ is a special form of prefix notation $+(2, 2)$; or more commonly, $\text{add}(2, 2)$<br>

# ---

# ## What is a structure?

# <span style="color: blue">**DEFINITION**</span><br>
# A structure is a nonempty set $A$ with a collection of one or more operations on $A$ and a possibly empty collection of relations on $A$.<br>

# <span style="color: blue">Note:</span><br>
# A structure may also be called an algebraic structure or an algebraic system.<br>

# <span style="color: blue">**DEFINITION**</span><br>
# The __order__ of a structure is the order of its set.<br>

# <span style="color: green">Example</span><br>
# Examples of structures:
# 
# $(\mathbb{R}, +, \cdot, \lt)$
# * order infinite
# 
# $(\mathbb{R}, \cdot)$
# * order infinite
# 
# $(\mathbb{R}, +)$
# * order infinite
# * closed under $+$
# * associative
# * commutative
# * identity element 0
# * every element has an inverse: its negative
# 
# $(\mathbb{Q}, \cdot)$
# * order infinite
# * closed under $\cdot$
# 
# $(\mathbb{Q}, +)$
# * order infinite
# * closed under $+$
# 
# $(\mathbb{Z}, \cdot)$
# * order infinite
# * closed under $\cdot$
# * associative
# * commutative
# * identity element $1$
# * only $\{1, -1\}$ have inverses
# 
# $(\mathbb{N}, +, \lt)$
# * order infinite
# 
# $(\mathbb{E}, \cdot)$ the set of even integers
# * order infinite
# * closed under $\cdot$
# 
# $(\mathbb{E}, +)$ the set of even integers
# * order infinite
# * closed under $+$
# 
# $((0, 1), \cdot)$ the open interval $(0, 1)$
# * order infinite
# * closed under $\cdot$
# 
# $((0, 1), +)$ the open interval $(0, 1)$
# * order infinite
# * not closed under $+$
# 
# $(\{0, 1\}, \cdot)$
# * order 2
# * closed under $\cdot$
# 
# $(\{0, 1\}, +)$
# * order 2
# * not closed under $+$
# 
# $(\{0\}, \cdot)$
# * order 1
# * closed under $\cdot$
# 
# $(\{0\}, +)$
# * order 1
# * closed under $+$

# ---

# ## Properties of Structures

# ### Closure

# <span style="color: blue">**DEFINITION**</span><br>
# Let $(A, *)$ be a structure and let $B$ be a subset of $A$.<br>
# $B$ is _closed under $*$_ iff for all $x, y \in B, x * y \in B$.<br>

# $A$ is closed under $*$ since $*$ is a function that maps to $A$.<br>
# For any proper subset $B$ of $A$ that is closed under $*$, the same operation $*$ is used to denote the restriction of the operation to $B \times B$.<br>

# The following statements are equivalent:
# 
# $B$ is closed under $*$<br>
# $*$ is an operation on $B$<br>
# $(B, *)$ is a structure<br>

# ### Associativity
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $(A, *)$ be a structure.<br>
# $*$ is associative on $A$ iff for all $x, y, z \in A, (x * y) * z = x * (y * z)$.<br>

# ### Commutativity
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $(A, *)$ be a structure.<br>
# $*$ is commutative on $A$ iff for all $x, y \in A, x * y = y * x$.<br>

# ### Existence of an Identity Element
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $(A, *)$ be a structure.<br>
# An element $e$ of $A$ is an identity element for $*$ iff for all $x \in A, x * e = e = e * x$.<br>

# ### Existence of Inverse Elements
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $(A, *)$ be a structure.<br>
# If $A$ has an identity element $e$, and $a$ and $b$ are in $A$, then $b$ is an inverse of $a$ iff $a * b = b * a = e$. In this case, $a$ would also be an inverse of $b$.<br>

# ---

# ## Operation Tables
# 
# <span style="color: blue">**DEFINITION**</span><br>
# An operation table for a structure $(A, *)$ of order $n$ is an $n \times n$ array of products such that the product $x * y$ appears in row $x$ and column $y$.<br>

# $*$ is commutative on $A$ if the operation table for $(A, *)$ is symmetric about its main diagonal.<br>

# There is no easy way to check that $*$ is associative on $A$ just by visually inspecting the operation table for $(A, *)$.<br>
# For a structure of order $n$, associativity requires the equivalence all $n^3$ products of three elements  $x * y * z$ grouped two ways  $(x * y) * z$ and  $x * (y * z)$.<br>

# <span style="color: green">Example</span><br>
# $(\{1, 2, 3\}, *)$
# 
# $
# \begin{array}{c | c c c}
# * & 1 & 2 & 3 \\
# \hline 
# 1 & 3 & 2 & 1 \\ 
# 2 & 3 & 1 & 3 \\ 
# 3 & 2 & 3 & 3 \\ 
# \end{array}
# $

# Properties<br>
# * closed under $*$
# * not commutative
#   * $1 * 1 = 3$
#   * <span style="color: red;">$1 * 2 = 2$ but $2 * 1 = 3$</span>
#   * <span style="color: red;">$1 * 3 = 1$ but $3 * 1 = 2$</span>
#   * $2 * 2 = 1$
#   * $2 * 3 = 3$ and $3 * 2 = 3$
#   * $3 * 3 = 3$
# * not associative
#   * <span style="color: red;">$(1 * 1) * 1 = 2$ but $1 * (1 * 1) = 1$</span>
#   * <span style="color: red;">$(1 * 1) * 2 = 3$ but $1 * (1 * 2) = 2$</span>
#   * $(1 * 1) * 3 = 3$ and $1 * (1 * 3) = 3$
#   * <span style="color: red;">$(1 * 2) * 1 = 3$ but $1 * (2 * 1) = 1$</span>
#   * <span style="color: red;">$(1 * 2) * 2 = 1$ but $1 * (2 * 2) = 3$</span>
#   * <span style="color: red;">$(1 * 2) * 3 = 3$ but $1 * (2 * 3) = 1$</span>
#   * <span style="color: red;">$(1 * 3) * 1 = 3$ but $1 * (3 * 1) = 2$</span>
#   * <span style="color: red;">$(1 * 3) * 2 = 2$ but $1 * (3 * 2) = 1$</span>
#   * $(1 * 3) * 3 = 1$ and $1 * (3 * 3) = 1$
#   * ...
# * no identity element

# <span style="color: green">Example</span><br>
# $(\{1, 2, 3\}, \circ)$
# 
# $
# \begin{array}{c | c c c}
# \circ & 1 & 2 & 3 \\
# \hline 
# 1 & 1 & 2 & 3 \\ 
# 2 & 1 & 2 & 3 \\ 
# 3 & 1 & 2 & 3 \\ 
# \end{array}
# $

# Properties<br>
# * closed under $\circ$
# * not commutative
#   * $1 \circ 1 = 1$
#   * <span style="color: red;">$1 \circ 2 = 2$ but $2 \circ 1 = 1$</span>
#   * ...
# * associative
#   * $(1 \circ 1) \circ 1 = 1$ and $1 \circ (1 \circ 1) = 1$
#   * $(1 \circ 1) \circ 2 = 2$ and $1 \circ (1 \circ 2) = 2$
#   * $(1 \circ 1) \circ 3 = 3$ and $1 \circ (1 \circ 3) = 3$
#   * $(1 \circ 2) \circ 1 = 1$ and $1 \circ (2 \circ 1) = 1$
#   * $(1 \circ 2) \circ 2 = 2$ and $1 \circ (2 \circ 2) = 2$
#   * $(1 \circ 2) \circ 3 = 3$ and $1 \circ (2 \circ 3) = 3$
#   * $(1 \circ 3) \circ 1 = 1$ and $1 \circ (3 \circ 1) = 1$
#   * $(1 \circ 3) \circ 2 = 2$ and $1 \circ (3 \circ 2) = 2$
#   * $(1 \circ 3) \circ 3$ and $1 \circ (3 \circ 3)$
#   * $(2 \circ 1) \circ 1$ and $2 \circ (1 \circ 1)$
#   * $(2 \circ 1) \circ 2$ and $2 \circ (1 \circ 2)$
#   * $(2 \circ 1) \circ 3$ and $2 \circ (1 \circ 3)$
#   * $(2 \circ 2) \circ 1$ and $2 \circ (2 \circ 1)$
#   * $(2 \circ 2) \circ 2$ and $2 \circ (2 \circ 2)$
#   * $(2 \circ 2) \circ 3$ and $2 \circ (2 \circ 3)$
#   * $(2 \circ 3) \circ 1$ and $2 \circ (3 \circ 1)$
#   * $(2 \circ 3) \circ 2$ and $2 \circ (3 \circ 2)$
#   * $(2 \circ 3) \circ 3$ and $2 \circ (3 \circ 3)$
#   * $(3 \circ 1) \circ 1$ and $3 \circ (1 \circ 1)$
#   * $(3 \circ 1) \circ 2$ and $3 \circ (1 \circ 2)$
#   * $(3 \circ 1) \circ 3$ and $3 \circ (1 \circ 3)$
#   * $(3 \circ 2) \circ 1$ and $3 \circ (2 \circ 1)$
#   * $(3 \circ 2) \circ 2$ and $3 \circ (2 \circ 2)$
#   * $(3 \circ 2) \circ 3$ and $3 \circ (2 \circ 3)$
#   * $(3 \circ 3) \circ 1$ and $3 \circ (3 \circ 1)$
#   * $(3 \circ 3) \circ 2$ and $3 \circ (3 \circ 2)$
#   * $(3 \circ 3) \circ 3$ and $3 \circ (3 \circ 3)$
# * no identity element

# <span style="color: green">Example</span><br>
# $(\{1, 2, 3\}, \cdot)$
# 
# $
# \begin{array}{c | c c c}
# \cdot & 1 & 2 & 3 \\
# \hline 
# 1 & 3 & 1 & 2 \\ 
# 2 & 1 & 2 & 3 \\ 
# 3 & 2 & 3 & 1 \\ 
# \end{array}
# $

# Properties<br>
# * closed under $\cdot$
# * commutative
#   * $1 \cdot 1 = 3$
#   * $1 \cdot 2 = 1$ and $2 \cdot 1 = 1$
#   * $1 \cdot 3 = 2$ and $3 \cdot 1 = 2$
#   * $2 \cdot 2 = 2$
#   * $2 \cdot 3 = 3$ and $3 \cdot 2 = 3$
#   * $3 \cdot 3 = 1$
# * associative
#   * $(1 \cdot 1) \cdot 1$ and $1 \cdot (1 \cdot 1)$
#   * $(1 \cdot 1) \cdot 2$ and $1 \cdot (1 \cdot 2)$
#   * $(1 \cdot 1) \cdot 3$ and $1 \cdot (1 \cdot 3)$
#   * $(1 \cdot 2) \cdot 1$ and $1 \cdot (2 \cdot 1)$
#   * $(1 \cdot 2) \cdot 2$ and $1 \cdot (2 \cdot 2)$
#   * $(1 \cdot 2) \cdot 3$ and $1 \cdot (2 \cdot 3)$
#   * $(1 \cdot 3) \cdot 1$ and $1 \cdot (3 \cdot 1)$
#   * $(1 \cdot 3) \cdot 2$ and $1 \cdot (3 \cdot 2)$
#   * $(1 \cdot 3) \cdot 3$ and $1 \cdot (3 \cdot 3)$
#   * $(2 \cdot 1) \cdot 1$ and $2 \cdot (1 \cdot 1)$
#   * $(2 \cdot 1) \cdot 2$ and $2 \cdot (1 \cdot 2)$
#   * $(2 \cdot 1) \cdot 3$ and $2 \cdot (1 \cdot 3)$
#   * $(2 \cdot 2) \cdot 1$ and $2 \cdot (2 \cdot 1)$
#   * $(2 \cdot 2) \cdot 2$ and $2 \cdot (2 \cdot 2)$
#   * $(2 \cdot 2) \cdot 3$ and $2 \cdot (2 \cdot 3)$
#   * $(2 \cdot 3) \cdot 1$ and $2 \cdot (3 \cdot 1)$
#   * $(2 \cdot 3) \cdot 2$ and $2 \cdot (3 \cdot 2)$
#   * $(2 \cdot 3) \cdot 3$ and $2 \cdot (3 \cdot 3)$
#   * $(3 \cdot 1) \cdot 1$ and $3 \cdot (1 \cdot 1)$
#   * $(3 \cdot 1) \cdot 2$ and $3 \cdot (1 \cdot 2)$
#   * $(3 \cdot 1) \cdot 3$ and $3 \cdot (1 \cdot 3)$
#   * $(3 \cdot 2) \cdot 1$ and $3 \cdot (2 \cdot 1)$
#   * $(3 \cdot 2) \cdot 2$ and $3 \cdot (2 \cdot 2)$
#   * $(3 \cdot 2) \cdot 3$ and $3 \cdot (2 \cdot 3)$
#   * $(3 \cdot 3) \cdot 1$ and $3 \cdot (3 \cdot 1)$
#   * $(3 \cdot 3) \cdot 2$ and $3 \cdot (3 \cdot 2)$
#   * $(3 \cdot 3) \cdot 3$ and $3 \cdot (3 \cdot 3)$
# * identity element 2
#   * $1 \cdot 2 = 1 = 2 \cdot 1$
#   * $2 \cdot 2 = 2$
#   * $3 \cdot 2 = 3 = 2 \cdot 3$
# * inverse elements
#   * $1$ and $3$ are inverses
#   * $2$ is its own inverse

# <span style="color: green">Example</span><br>
# $(\{1, 2, 3\}, +)$
# 
# $
# \begin{array}{c | c c c}
# + & 1 & 2 & 3 \\
# \hline 
# 1 & 3 & 3 & 1 \\ 
# 2 & 1 & 1 & 2 \\ 
# 3 & 1 & 2 & 3 \\ 
# \end{array}
# $

# Properties<br>
# * closed under $+$
# * not commutative
#   * $1 + 1 = 3$
#   * <span style="color: red;">$1 + 2 = 3$ but $2 + 1 = 1$</span>
#   * $1 + 3 = 1$ and $3 + 1 = 1$
#   * $2 + 2 = 1$
#   * $2 + 3 = 2$ and $3 + 2 = 2$
#   * $3 + 3 = 3$
# * not associative
#   * $(1 + 1) + 1 = 1$ and $1 + (1 + 1) = 1$
#   * <span style="color: red;">$(1 + 1) + 2 = 2$ but $1 + (1 + 2) = 1$</span>
#   * ...
# * identity element 3
#   * $1 + 3 = 1 = 3 + 1$
#   * $2 + 3 = 2 = 3 + 2$
#   * $3 + 3 = 3$
# * inverse elements
#   * $3$ is its own inverse
#   * $1$ and $2$ do not have inverses

# ---
