import streamlit as st
import numpy as pd

import pandas as pd
# from streamlit_image_comparison import image_comparison
# import cv2


st.set_page_config("Fashion Trand")


st.image("./Fashion/2020 image/유아인.png") #카메라


st.header("1980's Fashion vs 2020's Fashion")

st.write("")
"This web is a site where you can know the fashion from the past to the present.!"
st.write("")

st.markdown("### 1980's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("Spring")
   st.image("./Fashion/1980 image/1980패션 봄.jpg")

with col2:
   st.header("Summer")
   st.image("./Fashion/1980 image/1980패션 여름.jpg")
with col3:
    st.header("Fall")
    st.image("./Fashion/1980 image/1980패션 가을.jpg")

with col4:
    st.header("Winter")
    st.image("./Fashion/1980 image/1980패션 겨울.jpg")

st.markdown("### 2020's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("Spring")
   st.image("./Fashion/2020 image/2020패션 봄.jpg")

with col2:
   st.header("Summer")
   st.image("./Fashion/2020 image/2020패션 여름.jpg")

with col3:
    st.header("Fall")
    st.image("./Fashion/2020 image/2020패션 가을.jpg")

with col4:
    st.header("Winter")
    st.image("./Fashion/2020 image/2020패션 겨울.jpg")

add_selectbox = st.sidebar.selectbox("여성패션 온라인 쇼핑몰", ("45번가", "갠소", "고고싱","그녀희재","그레이시크"))
add_selectbox = st.sidebar.selectbox("남성패션 온라인 쇼핑몰", ("무신사", "디에프디", "힙합퍼",))
add_selectbox = st.sidebar.selectbox("액세서리 온라인 쇼핑몰", ("도나앤디","러블링","윙블링"))
add_selectbox = st.sidebar.selectbox("신발 온라인 쇼핑몰", ("러블리슈즈", "보가", "사뿐",))


Fashion = pd.read_csv('./df/2020-2022_fashion_marketing.csv')
st.write(Fashion)

import plotly.express as px
st.header("Size of the fashion market for all items")
st.bar_chart(Fashion, width = 150, height = 600)