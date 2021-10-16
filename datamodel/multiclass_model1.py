import pandas as pd
import json
import re
import nltk
import string
import swifter

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


from textblob import TextBlob

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
  
    
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import FeatureUnion
from sklearn.feature_extraction import DictVectorizer
    


filename="News_Category_Dataset_v2.json"

nltk.download('wordnet')

# Read Json file
df_news = pd.read_json(filename, lines=True)

# Check Columns
# df_news.columns

df_news['text'] = df_news['headline'] + df_news['short_description']

def Preprocessing(text):
    clean_text=[]
    clean_text2=[]
    text = re.sub("'","",text) #remove apostrophe
    text = re.sub("(\\d|\\W)+"," ",text)
    clean_text = [wn.lemmatize(word, pos="v") for word in word_tokenize(text.lower()) if black_txt(word)]
    clean_text2 = [word for word in clean_text if black_txt(word)]
    return " ".join(clean_text2)

stop_words_ = set(stopwords.words('english'))
wn = WordNetLemmatizer()
my_sw = ['make', 'amp',  'news','new' ,'time', 'u','s', 'photos',  'get', 'say']

def black_txt(token):
    return  token not in stop_words_ and token not in list(string.punctuation)  and len(token)>2 and token not in my_sw

# Next we are going to create some news variables columns (like metadata) to try to improve the quality of our classifier 
# with the help of textblob package, we will create

# Polarity: to check the sentiment of the text
# Subjectivity: to check if text is objective or subjective
# Len: The number of word in the text


def subj_txt(text):
    return  TextBlob(text).sentiment[1]

def polarity_txt(text):
    return TextBlob(text).sentiment[0]

def len_text(text):
    if len(text.split())>0:
         return len(set(Preprocessing(text).split()))/ len(text.split())
    else:
         return 0

df_news['text'] = df_news['headline']  +  " " + df_news['short_description']

df_news['text'] = df_news['text'].swifter.apply(Preprocessing)
df_news['polarity'] = df_news['text'].swifter.apply(polarity_txt)
df_news['subjectivity'] = df_news['text'].swifter.apply(subj_txt)
df_news['len'] = df_news['text'].swifter.apply(lambda x: len(x))

#Label Encoding

X = df_news[['text', 'polarity', 'subjectivity','len']]
y =df_news['category']

encoder = LabelEncoder()
y = encoder.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
v = dict(zip(list(y), df_news['category'].to_list()))

#Traing the Model

text_clf = Pipeline([('vect', CountVectorizer(analyzer="word", stop_words="english")),('tfidf', TfidfTransformer(use_idf=True)),('clf', MultinomialNB(alpha=.01))])

text_clf.fit(x_train['text'].to_list(), list(y_train))

# Saving the Model

import pickle
with open('model.pkl','wb') as f:
    pickle.dump(text_clf,f)

# load
with open('model.pkl', 'rb') as f:
    clf2 = pickle.load(f)

def predict(text):
	predicted = clf2.predict(text)
	return v[predicted[0]]



