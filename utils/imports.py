# env
import sys
local_path = '/Users/hinzlehome/codeup-data-science/binance-project/'
sys.path.insert(0,local_path+'.env')
from env import *
# # used for trouble shooting filepath issues
# import os
# print(os.getcwd())
# # used for trouble shooting large notebooks
# jupyter nbconvert --clear-output explore.ipynb
# jupyter nbconvert --inplace --execute explore.ipynb
# jupyter nbconvert --to python explore.ipynb

# local-host
import unicodedata, itertools, re, requests, math, random, os, datetime, json, pprint

# python data science library's
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import Holt
from scipy import stats
# from pydataset import data

# sklearn optimizer for intel chip
from sklearnex import patch_sklearn
# $ conda install scikit-learn-intelex
# $ python -m sklearnex my_application.py
patch_sklearn()

# sci-kit-learn modules
from sklearn import metrics 
	# (
	# confusion_matrix,accuracy_score,precision_score,recall_score,
	# classification_report,mean_squared_error,r2_score,explained_variance_score
	# )
from sklearn.cluster import KMeans, DBSCAN
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.feature_selection import SelectKBest, RFE, f_regression
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression, LinearRegression, LassoLars, TweedieRegressor
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer, PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

# visualizations
from pandas.plotting import register_matplotlib_converters

# matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D

# seaborn
import seaborn as sns

# wordcloud
from wordcloud import WordCloud

# binance modules
import websocket, talib
from binance.client import Client
from binance.enums import *

# facebook "prophet"
from prophet import Prophet

# beautifulsoup
from bs4 import BeautifulSoup

#natural language toolkit
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

# state properties
np.random.seed(123)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)