# This is a sample Python script.
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

tag = st.selectbox('choose a topic',['love','humour','life','books'])

url = f"http://quotes.toscrape.com/tag/{tag}/"

#
res = requests.get(url)
# st.write(res)

content = BeautifulSoup(res.content, 'html.parser')

st.code(content)