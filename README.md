# Conversational Book Recommender

This project is a student-friendly implementation of a **natural language-based book recommendation system**. Instead of selecting genres manually, users simply describe the kind of book they want to read in their own words — and the system finds relevant book suggestions based on the meaning of their input.

It demonstrates how artificial intelligence and natural language processing (NLP) can be applied to real-world problems like personalized content discovery. This is an ideal project for showcasing Python skills, AI integration, inheritance, and modular design.

---

## 📦 Project Structure
```
conversational_book_recommender/
│
├── data/
│   └── data.csv              # Dataset with title, genre, summary
│
├── recommender/
│   ├── base.py               # Base class (supports inheritance)
│   └── model.py              # Conversational recommender (inherits from base)
│
├── main.py                  # CLI program to run the recommender
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🚀 How to Run the Project

1. Make sure you have Python 3.10+ installed.
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the application:
   ```bash
   python main.py
   ```

---

## 💬 Example Interaction
```
Describe what kind of book you're looking for (or type 'exit' to quit):
> A suspenseful thriller involving a detective

🔍 Recommendations:
📘 Title: The Girl with the Dragon Tattoo
📂 Genre: Crime
📝 Summary: A journalist and a hacker team up to uncover dark secrets...
```

---

## ✅ Dataset Format
The system uses a CSV file containing book information. Required columns:
- `title`: The name of the book
- `genre`: The category or style of the book
- `summary`: A short description of the book’s plot/content

---

## 🤖 How It Works
This project uses **semantic similarity** to match your description with the most relevant book summaries. The main steps include:
1. **Converting text to vectors** using the Sentence-BERT model (`all-MiniLM-L6-v2`)
2. **Comparing vectors** with cosine similarity to find the closest matches
3. **Displaying book titles, genres, and summaries** ranked by relevance

This removes the limitations of keyword-based search and enables more intelligent, conversational interaction.

---

## 🧠 Technologies & Libraries Used
- `sentence-transformers`: for generating vector embeddings from text
- `torch` (PyTorch): for efficient numerical computations
- `pandas`: for reading and processing the dataset

---

## 🎓 What You Learn from This Project
- Object-Oriented Programming (OOP) with Inheritance
- Use of Python modules and packages
- Basics of Natural Language Processing (NLP)
- Text similarity and AI-based recommendation
- Code modularity and project structuring

---

## 🛠️ Future Improvements
- Allow users to save their favorite books (with pickle or SQLite)
- Add a feedback system (Was this book helpful?)
- Build a web version using Streamlit or Flask
- Support for multilingual queries and summaries

---

It’s a simple, functional, and meaningful AI-based software solution — ideal for real-world educational or business-oriented use cases.
