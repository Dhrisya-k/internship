import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Key
api_key = "21297afe92c04e62984cbc5eb3f4321d"

# URL
url = f"https://newsapi.org/v2/top-headlines?category=politics&country=us&pageSize=10&apiKey={api_key}"

# Request data
response = requests.get(url)

# Convert to JSON
data = response.json()

# Correct key
articles = data["articles"]

news_list = []

# Extract data
for article in articles:

    news_list.append({
        "Title": article["title"],
        "Source": article["source"]["name"]
    })

# Create DataFrame
df = pd.DataFrame(news_list)

# Print data
print(df)

# Count sources
source_count = df["Source"].value_counts()

# Plot graph
plt.figure(figsize=(10,5))

source_count.plot(kind="bar")

plt.title("Top Political News Sources")
plt.xlabel("Source")
plt.ylabel("Number of Articles")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()