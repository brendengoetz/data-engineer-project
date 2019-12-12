import pandas as pd
import json
from pandas.io.json import json_normalize
import csv
import ast

# Read in only data needed for Movies table
# A more scalable workflow would automate the download frmo S3
movie_cols = [2, 5, 6, 10, 14, 15, 18, 20]
movies = pd.read_csv('the-movies-dataset/movies_metadata.csv', low_memory=False, usecols=movie_cols)

# Read in only data needed for Genres table
genre_cols = [3]
genres = pd.read_csv('the-movies-dataset/movies_metadata.csv', low_memory=False, usecols=genre_cols)

# Attempting to handle the fact that the Genres field is a list of dictionaries
# but is recognized as a literal string
with open('the-movies-dataset/movies_metadata.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        single_json = row[3]
        single_json = single_json.replace("'", '"')
        #single_json = single_json.replace("[", "{").replace("]", "}") #.split("}, ") #convert str to list
        single_json = ast.literal_eval(single_json) #convert str to list
        #data = json.load(single_json)
        #print(json.dumps(data, indent=4))
        print(single_json)
