#from collections import namedtuple
#import altair as alt
#import math
#import pandas as pd
import streamlit as st
import requests

"""
# ML-Zoomcamp Capstone Project

"""

idx = st.slider("Mammography image number", 1, 200, 100)

url = 'https://ad1p7rqhyj.execute-api.eu-west-2.amazonaws.com/test/predict'  
data = {'url': 'https://i.ibb.co/ZXs9SJN/mdb182.jpg'}                      

result = requests.post(url, json=data).json() 

result

