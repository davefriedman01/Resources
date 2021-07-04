#!/usr/bin/env python
# coding: utf-8

# ### Data Types in Python

# In[1]:


from typing import    Callable,    Dict,    List
Array_Function = Callable[[ndarray], ndarray] # A Function takes in an ndarray as an argument and produces an ndarray
Chain = List[Array_Function]                  # A Chain is a list of functions


# ### NumPy and Pandas

# In[ ]:


import numpy as np
np.set_printoptions(suppress=True)
np.set_printoptions(precision=4)
from numpy import ndarray
import numpy.random as npr
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# ### Matplotlib and Seaborn

# In[ ]:


from pylab import mpl, plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (10, 6)


# ### SciPy

# In[ ]:


from scipy.special import softmax


# ### Scikit-Learn

# In[ ]:


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


# ### Spark

# In[ ]:


from pyspark.sql.functions import desc, max

from pyspark.ml import Pipeline
from pyspark.ml.classification import    DecisionTreeClassifier
from pyspark.ml.clustering import LDA
from pyspark.ml.evaluation import    MulticlassClassificationEvaluator
from pyspark.ml.feature import    Binarizer,    CountVectorizer,    IDF,    IndexToString,    MinMaxScaler,    NGram,    RegexTokenizer,    SQLTransformer,    StopWordsRemover,    StringIndexer,    VectorAssembler
from pyspark.ml.tuning import    CrossValidator,    ParamGridBuilder
from pyspark.sql import functions as fun, Row
from pyspark.sql.types import *

import sparknlp
from sparknlp import    DocumentAssembler,    Finisher
from sparknlp.annotator import    Lemmatizer,    LemmatizerModel,    Normalizer,    NorvigSweetingModel,    PerceptronApproach,    PerceptronModel,    SentenceDetector,    Stemmer,    SymmetricDeleteModel,    Tokenizer
from sparknlp.pretrained import PretrainedPipeline

#####
#
# this

spark = sparknlp.start()

# or this

from pyspark import SparkConf
from pyspark.sql import SparkSession
spark_conf = SparkConf()
spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()

#
#####


# ### Statsmodels

# In[ ]:


import statsmodels.api as sm
# sm.tsa.filters.hpfilter()
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
#from statsmodels.tsa.arima.model import ARIMA
import arch


# ### NLP

# In[ ]:


import nltk

from nltk import ngrams
from nltk.util import ngrams

from nltk.corpus import inaugural, reuters, stopwords
#stopwords.words('english')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer, sent_tokenize, word_tokenize
from wordcloud import WordCloud


# In[ ]:


import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


# In[ ]:


from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
tone_api = '0R866-tePJfMWni9gl454-jWDOS44kvX12Te4KZFe6Wr'
tone_url = 'https://api.us-east.tone-analyzer.watson.cloud.ibm.com/instances/fc8d2c71-5116-43ab-8c9a-de4a584aa663'


# ### API

# In[ ]:


#####
#
# python-dotenv
#
#####
from dotenv import find_dotenv, get_key

alpaca_api_key = get_key(find_dotenv(), 'ALPACA_API_KEY')
alpaca_secret_key = get_key(find_dotenv(), 'ALPACA_SECRET_KEY')

news_api_key = get_key(find_dotenv(), 'NEWSAPI_API_KEY')

quandl_api_key = get_key(find_dotenv(), 'QUANDL_API_KEY')


# In[ ]:


#####
#
# configparser
#
#####
import configparser
c = configparser.ConfigParser()
c.read('api.cfg')

alpaca_api_key = c['alpaca']['api_key']
alpaca_secret_key = c['alpaca']['secret_key']

news_api_key = c['newsapi']['api_key']

quandl_api_key = c['quandl']['api_key']


# In[ ]:


import alpaca_trade_api as tradeapi
api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version='v2',
)


# In[ ]:


import quandl as q
q.ApiConfig.api_key = quandl_api_key


# In[ ]:


from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key=news_api_key)


# ### Other

# In[ ]:


from __future__ import division
from collections import Counter, OrderedDict
from datetime import datetime, timedelta
import itertools as it
import json
from operator import add, concat, itemgetter, methodcaller
import string
import re
from time import sleep


# In[ ]:


import networkx as nx

