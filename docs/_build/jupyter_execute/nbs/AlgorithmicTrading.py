#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.set_printoptions(precision=4)
import numpy.random as npr
import numpy_financial as npf
import pandas as pd
import pandas_datareader as pdr

from scipy.optimize import curve_fit
import scipy.stats as scs

get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import mpl, plt
import seaborn as sns
mpl.style.use('seaborn')
mpl.rcParams['figure.figsize'] = (10, 6)

import    datetime as dt,    json,    math,    requests,    threading,    time
import warnings
warnings.filterwarnings('ignore')

import panel as pn
pn.extension('plotly')
import plotly.express as px
import hvplot.pandas



import yfinance as yf

from dotenv import find_dotenv, get_key

import quandl
quandl.ApiConfig.api_key = get_key(find_dotenv(), 'QUANDL_API_KEY')

API_KEY = get_key(find_dotenv(), 'ALPACA_API_KEY')
API_SECRET = get_key(find_dotenv(), 'ALPACA_SECRET_KEY')
APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame
api = REST(
    API_KEY,
    API_SECRET,
    api_version='v2',
)


# ---

# Bitfinex [Home](https://www.bitfinex.com)<br>
# Kraken [Home](https://www.kraken.com/en-us/)<br>

# # Algorithmic Trading

# Trading Signal<br>
# Backtest<br>
# Portfolio Performance<br>
# Per-Trade Performance<br>
# Technical Analysis<br>
# Fundamental Analysis<br>
# 
# Dual Moving Average Crossover<br>
# Kraken Cryptocurrency Exchange API<br>
# asyncio<br>
# streaming<br>
# Heroku<br>
# 
# AlphaVantage<br>
# split adjusted<br>
# Advances in Financial Machine Learning, Marcos Lopez de Prado<br>
# 	fractal differencing<br>
#     
# Entry Strategy<br>
# Exit Strategy<br>

# ---

# Activity 1

# In[3]:


amd_df = pd.DataFrame({"close": [30.05, 30.36, 30.22, 30.52, 30.45, 31.85, 30.47, 30.60, 30.21, 31.30]})
amd_df.index = pd.bdate_range(start='2019-09-09', periods=10)
amd_df.plot();


# In[4]:


amd_df['side'] = np.nan
previous_price = 0
for index, row in amd_df.iterrows():
    if previous_price == 0:
        amd_df.loc[index, 'side'] = 'buy'
    elif row['close'] < previous_price:
        amd_df.loc[index, 'side'] = 'buy'
    elif row['close'] > previous_price:
        amd_df.loc[index, 'side'] = 'sell'
    else:
        amd_df.loc[index, 'side'] = 'hold'
    previous_price = row['close']
amd_df


# In[5]:


amd_df['side'] = np.nan
amd_df['per share profit/loss'] = np.nan
previous_price = 0
buy = []
sell = []
for index, row in amd_df.iterrows():
    if previous_price == 0:
        amd_df.loc[index, 'side'] = 'buy'
        buy.append(row['close'])
        amd_df.loc[index, 'per share profit/loss'] = 0
    elif row['close'] < previous_price:
        amd_df.loc[index, 'side'] = 'buy'
        buy.append(row['close'])
        amd_df.loc[index, 'per share profit/loss'] = 0
    elif row['close'] > previous_price:
        amd_df.loc[index, 'side'] = 'sell'
        sell.append(row['close'])
        amd_df.loc[index, 'per share profit/loss'] = sell[-1] - buy[-1]
    else:
        amd_df.loc[index, 'side'] = 'hold'
    previous_price = row['close']
amd_df


# In[7]:


# initialize capital
initial_capital = 100_000
# initialize share size
share_size      = 1_000
# calculate the total profit/loss for 500 share size orders
total_profit_loss = round(amd_df['per share profit/loss'].sum() * share_size, 2)
# calculate ROI
roi = round((total_profit_loss / initial_capital) * 100, 2)
print(
    f'The total profit/loss of the trading strategy is ${total_profit_loss},',
    f'resulting in a return on investment of {roi}%',
)


# In[ ]:




