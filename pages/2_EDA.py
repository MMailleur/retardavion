import xgboost as xgb
import streamlit as st
import pandas as pd
import pymysql
from utils import create_table, save_formulaire,state_list,heure_list
import numpy as np
from Groupe import janvier2016,model,conn

col1, col2, col3 = st.columns((.4,1,.2))
with col2 :
    st.title('Analyse exploratoire')

st.header("Proportion de vol en retard par compangnie")
col1, col2, col3 = st.columns((.4,1,.2))
with col2 :
    st.image("pourcentage.png")

st.header("Etats avec le plus de vol")
st.image("map.png")

st.header("Proportion d'avion en retard par Etat")
st.image("map3.png")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2018/05/28/11/13/clouds-3435767_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
add_bg_from_url() 

