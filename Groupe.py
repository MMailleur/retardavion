import xgboost as xgb
import streamlit as st
import pandas as pd
import pymysql
from utils import create_table, save_formulaire,state_list,heure_list
import numpy as np
import base64
import datetime
from datetime import date

st.set_page_config(
    page_title="RetardAvion",
    page_icon=":airplane:",
)
janvier2016 = date(2016, 1, 1)

# #Caching the model for faster loading
@st.cache_data 
def load_data(data_name):
    df = pd.read_pickle(data_name)
    return df
X_test = load_data("./Model/X_test.pkl")
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('photo de groupe.png')    
# #Loading up the Regression model we created
@st.cache_resource
def db_connec():
    conn = conn=pymysql.connect(host='localhost',port=int(3306),user='root', passwd='root', db='retardavion')
    create_table(table_name="pred_historique")
    return conn
conn = db_connec()
def import_model() :
    model = xgb.XGBClassifier()
    model.load_model('./Model/xgb_model.json')
    return model
model = import_model()

