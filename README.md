# Conversational Book Recommender.

This project is a beginner-friendly implementation of a conversational book recommendation system built using Python. Instead of choosing from a predefined list of genres, users can describe the kind of book they are interested in, and the system will respond with appropriate book suggestions based on the meaning of their input.

This project applies artificial intelligence techniques and natural language processing to help users discover relevant reading material. It is well-suited for showcasing concepts like class inheritance, modular coding practices, and semantic search.

---

## Project Structure
```
conversational_book_recommender/
│
├── data/
│   └── data.csv              # CSV file containing books with titles, genres, and summaries
│
├── recommender/
│   ├── base.py               # Abstract base class (used for inheritance)
│   └── model.py              # Main class that extends the base and implements the recommendation logic
│
├── main.py                  # Main script for running the program
├── requirements.txt         # List of required Python packages
└── README.md                # Project explanation and setup instructions
```

---

## Getting Started

1. Ensure Python 3.10 or newer is installed on your system.
2. (Optional) Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # For macOS/Linux
   .venv\Scripts\activate       # For Windows
   ```
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## Sample Run
```
Please describe the kind of book you're interested in (or type 'exit' to quit):
> A mystery involving a detective and a secret society

Here are some suggested books:
Title: The Da Vinci Code
Genre: Mystery
Summary: A symbologist and a cryptologist uncover a historical conspiracy...
```

---

## CSV Format
The application uses a CSV file containing information about books. Each row should include:
- `title`: Book name
- `genre`: Category of the book
- `summary`: A short description of the book content

---

## Technical Overview
The program works by comparing the user's input with summaries of books using semantic similarity. Here's how it functions:
1. The Sentence-BERT model transforms text into vector representations.
2. Cosine similarity is used to compare user input against book summaries.
3. The system then selects the most relevant matches based on similarity scores.

---

## Tools and Libraries Used
- `sentence-transformers`: For encoding text into vectors
- `torch`: For mathematical operations and efficient processing
- `pandas`: For reading and managing tabular data from CSV files

---

## Educational Value
This project provides hands-on experience in:
- Object-oriented programming using class inheritance
- Organizing Python code into packages and reusable modules
- Understanding and applying NLP techniques in a practical setting
- Developing a functional command-line software tool

---

## Possible Future Additions
- Ability to store and retrieve user preferences using file storage or databases
- User feedback or rating system
- Graphical or web-based interface
- Expand support for multilingual data or questions

---

This project is a strong candidate for academic demonstrations, learning AI techniques, and building personalized recommendation engines in real-world settings.