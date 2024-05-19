# ☁️ WordCloud Generator

A simple and interactive **Streamlit app** that generates a word cloud from `.txt`, `.docx`, or `.pdf` files.  
Designed for quick text analysis, keyword visualization, and document previews.

---

## 🚀 Features

- 📂 Upload `.txt`, `.docx`, or `.pdf` files
- 👀 Preview your uploaded content before processing
- 🧹 Removes punctuation and common uninteresting words
- 📊 Displays top 20 most frequent words
- 🎨 Generates a dynamic word cloud (matplotlib + WordCloud)

---

## 🖥️ Live Demo

> Want to see it in action? [Streamlit Cloud Deploy Button coming soon!]

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wordcloud-generator.git
cd wordcloud-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the App

```bash
streamlit run app.py
```

## 🧾 Requirements

```
   - Python 3.8+
   - Streamlit
   - wordcloud
   - matplotlib
   - python-docx
   - PyMuPDF (fitz)
```

Install all with:

```bash
    pip install -r requirements.txt
```
## 📁 Project Structure
```bash
wordcloud_generator/
│
├── app.py                 # Streamlit UI
├── wordcloud_helper.py   # Text cleaning, word counting, cloud generation
├── requirements.txt       # Python dependencies
└── README.md              # This file
```
## ✨ Future Enhancements
    🔽 Downloadable image output (PNG)
    🎨 Custom color/theme selection
    📝 User-defined stopword list
    📊 Word frequency chart view

## 🧑‍💻 Author
Shushant Rishav