#!/usr/bin/env python
# coding: utf-8

# # Sets

# ---

# ## Sets
# 
# <span style="color: blue">**DEFINITION**</span><br>
# A set is a collection of objects called elements (or members, points, etc.).<br>

# The __order__ of a set is the number of elements in the set if the set is finite or infinite if the number of elements in the set is infinite.

# ---

# Examples of sets:
# 
# * $\mathbb{N}$ the set of natural numbers
#   * $\mathbb{N} \cup \{0\} \overset{\text{def}}= \{0, 1, 2, ...\}$ the set of natural numbers including zero
#   * $\mathbb{N} - \{0\} \overset{\text{def}}= \{1, 2, ...\}$ the set of natural numbers excluding zero
# * $\mathbb{Z} \overset{\text{def}}= \{..., -2, -1, 0, 1, 2, ...\}$ the set of integers
#   * $\mathbb{Z}^+$ the set of positive integers (equivalent to $\mathbb{N} - \{0\}$)
#   * $\mathbb{Z}^+ \cup \{0\}$ the set of nonnegative integers (equivalent to $\mathbb{N} \cup \{0\}$)
#   * $\mathbb{E} \overset{\text{def}}= \{..., -2, 0, 2 ...\}$ the set of even integers
# * $\mathbb{Q} \overset{\text{def}}= \{\frac{p}{q} : p, q \in \mathbb{Z}, q \ne 0\}$ the set of rational numbers
# * $\mathbb{R}$ the set of real numbers
#   * $\mathbb{R}^-$ the set of negative numbers
# * $\mathbb{C} \overset{\text{def}}= \{a + bi : a, b \in \mathbb{R}, i \overset{\text{def}}= \sqrt{-1}\}$ the set of complex numbers
# * $\{0, 1\}^n$ the set of $n$-bit binary strings

# $$
# \mathbb{N}
# \subset
# \mathbb{Z}
# \subset
# \mathbb{Q}
# \subset
# \mathbb{R}
# \subset
# \mathbb{C}
# $$

# ---
