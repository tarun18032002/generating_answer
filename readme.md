# 🧠 Question Answer Manager using Django + OpenAI

A web app that lets you upload `.docx` files containing technical questions, auto-generates answers using OpenAI, and displays all results batch-wise — perfect for studying, documentation, or impressing your CTO.

---

## 🚀 Features

- 📄 Upload `.docx` files with questions (one per paragraph)
- 🔐 Each upload is saved as a unique batch (UUID-based)
- 🧠 Auto-generate answers using OpenAI GPT API
- 💾 Store questions and answers in the database
- 🔍 View all Q&A entries by batch
- ✅ Clean and simple UI with upload feedback

---

## 🛠️ Tech Stack

- **Backend**: Django
- **AI Integration**: OpenAI GPT-3.5 Turbo
- **Database**: SQLite (default)
- **File Parsing**: `python-docx`

---

## 🖼️ Screenshots

### 🔼 Upload `.docx` File
Uploads a Word file with questions.

### ✅ Answers Generated Automatically
Each question is answered using OpenAI and stored.

### 🔍 View Batch Questions & Answers
Each batch gets a unique page showing all Q&As.

---

## 🧑‍💻 Getting Started Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/question-answer-manager.git
cd question-answer-manager

2. **Create a virtual environment**
    ```python -m venv env
    source env/bin/activate  # On Windows:env\Scripts\activate
    ```

3. **Install dependencies**
    ```pip install -r requirements.txt```

4. **Set your OpenAI API Key**

    ### Option A: Set as environment variable

    ```export OPENAI_API_KEY="your-api-key"  # Windows: set OPENAI_API_KEY=your-api-key```

    ### Option B: Hardcode in views.py (for quick testing)

    ```openai.api_key = "your-api-key"```

5. **Run migrations**

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the development server**

    ``` python manage.py runserver ```

📌 Future Enhancements
- 🔐 Add user authentication & roles

- 📤 Export batch data to Excel or PDF

- 🏷️ Tag questions by category

- 🔍 Search/filter functionality

- 📊 Stats on questions/topics