#!/usr/bin/env python
# coding: utf-8

# # Structures

# ---

# <span style="color: blue; font-size: 20px;">**Operation**</span>

# An operation may also be called a function or a computation.

# Let $A$ be a nonempty set.<br>
# For example, a __unary operation__ on $A$ is a function from $A$ to $A$.<br>
# A __binary operation__ on $A$ is a function from $A \times A$ to $A$.<br>
# A __ternary operation__ on $A$ is a function from $A \times A \times A$ to $A$.<br>
# In general, an __$n$-ary operation__ on $A$ is a function from $\underbrace{A \times A \times ... \times A}_{n \,\text{times}}$ to $A$.<br>

# A note on notation:
# 
# __Infix notation__ is standard in integer arithmetic $2 + 2 = 4$
# 
# __Prefix notation__ places the operation before its operands like this $+ \, 2 \, 2 = 4$
# 
# __Function notation__ is a special form of prefix notation $+(2, 2)$; or more commonly, $\text{add}(2, 2)$

# ---

# <span style="color: blue; font-size: 20px;">**Structure**</span>

# A structure is a nonempty set $A$ with a collection of one or more operations on $A$ and a possibly empty collection of relations on $A$.<br>
# A structure may also be called an algebraic structure or an algebraic system.<br>

# The __order__ of a structure is the order of its set.<br>

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
# 
# $(\mathbb{Q}, \cdot)$
# * order infinite
# * closed under $\cdot$
# 
# $(\mathbb{Q}, +)$
# * order infinite
# * closed under $+$
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

# <span style="color: blue; font-size: 20px;">**Properties of Structures**</span>

# ### Closure

# Let $(A, *)$ be a structure and let $B$ be a subset of $A$.<br>
# $B$ is _closed under $*$_ iff for all $x, y \in B, x * y \in B$.<br>

# $A$ is closed under $*$ since $*$ is a function that maps to $A$.<br>
# For any proper subset $B$ of $A$ that is closed under $*$, the same operation $*$ is used to denote the restriction of the operation to $B \times B$.<br>

# The following statements are equivalent:
# 
# $B$ is closed under $*$<br>
# $*$ is an operation on $B$<br>
# $(B, *)$ is a structure<br>

# ---
