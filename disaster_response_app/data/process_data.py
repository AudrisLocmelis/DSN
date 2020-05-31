import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''Load disaster response data into messages and categories dataframes.
    
    INPUT:
        messages_filepath: path to the messages data csv file
        categories_filepath: path to the categories data csv file
    
    RETURN:
        dataframes for messages and categories
    '''
    try:
        messages = pd.read_csv(messages_filepath)
    except:
        print("Error: can not find file or read data from", messages_filepath)
    else:
        print("Successfuly read messages file", messages_filepath)
    
    try:
        categories = pd.read_csv(categories_filepath)
    except:
        print("Error: can not find file or read data from", categories_filepath)
    else:
        print("Successfuly read categories file", categories_filepath)
        
    return messages, categories


def left_of_dash(chars):
    '''Return the characters left of a dash "-" in a string.'''
    return chars.split('-')[0]

def clean_data(df):
    '''Clean the messages and categories data
    
    INPUT:
        df: consists of two dataframes messages and categories
    
    RETURN:
        df: a merged an cleaned dataframe
    '''
    messages, categories = df
    
    # Drop duplicates and merge
    messages.drop_duplicates(inplace=True)
    categories.drop_duplicates(inplace=True)
    categories.drop_duplicates(['id'], keep='last', inplace=True)
    
    df = messages.merge(categories, how='inner',on='id', )
    
    # Create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(';', expand=True)
    
    # Extract a list of new column names and rename categories
    row = categories.iloc[0,:]
    category_colnames = row.apply(left_of_dash)
    categories.columns = category_colnames
    
    # Convert category values to 0 or 1
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: int(x[-1:]))
    
    # Replace categories column in df with new category columns
    df = df.drop(columns='categories')
    df = pd.concat([df, categories], axis=1, sort=False)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    return df


def save_data(df, database_filename): #='/home/workspace/data/disaster_response.db'):
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('messages_categorized', engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        print(df.shape)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()