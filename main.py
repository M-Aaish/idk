import streamlit as st
import subprocess
import os
import sys
from PIL import Image

st.set_page_config(page_title="Image Processing App", layout="wide")
st.title("Upload and Process Your Image")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
p_value = st.slider("Select parameter (--p)", min_value=1, max_value=10, value=4)

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)
    
    image = Image.open(uploaded_file)
    resized_image = image.resize((256, 256))
    file_path = os.path.join("uploads", uploaded_file.name)
    resized_image.save(file_path)
    
    col1, col2 = st.columns(2)
    col1.image(resized_image, caption="Input Image (256x256)", use_column_width=True)
    
    if st.button("Process Image"):
        command = [sys.executable, "Oil-Painting.py", "--f", file_path, "--p", str(p_value)]
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            base_name = os.path.splitext(uploaded_file.name)[0]
            output_dir = os.path.join("output", f"{base_name}-p-{p_value}")
            final_image_path = os.path.join(output_dir, "Final_Result.png")
            
            if os.path.exists(final_image_path):
                col2.image(final_image_path, caption="Processed Image", use_column_width=True)
            else:
                st.error("Processed image not found.")
        else:
            st.error("An error occurred while processing the image.")
            st.text(result.stderr)
