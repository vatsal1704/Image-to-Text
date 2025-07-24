# 🖼️ Image-to-Text Converter

A simple web application that extracts text from uploaded images using Optical Character Recognition (OCR).It transforms images into editable text—perfect for scanning documents, signage, screenshots, and more.

---

## 🌐 Live Demo  
Try the app live: **[Live Demo](https://image-to-text-gemini.streamlit.app/)**

## 📸 Screenshots  
See it in action: **[Screenshots](https://your-screenshots-link.example.com)**

---

## 💡 Why Use It?

- **Document digitization** – Convert scanned pages, PDFs, or camera pics into searchable/editable text.  
- **Image captioning & data entry** – Automatically extract text for populating forms, captions, or databases.  
- **Accessibility** – Make image content accessible by converting embedded or scanned text into readable format.  
- **Language learning & research** – Quickly extract quotes or paragraphs from images for translation or analysis.

---

## 🛠️ Features

- 🗂️ Upload PNG, JPEG, GIF images  
- 🔧 Pre-process images using OpenCV (grayscale, thresholding)  
- 📝 OCR using Tesseract (via `pytesseract`)  
- 📋 Displays extracted text with an easy copy button  
- ⚙️ Optionally customize language or preprocessing steps

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.x  
- [Tesseract OCR Engine](https://github.com/tesseract-ocr/tesseract) installed

```bash
# Install Tesseract on Ubuntu
sudo apt update
sudo apt install tesseract-ocr libtesseract-dev
