import time

# import pandas as pd
# import numpy as np
# import warnings
# warnings.filterwarnings('ignore')
# import gzip
# import json
# import re
# import os
# from pickle import dump, load
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# csv_file_path = 'df_books_processed_1.csv.gz'
# chunk_size = 10000
# df_books_processed = pd.DataFrame()
# chunks = pd.read_csv(csv_file_path, chunksize=chunk_size)
# for chunk in chunks:
#     df_books_processed = pd.concat([df_books_processed, chunk], ignore_index=True)
# # df_books_processed = pd.read_csv('df_books_processed_1.csv.gz')
# with open("vectorizer_description.pkl", "rb") as p:
#     vectorizer_description = load(p)

# warnings.filterwarnings("ignore")
# import re
# from pickle import dump, load
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# df_books_processed = pd.read_csv("df_books_processed_1.csv.gz")

# with open("vectorizer_description.pkl", "rb") as p:
#     vectorizer_description = load(p)

# with open("tfidf_description.pkl", "rb") as p:
#     tfidf_description = load(p)


def search(query):
    # processed = re.sub("[^a-zA-Z0-9 ]", "", query.lower())
    # query_vec = vectorizer_description.transform([query])
    # similarity = cosine_similarity(query_vec, tfidf_description).flatten()

    # indices = np.argpartition(similarity, -10)[-10:]

    # results = pd.DataFrame(
    #     {
    #         "book_id": df_books_processed["book_id"].iloc[indices],
    #         "similarity_score": similarity[indices],
    #     }
    # )

    # results = results.sort_values(by="similarity_score", ascending=False).head(10)

    # results = pd.merge(results, df_books_processed, on="book_id")

    # return results[["book_id", "title_without_series"]]

    #  wait for 5 seconds then return true

    time.sleep(5)

    return {"book_id": query}
