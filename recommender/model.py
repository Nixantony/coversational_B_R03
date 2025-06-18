# recommender/model.py
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import torch
from recommender.base import BaseRecommender  # 🧠 Inheritance

class ConversationalRecommender(BaseRecommender):
    def __init__(self, csv_path):
        super().__init__(csv_path)
        self.load_data()

    def load_data(self):
        self.data = pd.read_csv(self.csv_path)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.summaries = self.data['summary'].fillna("").tolist()
        self.embeddings = self.model.encode(self.summaries, convert_to_tensor=True)

    def recommend(self, user_input, top_k=5):
        query_embedding = self.model.encode(user_input, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        top_indices = torch.topk(scores, k=top_k).indices.tolist()

        return [
            {
                "title": self.data.iloc[i]['title'],
                "genre": self.data.iloc[i]['genre'],
                "summary": self.data.iloc[i]['summary']
            }
            for i in top_indices
        ]
