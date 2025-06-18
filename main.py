import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'recommender'))

from model import ConversationalRecommender

def main():
    print("\n📚 Welcome to the Conversational Book Recommender!")

    recommender = ConversationalRecommender("data/data.csv")

    while True:
        user_input = input("\nDescribe what kind of book you'd like to read (or type 'exit' to quit):\n> ")

        if user_input.lower() in ["exit", "quit"]:
            print("\n👋 Thank you for using the recommender. Goodbye!")
            break

        results = recommender.recommend(user_input)

        print("\n🔍 Here are some book suggestions for you:")
        for book in results:
            print("\n📘 Title:", book['title'])
            print("📂 Genre:", book['genre'])
            print("📝 Summary:", book['summary'][:300] + "...")


if __name__ == "__main__":
    main()
