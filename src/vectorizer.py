from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:
    def __init__(self, corpus_texts):
        # allow underscores in tokens, so "machine_learning" is kept as one word
        self.vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b[\w]+\b")

        # turn all job roles' skill text into TF-IDF vectors (numbers)
        self.item_matrix = self.vectorizer.fit_transform(corpus_texts)

    def score_user(self, user_query_text):
        # turn the user's skills into a vector using the SAME vocabulary
        user_vector = self.vectorizer.transform([user_query_text])

        # if none of the user's words matched anything, vector is all zeros
        if user_vector.nnz == 0:
            return None  # this means "cold start", handled in recommender.py

        # compare user vector against every job role vector
        scores = cosine_similarity(user_vector, self.item_matrix).flatten()
        return scores