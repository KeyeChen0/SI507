import requests
import json
import os
import pandas as pd

def get_data_from_API():
    api_key = '44c2928e'
    movie = input('Enter a movie title: ')
    if not os.path.exists('cache.json'):
        with open('cache.json', 'w') as f:
            json.dump({}, f)
    with open('cache.json', 'r') as f:
        data = json.load(f)
    if movie in data:
        return data[movie]
    else:
        url = f'http://www.omdbapi.com/?t={movie}&apikey={api_key}'
        response = requests.get(url)
        new_data = response.json()
        data[movie] = new_data
        with open('cache.json', 'w') as f:
            json.dump(data, f)
        return new_data


def read_data_from_csv():
    df_movie_metadata = pd.read_csv('movie_metadata.csv')
    df_credit = pd.read_csv('credits.csv')
    return df_movie_metadata, df_credit



get_data_from_API()
