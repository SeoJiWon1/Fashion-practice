import streamlit as st
# from streamlit_image_comparison import image_comparison
# import cv2


st.set_page_config("1980's P vs 2020's P")


st.image(
    "https://www.musinsastudio.com/v2/share.jpg", #카메라
    width=340,
)

st.header("1980's Fashion vs 2020's Fashion")

st.write("")
"This web is a site where you can know the fashion from the past to the present.!"
st.write("")

st.markdown("### 1980's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("Spring")
   st.image("./1980 image/1980패션 봄.jpg")

with col2:
   st.header("Summer")
   st.image("./1980 image/1980패션 여름.jpg")
with col3:
    st.header("Fall")
    st.image("./1980 image/1980패션 가을.jpg")

with col4:
    st.header("Winter")
    st.image("./1980 image/1980패션 겨울.jpg")

st.markdown("### 2022's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("Spring")
   st.image("https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg")

with col2:
   st.header("Summer")
   st.image("https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg")

with col3:
    st.header("Fall")
    st.image("https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg")

with col4:
    st.header("Winter")
    st.image("https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg")
