# Study Planner Assistant (AI-Powered)

An intelligent Study Planner Assistant that generates personalized study plans using Retrieval-Augmented Generation (RAG) and Machine Learning.

---

## Features

* Generate study plans based on subject and available hours
* Uses AI (Sentence Transformers + FAISS)
* Retrieves relevant topics using RAG
* Simple web interface using Flask
* Fast and efficient recommendations

---

## Tech Stack

* Python
* Flask
* FAISS (Vector Search)
* Sentence Transformers
* HTML, CSS

---

## Project Structure

```
Study-Planner-Assistant/
│── app.py
│── rag_engine.py
│── build_index.py
│── docs.json
│── rag.index
│── templates/
│   ├── index.html
│   ├── login.html
│   ├── plan.html
│── data/
│── README.md
```

---

## How It Works

1. User enters subject and study hours
2. System encodes query using Sentence Transformers
3. FAISS retrieves relevant study content
4. Generates a structured study plan

---

## Run Locally

### 1. Clone the repository

```
git clone https://github.com/Ravi4348/Study-Planner-Assistant.git
cd Study-Planner-Assistant
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
python app.py
```

---

## Future Improvements

* Add user authentication
* Deploy on cloud (Render / Railway)
* Add more datasets for better recommendations
* Improve UI/UX

---

## Author

Ravi Teja
GitHub: https://github.com/Ravi4348

---

## License

This project is for educational purposes.
