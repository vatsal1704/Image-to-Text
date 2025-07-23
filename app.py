# import streamlit as st
# from PIL import Image
# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# # Page config (must be first Streamlit call)
# st.set_page_config(page_title="Image to Text – Build a Digital Marketing Campaign")

# # Load environment variables
# load_dotenv()

# # Configure Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Title and description
# st.title("🖼️📷 Image to Text with Gemini")
# st.write("Upload an image and get a text description using Google Generative AI.")

# # Input prompt
# input_prompt = st.text_input("✏️ Input Prompt")

# # Upload section
# st.subheader("📤 Upload your image for processing")
# uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# # Display the uploaded image
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image", use_container_width=True)

#     # Summary generation (placeholder or real logic)
#     st.markdown("### 📝 Summary")
    
#     if input_prompt:
#         # Convert image to Gemini-friendly format
#         img_data = genai.types.content.Image.from_pil_image(image)

#         # Generate response using Gemini
#         model = genai.GenerativeModel("gemini-pro-vision")
#         response = model.generate_content([input_prompt, img_data])

#         # Display response
#         st.write(response.text)
#     else:
#         st.info("ℹ️ Please enter an input prompt to generate a summary.")



# def get_llm_response():
#     if input_prompt!="":
#         response = model.generate_content([input_prompt, img_data])
#     else:
#         response=model.generate_content([input_prompt])
#     return st.write(response.text)



# # Optional submit button
# if st.button("Submit"):
#     if not uploaded_file or not input_prompt:
#         st.warning("⚠️ Please upload an image and enter the input prompt.")
#     else:
#         st.success("✅ Submission received!")


import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit page config
st.set_page_config(page_title="Image to Text – Gemini")

st.title("🖼️📷 Image to Text with Gemini")
st.write("Upload an image and enter a prompt to generate a description using Google Gemini Vision model.")

# Input prompt
input_prompt = st.text_input("✏️ Enter your prompt")

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

# Display image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

# Submit button (optional use-case)
if st.button("Submit"):
    if not uploaded_file or not input_prompt:
        st.warning("⚠️ Please upload an image and enter a prompt.")
    else:
        st.success("✅ Processing your input!")
    if input_prompt:
        # Convert PIL image to bytes
        image_bytes_io = io.BytesIO()
        image.save(image_bytes_io, format="JPEG")
        image_bytes = image_bytes_io.getvalue()

        # Prepare Gemini-compatible image dict
        img_data = {
            "mime_type": "image/jpeg",
            "data": image_bytes
        }

        # Load Gemini Vision model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate content
        response = model.generate_content([input_prompt, img_data])

        # Show result
        st.markdown("### 📝 Gemini Response")
        st.write(response.text)
    else:
        st.info("ℹ️ Please enter a prompt to generate text.")


