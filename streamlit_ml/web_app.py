import streamlit as st
import pandas as pd
import numpy as np
# from sklearn.preprocessing import LabelBinarizer
# from tensorflow import keras
from PIL import Image


st.set_page_config(page_title='ASL Recognition', page_icon='./logo.jpg') #layout="wide"
st.title('American Sign Language Recognition')
st.markdown(""" 
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: visible;}
    .big-font {
    font-size:25px !important;
    font: Serif;
    }
    </style> 
    """, unsafe_allow_html=True)

# @st.cache(allow_output_mutation=True)

st.markdown('<p class="big-font">Converts images of sign-language to English Numbers and Letters (MAIS 2022)</p>', unsafe_allow_html=True)
st.markdown('')
st.subheader('Convert an image to text')
image_file = st.file_uploader('Choose an ASL Image', ['jpg', 'png'])

st.markdown('')
st.subheader('Convert images to English sentence')
sentence_image_files = st.file_uploader('Select one or more ASL Images', ['jpg', 'png'], accept_multiple_files = True)

# if len(sentence_image_files) > 0:
#     sentence = ''
#     for image_file in sentence_image_files:
#         image = Image.open(image_file).convert('L')
#         image = np.array(image, dtype='float32')
#         letter = preprocess_image(image, image_file, best_model, label_binarizer)
#         sentence += letter
#     st.write(f'The sentence is predicted as {sentence}')

st.markdown('')
st.markdown('You can find the Convolutional Neural Network used [here](https://github.com/ArpanSaha07/signlang-to-text)')

st.image('./nural-network-05.jpg', use_column_width=True)


column1, column2 = st.columns(2)
column1.markdown("[![Title]('https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg')]('https://www.linkedin.com/in/arpan-saha7/')")
column2.markdown("[![Title]('./Octicons-mark-github.svg')]('https://github.com/ArpanSaha07)")


footer = """<style>
a:link , a:visited{
color: blue;
}

a:hover,  a:active {
color: red;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgba(62, 75, 91, 1);
    color: black;
    text-align: center;
    line-height: 0.7;
}
</style>
<div class="footer">
    <p>&copy 2022 @ Streamlit
    <p>Developed by Arpan Saha and Emilia Gagne</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
