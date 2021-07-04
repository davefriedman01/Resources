#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import numpy.random as npr
import numpy_financial as npf
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import mpl, plt
import seaborn as sns
mpl.style.use('seaborn')
mpl.rcParams['figure.figsize'] = (10, 6)

import    datetime as dt,    json,    requests,    time
import warnings
warnings.filterwarnings('ignore')

import panel as pn
pn.extension('plotly')
import plotly.express as px
import hvplot.pandas

from dotenv import find_dotenv, get_key
alpaca_api_key = get_key(find_dotenv(), 'ALPACA_API_KEY')
alpaca_secret_key = get_key(find_dotenv(), 'ALPACA_SECRET_KEY')
import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import REST, TimeFrame
api = REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version='v2',
)


# ---

# In[2]:


get_ipython().system('cat donofrio-linn-tarker/Resources/coin_Bitcoin.csv | head -n2')


# In[3]:


df_btc = pd.read_csv('donofrio-linn-tarker/Resources/coin_Bitcoin.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)[['Volume', 'Close']]
df_eth = pd.read_csv('donofrio-linn-tarker/Resources/coin_Ethereum.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)[['Volume', 'Close']]
df_lte = pd.read_csv('donofrio-linn-tarker/Resources/coin_Litecoin.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)[['Volume', 'Close']]
df_xrp = pd.read_csv('donofrio-linn-tarker/Resources/coin_XRP.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)[['Volume', 'Close']]

df_crypto_close = pd.concat([df_btc['Close'], df_eth['Close'], df_lte['Close'], df_xrp['Close']], axis=1, join='inner')
df_crypto_close.columns = ['BTC_Close', 'ETH_Close', 'LTE_Close', 'XRP_Close']

df_crypto_vol = pd.concat([df_btc['Volume'], df_eth['Volume'], df_lte['Volume'], df_xrp['Volume']], axis=1, join='inner')
df_crypto_vol.columns = ['BTC_Vol', 'ETH_Vol', 'LTE_Vol', 'XRP_Vol']


# In[4]:


ticker = ['DIA', 'SPY', 'IWM', 'GLD']
timeframe = '1D'
start = pd.Timestamp('2017-03-09', tz='America/New_York').isoformat()
end = pd.Timestamp('2021-02-27', tz='America/New_York').isoformat()
df_ticker = api.get_barset(
    ticker,
    timeframe,
    start=start,
    end=end,
    limit=1000,
).df
df_ticker.columns = ['_'.join(col) for col in df_ticker.columns.values]

df_stock_close = pd.concat([df_ticker['DIA_close'], df_ticker['SPY_close'], df_ticker['IWM_close'], df_ticker['GLD_close']], axis=1, join='inner')
df_stock_close.index = pd.DatetimeIndex(df_stock_close.index.date)
df_stock_close.index.name = 'Date'

df_stock_vol = pd.concat([df_ticker['DIA_volume'], df_ticker['SPY_volume'], df_ticker['IWM_volume'], df_ticker['GLD_volume']], axis=1, join='inner')
df_stock_vol.index = pd.DatetimeIndex(df_stock_vol.index.date)
df_stock_vol.index.name = 'Date'


# In[5]:


(df_crypto_close.pct_change() + 1).cumprod().dropna().plot();
(df_crypto_vol.pct_change() + 1).cumprod().dropna().plot();
(df_stock_close.pct_change() + 1).cumprod().dropna().plot();
(df_stock_vol.pct_change() + 1).cumprod().dropna().plot();


# In[6]:


(df_crypto_close.pct_change() + 1).cumprod().dropna()
(df_crypto_vol.pct_change() + 1).cumprod().dropna()
(df_stock_close.pct_change() + 1).cumprod().dropna()
(df_stock_vol.pct_change() + 1).cumprod().dropna()

df_all_close = pd.concat([(df_crypto_close.pct_change() + 1).cumprod().dropna(), (df_stock_close.pct_change() + 1).cumprod().dropna()], axis=1).dropna()
df_all_vol = pd.concat([(df_crypto_vol.pct_change() + 1).cumprod().dropna(), (df_stock_vol.pct_change() + 1).cumprod().dropna()], axis=1).dropna()

display(
    df_all_close.head(),
    df_all_vol.head(),
)


# In[7]:


df_combined_returns = pd.read_csv('donofrio-linn-tarker/Resources/combined_returns_df.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)
df_combined_vol = pd.read_csv('donofrio-linn-tarker/Resources/combined_vol_df.csv', index_col='Date', parse_dates=True, infer_datetime_format=True)

display(
    df_combined_returns.head(),
    df_combined_vol.head(),
)


# In[8]:


df_all_close.corr().style.background_gradient()


# In[9]:


sns.heatmap(df_all_close.corr(), annot=True);


# In[10]:


df_all_close.corr().hvplot(title='Returns Correlation', xlabel='Ticker', ylabel='Correlation')


# In[11]:


df_all_vol.corr().style.background_gradient()


# In[12]:


sns.heatmap(df_all_vol.corr(), annot=True);


# In[13]:


df_all_vol.corr().hvplot(title='Volume Correlation', xlabel='Ticker', ylabel='Correlation')


# In[14]:


px.scatter(
    df_all_close,
    x=df_all_close.index,
    y=['BTC_Close', 'ETH_Close', 'LTE_Close', 'XRP_Close', 'DIA_close', 'SPY_close', 'IWM_close', 'GLD_close'],
    title='Average Return by Ticker',
)


# In[15]:


px.scatter(
    df_all_vol,
    x=df_all_vol.index,
    y=['BTC_Vol', 'ETH_Vol', 'LTE_Vol', 'XRP_Vol', 'DIA_volume', 'SPY_volume', 'IWM_volume', 'GLD_volume'],
    title='Average Volume by Ticker',
)


# In[16]:


initial_investment = 10_000
cumulative_pnl = round(initial_investment * df_all_close, 2)
cumulative_pnl.tail()


# In[17]:


cumulative_pnl.hvplot(
    figsize=(20, 10),
    title='SImulated Daily Returns of a $10,000 investment'
).opts(yformatter='%.0f')


# In[18]:


total_rtn = cumulative_pnl.iloc[-1]
total_rtn.plot.barh(figsize=(15, 5), title='Simulated Daily Returns of a $10,000 investment', stacked=True);


# In[20]:


print(f"If you invested $10,000 on March 9th, 2017, your investment today would be worth:")
print(f"--------------------")
for i in ['BTC_Close', 'ETH_Close', 'LTE_Close', 'XRP_Close', 'DIA_close', 'SPY_close', 'IWM_close', 'GLD_close']:
    print(i + " " + str(total_rtn[i]))


# ---
