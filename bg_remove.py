import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import uuid

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download image", convert_image(fixed), uuid.uuid4().hex + "-rembg.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "dng"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 100MB.")
    else:
        fix_image(upload=my_upload)
