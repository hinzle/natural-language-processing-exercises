# current filepath system leaves plenty to be desired
import sys
local_path = '/Users/hinzlehome/codeup-data-science/natural-language-processing-exercises/utils/imports.py'
sys.path.insert(0, local_path)

# imports.py in /utils/
from utils.imports import *
from utils.acquire import *

def basic_clean(original):
	'''
	takes an original string and outputs a tidy "article"
	'''
	article=original.lower()
	article = unicodedata.normalize('NFKD', article).encode('ascii', 'ignore').decode('utf-8', 'ignore')
	article = re.sub(r"[^a-z0-9'\s]", '', article)
	return article

def tokenize(article):
	'''
	tokenizes an "article"
	'''
	tokenizer = nltk.tokenize.ToktokTokenizer()
	article_token=tokenizer.tokenize(article, return_str=True)
	return article_token


def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string

def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string

def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))

    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

def prep_article_data(df, column, extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['stemmed'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(stem)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df['lemmatized'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(lemmatize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    return df[['title', column,'clean', 'stemmed', 'lemmatized']]


def prepare_df(df, extra_words = [], exclude_words = []):
    """Adds columns for cleaned, stemmed, and lemmatized data in dataframe """
    # Create cleaned data column of content
    df['clean'] = df.content.apply(basic_clean).apply(tokenize).apply(remove_stopwords,
                                                       extra_words = extra_words,
                                                       exclude_words = exclude_words)
    
    # Create stemmed column with stemmed version of cleaned data
    df['stemmed'] = df.clean.apply(tokenize).apply(stem).apply(remove_stopwords,
                                                       extra_words = extra_words,
                                                       exclude_words = exclude_words)

    # Create lemmatized column with lemmatized version of cleaned data
    df['lemmatized'] = df.clean.apply(tokenize).apply(lemmatize).apply(remove_stopwords,
                                                       extra_words = extra_words,
                                                       exclude_words = exclude_words)
    
    return df
    

def create_prepared_news_df(extra_words =[], exclude_words = []):
    """Run this function to generate a prepared news article dataframe with cleaned, stemmed, and lemmatized data"""
    news_df = pd.DataFrame(get_news_articles())
    
    return prepare_df(news_df, extra_words, exclude_words)
    
def create_prepared_blog_df(extra_words =[], exclude_words = []):
    """Run this function to generate a prepared Codeup Blog dataframe with cleaned, stemmed, and lemmatized data"""

    codeup_df = pd.DataFrame(get_blog_articles())
    
    return prepare_df(codeup_df, extra_words, exclude_words)
    
    
def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test