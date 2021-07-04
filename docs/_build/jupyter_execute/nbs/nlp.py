#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

from collections import Counter
from datetime import datetime, timedelta
from dotenv import find_dotenv, get_key
import json
import re

import numpy as np
import pandas as pd
from pylab import mpl, plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import alpaca_trade_api as tradeapi
alpaca_api_key = 'PKKSFLVI3BMIRQBN6C2K'
alpaca_secret_key = 'sW1fFZmq9HZwyL5p6OkFrJbr2TFq1H5IJ2njVLik'
api = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version='v2')

from newsapi import NewsApiClient
#from newsapi.newsapi_client import NewsApiClient
api_key = '87dec3a300674a8a87b91a1da6ab30be'
newsapi = NewsApiClient(api_key=api_key)

import nltk
from nltk.corpus import inaugural, reuters, stopwords
#stopwords.words('english')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.util import ngrams
from wordcloud import WordCloud

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
tone_api = '0R866-tePJfMWni9gl454-jWDOS44kvX12Te4KZFe6Wr'
tone_url = 'https://api.us-east.tone-analyzer.watson.cloud.ibm.com/instances/fc8d2c71-5116-43ab-8c9a-de4a584aa663'

import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')


# ---

# NLP Natural Language Processing<br>
# &nbsp;&nbsp;&nbsp;&nbsp;
# Preprocessing<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# Tokenization<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# Lemmatization<br>
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# Stopwording<br>
# &nbsp;&nbsp;&nbsp;&nbsp;
# Extraction<br>
# &nbsp;&nbsp;&nbsp;&nbsp;
# Analysis<br>
# &nbsp;&nbsp;&nbsp;&nbsp;
# Representation<br>
# 
# Frequency Analysis<br>
# Counting tokens<br>
# Ngram<br>
# Word Cloud<br>
# 
# Text Modeling<br>
# Sentiment Analysis<br>
# Tone Analysis<br>
# 
# https://docs.python.org/3/library/re.html<br>
# https://spacy.io/api/data-formats<br>
# https://spacy.io/api/data-formats#pos-tagging<br>

# ---

# In[2]:


reuters.categories()


# ---

# In[3]:


def process_text (article):
    sw = set(stopwords.words('english'))
    sw_addons = {'said', 'sent', 'found', 'including', 'today', 'announced', 'week', 'basically', 'also'}
    regex = re.compile('[^a-zA-Z ]')
    re_clean = regex.sub('', article)
    words = word_tokenize(re_clean)
    lemmatizer = WordNetLemmatizer()
    lem = [lemmatizer.lemmatize(word) for word in words]
    output = [word.lower() for word in lem if word.lower() not in sw.union(sw_addons)]
    return output
def process_text_bg (doc):
    sw_words = process_text(doc)
    bigrams = ngrams(sw_words, 2)
    output = ['_'.join(i) for i in bigrams]
    return output
def word_counter (corpus):
    ''' Combine all articles in corpus into one large string. '''
    big_string = ' '.join(corpus)
    processed = process_text(big_string)
    top_10 = dict(Counter(processed).most_common(10))
    return pd.DataFrame(list(top_10.items()), columns=['word', 'count'])
def bigram_counter (corpus):
    ''' Combine all articles in corpus into one large string. '''
    big_string = ' '.join(corpus)
    processed = process_text(big_string)
    bigrams = ngrams(processed, n=2)
    top_10 = dict(Counter(bigrams).most_common(10))
    return pd.DataFrame(list(top_10.items()), columns=['bigram', 'count'])


# In[4]:


ids = reuters.fileids(categories='gas')
corpus = [reuters.raw(i) for i in ids]
display(
    word_counter(corpus),
    bigram_counter(corpus),
)

sentence_tokenized = [sent_tokenize(i) for i in corpus]

word_tokenized = []
for story in sentence_tokenized:
    words = []
    for sent in story:
        words = words + word_tokenize(sent)
    word_tokenized.append(words)

reuters_cpi = pd.DataFrame({'articles': corpus,
                            'sentence_tokenized': sentence_tokenized,
                            'word_tokenized': word_tokenized})
reuters_cpi.index = ids
reuters_cpi.head()


# In[5]:


wc = WordCloud(background_color='white').generate(' '.join(process_text(' '.join(corpus))))
plt.figure(figsize=(10, 8));
plt.imshow(wc, interpolation='bilinear');
plt.axis('off');
plt.title('');


# In[6]:


plt.figure(figsize=(10, 8));
wc = WordCloud(background_color='white').generate(' '.join(process_text_bg(' '.join(corpus))))
plt.imshow(wc, interpolation='bilinear');
plt.axis('off');
plt.title('');


# ---

# In[7]:


authenticator = IAMAuthenticator(tone_api)
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator,
)
tone_analyzer.set_service_url(tone_url)

text = """
Team, I know that times are tough!
Product sales have been disappointing for the past three quarters.
We have a competitive product, but we need to do a better job of selling it!
"""

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json',
    content_language='en',
    accept_language='en',
).get_result()
print(json.dumps(tone_analysis, indent=2))

doc_tone_df = pd.json_normalize(data=tone_analysis['document_tone'], record_path=['tones'])
doc_tone_df

sentences_tone_df = pd.json_normalize(
    data=tone_analysis['sentences_tone'],
    record_path=['tones'],
    meta=['sentence_id', 'text'],
)
sentences_tone_df

utterances = [
    {"text": "Hello, I'm having a problem with your product.", "user": "customer"},
    {"text": "OK, let me know what's going on, please.", "user": "agent"},
    {"text": "Well, nothing is working :(", "user": "customer"},
    {"text": "Sorry to hear that.", "user": "agent"},
]
utterance_analysis = tone_analyzer.tone_chat(
    utterances=utterances, content_language='en', accept_language='en',
).get_result()
print(json.dumps(utterance_analysis, indent=2))

chat_tone_df = pd.json_normalize(
    data=utterance_analysis['utterances_tone'],
    record_path=['tones'],
    meta=['utterance_id', 'utterance_text'],
)
chat_tone_df


# ---

# In[8]:


def retrieve_docs (terms):
    result_docs = []
    for doc_id in money_news_ids:
        found_terms = [
            word
            for word in reuters.words(doc_id)
            if any(term in word.lower() for term in terms)
        ]
        if len(found_terms) > 0:
            result_docs.append(doc_id)
    return result_docs

def create_df (news, language):
    """
    Transforms the articles into a DataFrame.
    
    Parameters
    ==========
    news [list]: the list of articles
    language [string]: specifies the language of the articles
    """
    articles = []
    for article in news:
        try:
            title = article['title']
            description = article['description']
            text = article['content']
            date = article['publishedAt'][:10]
            articles.append({
                'title': title,
                'description': description,
                'text': text,
                'date': date,
                'language': language,
            })
        except AttributeError:
            pass
    return pd.DataFrame(articles)

crisis_news_en = newsapi.get_everything(q='financial crisis 2008', language='en')
crisis_news_en['totalResults']

crisis_news_fr = newsapi.get_everything(q='financière crise 2008', language='fr')
crisis_news_fr['totalResults']

crisis_en_df = create_df(crisis_news_en['articles'], 'en')
crisis_fr_df = create_df(crisis_news_fr['articles'], 'fr')
crisis_df = pd.concat([crisis_en_df, crisis_fr_df])
crisis_df.tail()

crisis_df.to_csv('./crisis_news_en_fr.csv', index=False, encoding='utf-8-sig')


# ---

# In[9]:


analyzer = SentimentIntensityAnalyzer()
libra_headlines = newsapi.get_everything(
    q='facebook libra',
    language='en',
    page_size=100,
    sort_by='relevancy',
)
libra_sentiments = []
for article in libra_headlines['articles']:
    try:
        text = article['content']
        date = article['publishedAt'][:10]
        sentiment = analyzer.polarity_scores(text)
        compound = sentiment['compound']
        pos = sentiment['pos']
        neu = sentiment['neu']
        neg = sentiment['neg']
        libra_sentiments.append({
            'text': text,
            'date': date,
            'compound': compound,
            'positive': pos,
            'negative': neg,
            'neutral': neu,
        })
    except AttributeError:
        pass
libra_df = pd.DataFrame(libra_sentiments)
cols = ['date', 'text', 'compound', 'positive', 'negative', 'neutral']
libra_df = libra_df[cols]
libra_df.head()


# ---

# In[10]:


categories = ['money-fx', 'money-supply']
all_docs_id = reuters.fileids()
money_news_ids = [
    doc
    for doc in all_docs_id
    if categories[0] in reuters.categories(doc)
    or categories[1] in reuters.categories(doc)
]
money_news = [reuters.raw(doc).lower() for doc in money_news_ids]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(money_news)
money_news_df = pd.DataFrame(
    list(zip(vectorizer.get_feature_names(), np.ravel(X.sum(axis=0)))),
    columns=['Word', 'Frequency'],
)
money_news_df = money_news_df.sort_values(by=['Frequency'], ascending=False)
money_news_df.head()

top_words = money_news_df[(money_news_df['Frequency'] >= 10) & (money_news_df['Frequency'] <= 30)]
top_words.head()

terms_list = str(top_words['Word'].tolist())
wordcloud = WordCloud(colormap='RdYlBu', background_color='white').generate(terms_list)
plt.imshow(wordcloud, interpolation='bilinear');
plt.axis('off');
plt.title('Money News Word Cloud', fontdict={'fontsize': 20, 'fontweight': 'bold'});

len(retrieve_docs(['yen']))
len(retrieve_docs(['japan', 'banks']))
len(retrieve_docs(['england', 'dealers']))


# ---

# In[11]:


doc_ids = reuters.fileids()
len(doc_ids)

doc_id = 'test/15045'
doc_text = reuters.raw(doc_id)
doc_text

vectorizer = CountVectorizer(stop_words='english')
vectorizer

X = vectorizer.fit_transform([doc_text])
print(X)

words = vectorizer.get_feature_names()
words

words_df = pd.DataFrame(list(zip(words, np.ravel(X.sum(axis=0)))), columns=['Word', 'Word_Count'])
words_df



all_docs_id = reuters.fileids()
corpus_id = all_docs_id[:1000]
corpus = [reuters.raw(doc) for doc in corpus_id]
vectorizer = TfidfVectorizer(stop_words='english')
X_corpus = vectorizer.fit_transform(corpus)
words_corpus = vectorizer.get_feature_names()
words_corpus_df = pd.DataFrame(list(zip(words_corpus, np.ravel(X_corpus.mean(axis=0)))), columns=['Word', 'TF-IDF'])
words_corpus_df = words_corpus_df.sort_values(by=['TF-IDF'], ascending=False)
words_corpus_df


# ---

# In[12]:


def get_headlines (keyword):
    all_headlines = []
    all_dates = []
    date = datetime.strptime(current_date[:10], '%Y-%m-%d')
    end_date = datetime.strptime(past_date[:10], '%Y-%m-%d')
    print(f'Fetching news about \'{keyword}\'')
    print('*' * 30)
    while date > end_date:
        print(f'retrieving news from: {date}')
        articles = newsapi.get_everything(
            q=keyword,
            from_param=str(date)[:10],
            to=str(date)[:10],
            language='en',
            sort_by='relevancy',
            page=1,
        )
        headlines = []
        for i in range(0, len(articles['articles'])):
            headlines.append(articles['articles'][i]['title'])
        all_headlines.append(headlines)
        all_dates.append(date)
        date = date - timedelta(days=1)
    return all_headlines, all_dates

def headline_sentiment_summarizer_avg (headlines):
    sentiment = []
    for day in headlines:
        day_score = []
        for h in day:
            if h == None:
                continue
            else:
                day_score.append(sid.polarity_scores(h)['compound'])
        sentiment.append(sum(day_score) / len(day_score))
    return sentiment


# ---

# In[13]:


ticker = 'AAPL'
timeframe = '1D'
current_date = pd.Timestamp(datetime.now(), tz='America/New_York').isoformat()
past_date = pd.Timestamp(datetime.now() - timedelta(30), tz='America/New_York').isoformat()
df = api.get_barset(
    ticker,
    timeframe,
    limit=None,
    start=past_date,
    end=current_date,
    after=None,
    until=None,
).df
df.head()


# In[52]:


df = df.droplevel(axis=1, level=0)
df = df.drop(columns=['open', 'high', 'low', 'volume'])
df.index = df.index.date
df.head()


# In[53]:


aapl_returns = df.pct_change().dropna()
aapl_returns.head()


# In[55]:


aapl_headlines, dates = get_headlines('apple')
trade_headlines, _ = get_headlines('trade')
economy_headlines, _ = get_headlines('economy')


# In[58]:


sid = SentimentIntensityAnalyzer()

aapl_avg = headline_sentiment_summarizer_avg(aapl_headlines)
trade_avg = headline_sentiment_summarizer_avg(trade_headlines)
economy_avg = headline_sentiment_summarizer_avg(economy_headlines)

topic_sentiments = pd.DataFrame({'aapl_avg': aapl_avg, 'trade_avg': trade_avg, 'economy_avg': economy_avg})
topic_sentiments.index = pd.to_datetime(dates)
topic_sentiments = aapl_returns.join(topic_sentiments).dropna(how='any')
topic_sentiments


# In[59]:


topic_sentiments.corr().style.background_gradient()


# ---

# In[45]:


article = reuters.raw(fileids = reuters.fileids(categories='gas')[0])
doc = nlp(article)
displacy.render(doc, style='ent')


# In[46]:


articles = reuters.raw(categories='gas')
doc = nlp(articles)
entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'ORG']]
entities = [i.lower().replace(' ', '_') for i in entities]
wc = WordCloud().generate(' '.join(entities))
plt.imshow(wc);


# ---

# In[39]:


doc = nlp(u'Michael Jordan was a player in the National Basketball Association.')
for ent in doc.ents:
    print('{:40}{:40}'.format(ent.text, ent.label_))


# In[43]:


article = reuters.raw(fileids = reuters.fileids(categories='yen')[1])
doc = nlp(article)
print([ent.text for ent in doc.ents if ent.label_ == 'GPE'])
displacy.render(doc, style='ent')


# ---

# In[33]:


def most_freq_adj (text):
    """ This function uses spaCy to get the most common adjectives from each text.
    
    Parameters
    ==========
      text (string): The text to analyze
    
    Returns
    =======
      most_common_adj (list): A list containing a tuple with the most common adjective and its occurrence in the text
    """
    
    # Tokenizes text and parses each token
    doc = nlp(text)
    
    # Creates a list with all the adjectives in the text
    adjs = [token.text.lower() for token in doc if token.pos_ == 'ADJ']
    
    # Retrieves the most frequent adjective in the `adjs` list using the Counter module
    most_common_adj = Counter(adjs).most_common(1)
    
    return most_common_adj

def all_adj (text):
    """ This function retrieves all the adjectives on the given text.
    
    Parameters
    ==========
      text (string): The text to analyze.
      
    Returns
    =======
      adjs (string): A list with all the adjectives in the text
    """
    
    # Tokenize the text and parse each token
    doc = nlp(text)
    
    # Create a list with all the adjectives in the text
    adjs = [token.text.lower() for token in doc if token.pos_ == 'ADJ']
    
    return adjs

def get_word_counts (text, word):
    """ This function counts the occurrences of a word in a text.
    
    Parameters
    ==========
      text (string): The text where word counts will be analyzed
      word (string): The word to look into the text
      
    Returns
    =======
      word_count (int): The counts of the word in the given text
    """
    
    # Use the word_tokenize module from NLTK to tokenize the text
    tok = word_tokenize(text)
    
    # Create a list with all the tokens retrieved from the text
    tok = [word.lower() for word in tok]
    
    # Count the occurrences of the word in the text
    word_count = tok.count(word)
    
    return word_count

def describe_america (text):
    """ This function retrieves the adjectives in the text that describe the word 'America'.
    Parameters
      text (string): The text to analyze.
    Returns
      adjs (list): A list of the adjectives that describe the word 'America' in the text.
    """
    
    # Use the spaCy English language model to tokenize the text and parse each token
    doc = nlp(text)
    
    # Create a list with all the adjectives in the text that describe the word 'America'
    adjs = [token.text.lower() for token in doc if (token.pos_ == 'ADJ' and token.head.text == 'America')]
    
    return adjs


# In[25]:


ids = inaugural.fileids()
texts = [inaugural.raw(id) for id in ids]
adjs = [most_freq_adj(text) for text in texts]
df_adjs = pd.DataFrame({'doc_id': ids, 'adjective': adjs})
df_adjs.head()


# In[32]:


all_adjectives = []
for text in texts:
    all_adjectives = all_adjectives + all_adj(text)
most_freq_adjectives = Counter(all_adjectives).most_common(3)
great_counts = [get_word_counts(text, 'great') for text in texts]
other_counts = [get_word_counts(text, 'other') for text in texts]
own_counts = [get_word_counts(text, 'own') for text in texts]
dates = [id.split('-')[0] for id in ids]
presidents = [id.split('-')[1].split('.')[0] for id in ids]
adjectives_data = {'president': presidents, 'great': great_counts, 'other': other_counts, 'own': own_counts}
df_adjectives = pd.DataFrame(adjectives_data, index=pd.to_datetime(dates).year)
df_adjectives.head()


# In[34]:


df_adjectives.plot(
    title='Most Common Adjectives Used in the U.S. Presidential Inaugural Addresses',
    figsize=(10, 5),
);


# In[35]:


america_adjectives = []
for text in texts:
    america_adjectives = america_adjectives + describe_america(text)
america_adjectives


# ---

# In[16]:


def parser (s):
    tokens = nlp(s)
    l = []
    for token in tokens:
        l.append('{:20}{:20}{:20}{:20}'.format(token.text, token.pos_, token.dep_, token.head.text))
    return l


# In[18]:


s1 = 'The brown cow jumped over the round moon.'
s2 = 'Jose made a book collector happy the other day.'
res = parser(s2)
for line in res:
    print(line)


# In[10]:


nouns = [token.text for token in tokens if token.pos_ == 'NOUN']
cow_describers = [token.text for token in tokens if (token.head.text == 'cow' and token.pos_ == 'ADJ')]
display(
    nouns,
    cow_describers,
)


# In[7]:


displacy.render(tokens, style='dep')


# ---
