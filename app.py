import streamlit as st
import numpy as np
from PIL import Image

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention


st.title("🧠 AI Attention Visualizer")

st.write(
    "Upload an image to extract text and visualize attention scores."
)


file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if file:

    # Display uploaded image
    image = Image.open(file)
    st.image(image, width=500)

    # OCR
    text = extract_text(image)

    st.subheader("📝 Extracted Text")

    if not text.strip():
        st.error("No text found in the image.")
        st.stop()

    st.write(text)

    # Extract words
    words = text.split()

    # Remove punctuation
    words = [
        word.strip(".,!?;:()[]{}")
        for word in words
    ]

    # Remove very short words
    words = [
        word for word in words
        if len(word) > 2
    ]

    # Use first 20 words
    words = words[:20]

    # Create embeddings
    embeddings = create_embeddings(words)

    # Calculate attention
    scores = calculate_attention(embeddings)

    # Display attention
    st.subheader("🧠 Word Attention")

    max_score = scores.max()

    if max_score > 0:
        display_scores = scores / max_score
    else:
        display_scores = scores

    for word, score in zip(words, display_scores):

        st.write(f"**{word}**")

        st.progress(float(score))

    # Highest attention word
    top_index = np.argmax(scores)
    top_word = words[top_index]

    st.success(
        f"⭐ Highest Attention: **{top_word}**"
    )