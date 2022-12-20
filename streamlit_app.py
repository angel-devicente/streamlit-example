#from collections import namedtuple
#import altair as alt
#import math
#import pandas as pd
import streamlit as st
import requests

"""
# ML-Zoomcamp Capstone Project

"""

idx = st.slider("Mammography image number", 1, 2, 1)

url = 'https://ad1p7rqhyj.execute-api.eu-west-2.amazonaws.com/test/predict'  
data = {'url': 'https://mammography-test.s3.eu-west-2.amazonaws.com/mdb002.jpg'}                      

st.image(
    "https://mammography-test.s3.eu-west-2.amazonaws.com/mdb002.jpg",
    width=400, # Manually Adjust the width of the image as per requirement
)

if st.button('Predict'):
    result = requests.post(url, json=data).json() 
    result

