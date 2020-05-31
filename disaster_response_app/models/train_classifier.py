import sys
import pandas as pd
from sqlalchemy import create_engine

import re
import nltk
nltk.download(['stopwords', 'wordnet', 'punkt'])
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from sklearn.datasets import make_multilabel_classification
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline#, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import pickle

def load_data(database_filepath):
    engine = create_engine("sqlite:///{}".format(database_filepath))
    df = pd.read_sql("SELECT * FROM messages_categorized", engine)
    X = df.message
    Y = df.loc[:,'related':]
    category_names = list(Y.columns)
    
    return X, Y, category_names


def tokenize(text):
    '''A custom tokenizer function.
    
    INPUT:
        text: string to be tokenized
        
    RETURN:
        tokens: a list of tokens    
    '''
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # tokenize text
    tokens = word_tokenize(text)

    # lemmatize and remove stop words
    stop_words = stopwords.words("english")
    tokens = [WordNetLemmatizer().lemmatize(word) for word in tokens if word not in stop_words]
    
    return tokens


def build_model():
    '''Define the ML pipeline and set parameters for grid search.
    
    RETURN:
        model_pipeline: modela training pipeline
    '''
    classifier_pipe = Pipeline([
        ('preprocessing', TfidfVectorizer(tokenizer=tokenize)),
         
#         ('clf', MultiOutputClassifier(RandomForestClassifier()))
        ('clf', MultiOutputClassifier(KNeighborsClassifier()))
    ])
    
    parameters = {
        'preprocessing__use_idf': [True, False],
        'clf__estimator__n_neighbors': [15, 45]
    }
    
    model_pipeline = GridSearchCV(classifier_pipe, param_grid=parameters, verbose=10)
    
    return model_pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    '''Output model evaluation results
    '''
    Y_pred = pd.DataFrame(model.predict(X_test))
    
    i = 0
    for i, _ in enumerate(Y_test):
        print('Clasification report for:',Y_test.columns[i])
        print(classification_report(Y_test.iloc[:,i], Y_pred.iloc[:,i]))
    
    print(model.best_params_)


def save_model(model, model_filepath):
    ''' Save the model as a pickle file
    '''
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()