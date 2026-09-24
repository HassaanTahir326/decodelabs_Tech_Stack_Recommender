from src.data_loader import load_job_roles, build_user_query
from src.vectorizer import SimilarityEngine


class TechStackRecommender:
    def __init__(self, csv_path=None):
        # step 1 setup: load data and build the similarity engine once
        self.df = load_job_roles(csv_path) if csv_path else load_job_roles()
        self.engine = SimilarityEngine(self.df["skills_text"].tolist())

    def recommend(self, user_skills, top_n=3):
        if len(user_skills) < 3:
            raise ValueError("Please enter at least 3 skills.")

        # STEP 1: Ingestion - clean up user input
        query_text = build_user_query(user_skills)

        # STEP 2: Scoring - compare user vs every job role
        scores = self.engine.score_user(query_text)

        # no match at all -> use fallback list instead of returning nothing
        if scores is None:
            return self._trending_fallback(top_n)

        # STEP 3: Sorting - rank roles from best match to worst
        self.df["match_score"] = scores
        ranked = self.df.sort_values("match_score", ascending=False)

        # STEP 4: Filtering - keep only the top N roles
        top_results = ranked.head(top_n)

        # convert to a simple list of dicts to return
        return [
            {"role": row["role"], "score": round(float(row["match_score"]), 4)}
            for _, row in top_results.iterrows()
        ]

    def _trending_fallback(self, top_n):
        # used when user's skills don't match anything (cold start)
        fallback = self.df.head(top_n)
        return [
            {"role": row["role"], "score": 0.0, "fallback": True}
            for _, row in fallback.iterrows()
        ]