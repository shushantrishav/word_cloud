import streamlit as st
import matplotlib.pyplot as plt
from Wordcloud import (
    clean_text, count_frequency, generate_wordcloud,
    extract_text_from_docx, extract_text_from_pdf  # ← import added
)

st.set_page_config(page_title="Word Cloud Generator", layout="wide")
st.title("☁️ Word Cloud Generator")
st.write("Upload a `.txt` or `.docx` file to generate a word cloud.")

uploaded_file = st.file_uploader("Upload file", type=["txt", "docx", "pdf"])


if uploaded_file:
    if uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8").splitlines()
    elif uploaded_file.name.endswith(".docx"):
        text = extract_text_from_docx(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        text = extract_text_from_pdf(uploaded_file)
    else:
        st.error("Unsupported file format.")
        st.stop()

    # 🎯 PREVIEW PANE
    st.subheader("📄 File Preview")
    preview_text = "\n".join(text[:100])  # limit preview to top 100 lines
    st.text_area("Preview", value=preview_text, height=300, disabled=True)

    if st.button("🌀 Generate Word Cloud"):
        cleaned = clean_text(text)
        freqs = count_frequency(cleaned)
        cloud = generate_wordcloud(freqs)

        st.subheader("Generated Word Cloud")
        fig, ax = plt.subplots(figsize=(10, 7.2))
        ax.imshow(cloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

        with st.expander("🔠 Top 20 Words"):
            top_words = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:20]
            for word, count in top_words:
                st.write(f"**{word}**: {count}")
