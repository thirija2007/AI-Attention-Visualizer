#  AI Attention Visualizer

An interactive AI-based application that extracts text from an image using OCR, converts the extracted words into embeddings, and calculates attention scores to visualize which words receive higher attention.

##  Project Overview

The **AI Attention Visualizer** demonstrates the basic working concept of an attention mechanism using image text.

###  Project Flow

**Image → OCR → Extract Words → Embeddings → Attention → Word Attention Visualization**

##  Features

-  Upload an image containing text
-  Extract text using Tesseract OCR
-  Display the extracted text
-  Generate word embeddings using Sentence Transformers
-  Calculate attention scores using scaled dot-product attention
-  Display attention scores for each word
-  Highlight the word with the highest attention score
-  Interactive Streamlit interface

##  Technologies Used

- **Python**
- **Streamlit**
- **Tesseract OCR**
- **Pytesseract**
- **Sentence Transformers**
- **NumPy**
- **Pillow**

##  Project Structure

```text
AI-Attention-Visualizer/
│
├── app.py
├── ocr.py
├── embedding.py
├── attention.py
├── requirements.txt
├── packages.txt
└── README.md

⚙️ How It Works
1. Image Upload

The user uploads a JPG, JPEG, or PNG image through the Streamlit application.

2. OCR

Tesseract OCR extracts the text from the uploaded image.

3. Word Extraction

The extracted text is split into individual words. Unnecessary punctuation and very short words are removed.

4. Word Embeddings

The words are converted into numerical vectors using:

all-MiniLM-L6-v2

The model generates 384-dimensional embeddings.

5. Attention Calculation

The embeddings are used to calculate:

Q = XWQ
K = XWK
V = XWV

Scaled dot-product attention is then calculated using:

Attention(Q,K,V) = softmax(QKᵀ / √dk)V
6. Visualization

The application displays an attention bar for each extracted word.

The word with the highest calculated attention score is displayed as:

## Highest Attention

## Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/AI-Attention-Visualizer.git

Move into the project folder:

cd AI-Attention-Visualizer

Install the required Python packages:

pip install -r requirements.txt

##  Tesseract OCR Setup

Windows

Install Tesseract OCR on your computer.

The common installation location is:

C:\Program Files\Tesseract-OCR\tesseract.exe

The application is configured to use this path when running on Windows.

##  Run the Application

Run the following command:

streamlit run app.py

The application will open in your browser.

##  Streamlit Cloud Deployment

This project can be deployed using Streamlit Community Cloud.

The repository contains:

packages.txt

with:

tesseract-ocr

This allows Tesseract OCR to be installed in the Streamlit Cloud environment.

##  Application Workflow
<img width="1051" height="837" alt="Screenshot 2026-09-29 224909" src="https://github.com/user-attachments/assets/06e16e5d-318b-420e-b2af-04a7769ea8f3" />
<img width="988" height="867" alt="Screenshot 2026-09-29 224926" src="https://github.com/user-attachments/assets/62462039-faa0-4c83-88e1-3cc4f76bf67d" />
<img width="1030" height="797" alt="Screenshot 2026-09-29 224939" src="https://github.com/user-attachments/assets/00adc5da-53f7-41ac-86b0-590f0aea8dc6" />
<img width="1040" height="767" alt="Screenshot 2026-09-29 224952" src="https://github.com/user-attachments/assets/cbf36e30-fa63-4ef0-85d6-5c060a550983" />

Upload Image
      ↓
   OCR Text
      ↓
 Extract Words
      ↓
Word Embeddings
      ↓
Attention Calculation
      ↓
Attention Scores
      ↓
Word Attention Bars

##  Author

Thirija R

B.Sc. Computer Science with Artificial Intelligence
