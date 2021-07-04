#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import numpy.random as npr
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import mpl, plt
plt.style.use('seaborn')
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'serif'

import csv, math, random
import tables as tb

import configparser
c = configparser.ConfigParser()
c.read('pyalgo.cfg')

import quandl as q
q.ApiConfig.api_key = c['quandl']['api_key']


# ---

# https://www.quandl.com/data/BCHAIN/MKPRU-Bitcoin-Market-Price-USD<br>

# ---

# In[26]:


def generate_sample_data (rows, cols, freq='1min'):
    ''' Function to generate sample financial data.
    
    Parameters
    ==========
    rows: int
        number of rows to generate
    cols: int
        number of columns to generate
    freq: str
        frequency string for DatetimeIndex
        
    Returns
    =======
    df: DataFrame
        DataFrame object with the sample data
    '''
    r = 0.05 # constant short rate
    sigma = 0.5 # volatility factor
    rows = int(rows)
    cols = int(cols)
    # generate a DatetimeIndex object given the frequency
    index = pd.date_range('2021-1-1', periods=rows, freq=freq)
    # determine time delta in year fractions
    dt = (index[1] - index[0]) / pd.Timedelta(value='365D')
    # generate column names
    columns = ['No%d' % i for i in range(cols)]
    # generate sample paths for geometric Brownian motion
    raw = np.exp(np.cumsum((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * npr.standard_normal((rows, cols)), axis=0))
    # normalize the data to start at 100
    raw = raw / raw[0] * 100
    # generate the DataFrame object
    df = pd.DataFrame(raw, index=index, columns=columns)
    return df


# ---

# # Ch. 1 Python and Algorithmic Trading

# In[2]:


get_ipython().run_cell_magic('time', '', 'S0     = 100\nr      = 0.05\nT      = 1\nsigma  = 0.2\nvalues = []\nfor _ in range(1_000_000):\n    ST = S0 * math.exp((r - 0.5 * sigma ** 2) * T + sigma * random.gauss(0, 1) * math.sqrt(T))\n    values.append(ST)')


# In[5]:


get_ipython().run_cell_magic('time', '', 'S0     = 100\nr      = 0.05\nT      = 1\nsigma  = 0.2\nST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * npr.standard_normal(1_000_000) * np.sqrt(T))')


# In[12]:


1.21e0 / 46.8e-3


# In[18]:


d = q.get('BCHAIN/MKPRU')
d.info()


# In[20]:


d['Value'].resample('A').last()


# In[21]:


d['SMA'] = d['Value'].rolling(100).mean()
d.loc['2013-1-1':].plot(title='BTC/USD exchange rate', figsize=(10, 6));


# ---

# # Ch. 3 Working with Financial Data

# In[2]:


with open('data/AAPL.csv', 'r') as f:
    for _ in range(5):
        print(f.readline(), end='')


# In[12]:


data = pd.read_csv('data/AAPL.csv', index_col=0, parse_dates=True)
data.info()


# In[16]:


data.to_excel('data/aapl.xlsx', 'AAPL')
data.to_json('data/aapl.json')

data_copy_1 = pd.read_excel('data/aapl.xlsx', 'AAPL', index_col=0)
display(data_copy_1.head())

data_copy_2 = pd.read_json('data/aapl.json')
display(data_copy_2.head())


# In[22]:


data = q.get('FSE/SAP_X', start_date='2018-1-1', end_date='2021-05-01')
vol = q.get('VOL/MSFT')
vol.iloc[:, :10].info()
vol[['IvMean30', 'IvMean60', 'IvMean90']].tail()


# In[37]:


get_ipython().run_line_magic('time', 'data = generate_sample_data(rows=5e6, cols=10).round(4)')
h5 = pd.HDFStore('data/data.h5', 'w')
get_ipython().run_line_magic('time', "h5['data'] = data")
h5.close()


# In[39]:


get_ipython().run_line_magic('time', 'data = generate_sample_data(rows=5e6, cols=10).round(4)')
get_ipython().run_line_magic('time', "data.to_hdf('data/data.h5', 'data', format='table')")
get_ipython().run_line_magic('time', "data_copy = pd.read_hdf('data/data.h5', 'data')")


# In[44]:


h5 = tb.open_file('data/data.h5', 'r')
h5
h5.root.data.table[:3]
h5.close()


# ---

# # Ch. 4 Mastering Vectorized Backtesting

# In[53]:


raw = pd.read_csv('http://hilpisch.com/pyalgo_eikon_eod_data.csv', index_col=0, parse_dates=True).dropna()
raw.info()


# In[54]:


data = pd.DataFrame(raw['EUR='])
data = data.rename(columns={'EUR=': 'price'})
data.info()


# In[55]:


data['SMA1'] = data['price'].rolling(42).mean()
data['SMA2'] = data['price'].rolling(252).mean()
data.plot(title='EUR/USD | 42 & 252 days SMAs', figsize=(10, 6));


# In[56]:


data['position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)
data['position'].plot(ylim=[-1.1, 1.1], title='Market Positioning', figsize=(10, 6));


# In[57]:


data['returns'] = np.log(data['price'] / data['price'].shift(1))
data['returns'].hist(bins=35, figsize=(10, 6));


# In[58]:


data['strategy'] = data['position'].shift(1) * data['returns']
data[['returns', 'strategy']].sum()


# In[59]:


data[['returns', 'strategy']].sum().apply(np.exp)


# In[66]:


data[['returns', 'strategy']].cumsum().apply(np.exp).plot(title='Gross performance of EUR/USD compared to the SMA-based strategy', figsize=(10, 6));


# In[ ]:




