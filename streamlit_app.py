import streamlit as st
import csv
import pandas as pd
import numpy as py

df = pd.read_csv('sprint1items.csv')

namearray = []
descarray = []
ammountarray = []
picturearray = []
for i in range(38):
    namearray.append(df.iloc[i][0])
    descarray.append(df.iloc[i][1])
    ammountarray.append(df.iloc[i][2])
    picturearray.append(df.iloc[i][3])

st.set_page_config(page_title="Mohji's shop", page_icon=":tada:", layout='wide')
st.title("Welcome")

col1_names = []
col2_names = []
col3_names = []
col1_desc = []
col2_desc = []
col3_desc = []
col1_pic = []
col2_pic = []
col3_pic = []


for i in range(12):
    col1_names.append(namearray[i])
    namearray.pop(i)
    col1_pic.append(picturearray[i])
    picturearray.pop(i)

for i in range(12):
    col2_names.append(namearray[i])
    namearray.pop(i)
    col2_pic.append(picturearray[i])
    picturearray.pop(i)




# 

'''
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=200)
    tile.title(namearray[])
'''
    
col1, col2, col3 = st.columns(3)


with col1:
    for i in range(12):
        name = f"<p style = 'font-size:18px;'>{col1_names[i]}</p>"
        st.markdown(name, unsafe_allow_html=True)
        st.image(col1_pic[i])

with col2:
    for i in range(12):
        name = f"<p style = 'font-size:18px;'>{col2_names[i]}</p>"
        st.markdown(name, unsafe_allow_html=True)
        st.image(col2_pic[i])
    
    
    