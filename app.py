import streamlit as st
#from streamlit_image_comparison import image_comparison
#import cv2


st.set_page_config("1980's P vs 2020's P")


st.image(
    "https://rlyfaazj0.toastcdn.net/20221019/145434.523656000/106827397_1.png", #카메라
    width=120,
)

st.header("1980's P vs 2020's P")

st.write("")
"This is a reproduction of the fantastic [WebbCompare](https://www.webbcompare.com/index.html) app by [John Christensen](https://twitter.com/JohnnyC1423). It's built in Streamlit and takes only 10 lines of Python code. If you like this app, please star [John's original repo](https://github.com/JohnEdChristensen/WebbCompare)!"
st.write("")

# st.markdown("### Southern Nebula")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
#     img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
#     label1="Hubble",
#     label2="Webb",
# )


# st.markdown("### Galaxy Cluster SMACS 0723")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
#     img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
#     label1="Hubble",
#     label2="Webb",
# )

# st.markdown("### Carina Nebula")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/carina_2800.png",
#     img2="https://www.webbcompare.com/img/webb/carina_2800.jpg",
#     label1="Hubble",
#     label2="Webb",
# )

# st.markdown("### Stephan's Quintet")
# image_comparison(
#     img1="https://www.webbcompare.com/img/hubble/stephans_quintet_2800.jpg",
#     img2="https://www.webbcompare.com/img/webb/stephans_quintet_2800.jpg",
#     label1="Hubble",
#     label2="Webb",
# )


