import string
from wordcloud import WordCloud as wc
import docx
import fitz  # PyMuPDF

# Define stopwords and punctuations
punctuations = list(string.punctuation) + list("1234567890\n")
uninteresting_words = {
    "the", "mr", "mrs", "for", "us", "a", "so", "to", "if", "is", "not", "on", "it", "of", "and", "or", "an", "as", "in", "i", "me", "my",
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", "than"
}

def clean_text(text_lines):
    """Removes punctuation and joins lines into a single string."""
    cleaned_text = ""
    for line in text_lines:
        for char in punctuations:
            line = line.replace(char, "")
        cleaned_text += f" {line}"
    return cleaned_text

def count_frequency(text):
    """Counts word frequency excluding stopwords."""
    words = text.split()
    frequencies = {}
    for word in words:
        word = word.lower().strip()
        if word and word not in uninteresting_words:
            frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

def generate_wordcloud(frequencies):
    """Generates a WordCloud object from word frequencies."""
    cloud = wc(background_color="black", colormap="Blues", width=1200, height=720)
    cloud.generate_from_frequencies(frequencies)
    return cloud

def extract_text_from_docx(file):
    """Extracts text lines from a .docx file."""
    doc = docx.Document(file)
    return [p.text for p in doc.paragraphs if p.text]

def extract_text_from_pdf(file):
    """Extract text from PDF file as a list of lines."""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.splitlines()
