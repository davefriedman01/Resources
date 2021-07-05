#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib, json

from pprint import pprint


# In[2]:


dir(hashlib)


# In[3]:


help(hashlib)


# ---

# # Large Numbers

# In[4]:


atoms_in_the_universe = 10**80
googol = 1e100
myoglobin = 2e153
display(
    atoms_in_the_universe,
    googol,
    googol**2,
    myoglobin,
)


# ---

# ### What does hashlib.sha256 do?

# In[5]:


digest = hashlib.sha256(b'Hello world').hexdigest()
digest


# In[6]:


format(int(digest, 16), '0256b')


# In[7]:


len(format(int(digest, 16), '0256b'))


# ---

# # Cryptographic Hash

# In[8]:


# How many SHA256 hashes?
2**256


# In[9]:


# How many SHA512 hashes?
2**512


# ---

# # Python Blockchain

# In[10]:


class Block:
    bid    = 0
    pid    = None
    blocks = [None]
    
    def __init__ (self, data=None):
        self.bid                = Block.bid               # current block id
        self.data               = data
        self.pid, Block.pid     = Block.pid, self.bid     # previous block id
        self.phash              = hashlib.sha256(json.dumps(Block.blocks[-1].__dict__).encode('utf-8')).hexdigest() if Block.blocks[-1] else None
        
        Block.blocks.append(self)
        Block.bid              += 1                       # increment the block number for the next block
        
def bhash (block):
    return hashlib.sha256(json.dumps(block.__dict__).encode('utf-8')).hexdigest()

def print_all_blocks ():
    for block in Block.blocks:
        pprint((block.__dict__, bhash(block)) if block else None)


# In[11]:


# genesis block
bG = Block('Nelson likes cat')
display(
    bG.__dict__,
    bhash(bG),
)


# In[12]:


b1 = Block('Marie likes dog')
display(
    b1.__dict__,
    bhash(b1),
)


# In[13]:


b2 = Block('Marie likes dog')
display(
    b2.__dict__,
    bhash(b2),
)


# In[14]:


print_all_blocks()


# ---

# In[15]:


# How many atoms in the visible universe (i.e., a 46 billion lightyear sphere)?
10**78


# In[16]:


# How old is the universe in seconds?
10**17


# In[17]:


class Blockchain:
    def __init__ (self):
        self.block_genesis = {
            'prev_hash': None,
            'transactions': None,
        }
        self.block_number = 1
        self.blocks = list(self.block_genesis)
    def block (self, block):
        
        self.blocks.append(block)


# In[18]:


block_genesis = {
    'prev_hash': None,
    'transactions': [1, 3, 4, 2]
}
block_genesis_serialized = json.dumps(block_genesis, sort_keys=True).encode('utf-8')
block_genesis_hash = hashlib.sha256(block_genesis_serialized).hexdigest()

block_2 = {
    'prev_hash': block_genesis_hash,
    'transactions': [3, 3, 3, 8, 7, 12]
}
block_2_serialized = json.dumps(block_2, sort_keys=True).encode('utf-8')
block_2_hash = hashlib.sha256(block_2_serialized).hexdigest()

block_3 = {
    'prev_hash': block_2_hash,
    'transactions': [3, 4, 4, 8, 34]
}
block_3_serialized = json.dumps(block_3, sort_keys=True).encode('utf-8')
block_3_hash = hashlib.sha256(block_3_serialized).hexdigest()


# ---
