
# author: mujtaba
# date: july 30, 2023

# This script generates clusters from the given dataset (found in /data/ folder) and saves them in /clusters/ folder

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans

def cluster_strings(strings, k):
    # Step 1: Calculate the cosine similarity matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(strings)
    cosine_sim_matrix = cosine_similarity(tfidf_matrix)

    # Step 2: Perform K-Means clustering on the cosine similarity matrix
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(cosine_sim_matrix)

    # Step 3: Create k smaller sets
    clusters = {}
    for i, label in enumerate(kmeans.labels_):
        if label not in clusters:
            clusters[label] = []
        clusters[label].append(strings[i])

    return list(clusters.values())

# Example usage
huge_set_of_strings = [
    "kiwi apple",
    "orange grapefruit",
    "mango pineapple",
    "watermelon honeydew",
    "banana pear",
    "strawberry blueberry raspberry",
    "cherry plum",
    "lemon lime",
    "coconut",
    "peach apricot",
    "papaya",
    "guava",
    "persimmon",
    "dragonfruit",
    "passionfruit",
    "blackberry",
    "cranberry",
    "date",
    "fig",
    "kiwi",
    "tangerine",
    "nectarine",
    "kiwi pineapple",
    "kiwi strawberry",
    "grapefruit lime",
    "lemon orange",
    "papaya mango",
    "pear apple",
    "orange tangerine",
    "watermelon cantaloupe",
    "apricot peach",
    "persimmon plum",
    "blueberry raspberry",
    "pineapple mango",
    "kiwi strawberry",
    "lemon lime",
    "lime lemon",
    "coconut pineapple",
    "blueberry raspberry",
    "blackberry raspberry",
    "cranberry blueberry",
    "kiwi watermelon",
    "grapefruit tangerine",
    "orange tangerine",
    "lemon lime",
    "watermelon cantaloupe",
    "pineapple mango",
    "blackberry raspberry",
]

# Call the clustering function again with the updated set of strings
k = 3  # Number of resulting sets
resulting_sets = cluster_strings(huge_set_of_strings, k)

# Print the resulting sets
for i, smaller_set in enumerate(resulting_sets):
    print(f"Set {i + 1}: {smaller_set}")
