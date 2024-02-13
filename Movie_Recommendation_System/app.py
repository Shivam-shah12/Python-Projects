
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# printing the first 5 rows of the dataframe
# movies_data.head()
selected_features = ['genres','keywords','tagline','cast','director']
# replacing the null valuess with null string

for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
# converting the text data to feature vectors

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
# getting the similarity scores using cosine similarity

similarity = cosine_similarity(feature_vectors)
# getting the movie name from the user

movie_name = input(' Enter your favourite movie name : ')
# creating a list with all the movie names given in the dataset

list_of_all_titles = movies_data['title'].tolist()
close_match = find_close_match[0]
# finding the index of the movie with title

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
# getting a list of similar movies

similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

# print the name of similar movies based on the index

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1
def recommend(movie_name):
  list_of_all_titles = movies_data['title'].tolist()

  find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

  close_match = find_close_match[0]

  index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

  similarity_score = list(enumerate(similarity[index_of_the_movie]))

  sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

  print('Movies suggested for you : \n')

  i = 1

  for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index==index]['title'].values[0]
    if (i<30):
      print(i, '.',title_from_index)
      i+=1
