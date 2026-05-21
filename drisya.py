import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
movies = pd.read_csv("archive/tmdb_5000_movies.csv")

# 1. Top Revenue Movies
print("\nTOP REVENUE MOVIES\n")

top_revenue = movies[['title', 'revenue']].sort_values(
    by='revenue',
    ascending=False
).head(10)

print(top_revenue)

# 2. Profit Analysis
print("\nMOST PROFITABLE MOVIES\n")

movies['profit'] = movies['revenue'] - movies['budget']

top_profit = movies[['title', 'profit']].sort_values(
    by='profit',
    ascending=False
).head(10)

print(top_profit)

# 3. Most Popular Movies
print("\nMOST POPULAR MOVIES\n")

popular = movies[['title', 'popularity']].sort_values(
    by='popularity',
    ascending=False
).head(10)

print(popular)

# 4. Highest Rated Movies
print("\nHIGHEST RATED MOVIES\n")

rated = movies[['title', 'vote_average', 'vote_count']]

rated = rated[rated['vote_count'] > 1000]

top_rated = rated.sort_values(
    by='vote_average',
    ascending=False
).head(10)

print(top_rated)

# 5. Movie Release Trend
movies['release_date'] = pd.to_datetime(movies['release_date'])

movies['year'] = movies['release_date'].dt.year

yearly = movies['year'].value_counts().sort_index()

print("\nMOVIES RELEASED EACH YEAR\n")

print(yearly)

# Graph
yearly.plot(figsize=(12,5))

plt.title("Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")

plt.show()