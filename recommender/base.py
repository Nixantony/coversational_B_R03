# recommender/base.py
class BaseRecommender:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def load_data(self):
        raise NotImplementedError("Subclasses must implement load_data")

    def recommend(self, user_input):
        raise NotImplementedError("Subclasses must implement recommend")
