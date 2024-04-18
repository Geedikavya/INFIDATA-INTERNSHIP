import streamlit as st
from PIL import Image

st.header("Image Gallery")

st.info("Lotus")
img=Image.open("lotus1.jpg")
st.image(img,width=600)

st.info("Butterfly")
img2=Image.open("butterfly.jpg")
st.image(img2,width=600)

st.info("Tom and jerry")
img3=Image.open("1.jpg")
st.image(img3,width=600)


