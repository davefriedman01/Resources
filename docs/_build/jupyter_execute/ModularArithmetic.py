#!/usr/bin/env python
# coding: utf-8

# # Modular Arithmetic

# ---

# ### Equivalence Class
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $R$ be an equivalence relation on $A$.<br>
# For $x \in A$, the equivalence class of $x$ determined by $R$ is the set $x/R = \{y \in A : x R y\}$ which is read "x mod R".<br>

# The set of all equivalence classes $A/R = \{x/R : x \in A\}$ which is read "A mod R".<br>

# ---

# ### Congruence modulo $m$
# 
# <span style="color: blue">**DEFINITION**</span><br>
# Let $\equiv_m$ for a fixed integer $m \ne 0$ be the relation on $\mathbb{Z}$ given by
# 
# $$
# x \equiv_m y\,\,\text{iff}\,\, m \,\,\text{divides}\,\, (x - y)
# $$

# <span style="color: blue">Notation</span><br>
# $x \equiv_m y$ may be written $x \equiv y \,(\text{mod}\, m)$ or $x = y \,(\text{mod}\, m)$<br>

# ---

# ### $\mathbb{Z}_m$ the set of congruence classes modulo $m$

# In this context, we write $\bar{x}$ for the equivalence class of $x$ instead of $x/\equiv_m$.<br>

# The equivalence class of $x \in \mathbb{Z}$ is $\bar{x} = \{y \in \mathbb{Z} : x \equiv_m y\}$

# ---

# ### Theorem
# 
# There are exactly $m$ different equivalence classes for the relation $\equiv_m$.<br>
# The set $\mathbb{Z}_m$ is always ${\bar{0}, \bar{1}, \bar{2}, ..., \overline{(m - 1)}}$.<br>

# In[ ]:




