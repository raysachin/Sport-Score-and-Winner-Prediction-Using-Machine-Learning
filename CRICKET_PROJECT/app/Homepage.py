import streamlit as st
from PIL import Image
st.set_page_config(
    page_title= "SPORTS_SCORE_PREDICTION",
    page_icon= "IPL"


)

st.title("IPL SCORE AND WIN PREDICTION")
ipl_image = Image.open('./assets/IPL.jpg')
st.image(ipl_image)
st.sidebar.success("Select a page above")
