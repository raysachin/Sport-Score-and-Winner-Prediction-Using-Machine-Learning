import streamlit as st
from PIL import Image
import os
st.set_page_config(
    page_title= "SPORTS_SCORE_PREDICTION",
    page_icon= "IPL"


)

st.title("IPL SCORE AND WIN PREDICTION")
base_dir = os.path.dirname(__file__)

# Construct the full path to the image
image_path = os.path.join(base_dir, 'assets', 'IPL.jpg')
# Open the image
ipl_image = Image.open(image_path)
st.image(ipl_image)
st.sidebar.success("Select a page above")
