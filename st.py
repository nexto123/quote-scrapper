# This is a sample Python script.
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

tag = st.selectbox('choose a topic',['love','humour','life','books'])

generate = st.button('generate csv')

url = f"http://quotes.toscrape.com/tag/{tag}/"

#
res = requests.get(url)
# st.write(res)

content = BeautifulSoup(res.content, 'html.parser')

quotes  = content.find_all('div',class_='quote')

quote_file = []

for quote in quotes:
    text  = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    st.success(text)
    st.write(author)
    st.markdown(f"<a href=http://quotes.toscrape.com{link['href']}>{author}</a>", unsafe_allow_html=True )
    st.code(f"http://quotes.toscrape.com{link['href']}")
    quote_file.append([text, author, link])


if generate:
    try:
        df = pd.DataFrame(quote_file)
        df.to_csv('quote.csv', index=False, header=['Quote','Author','Link'])
    except:
        st.write('loading..')