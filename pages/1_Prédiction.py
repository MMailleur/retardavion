import xgboost as xgb
import streamlit as st
import pandas as pd
import pymysql
from utils import create_table, save_formulaire,state_list,heure_list,delete_formulaire
import numpy as np
from Groupe import janvier2016,model,conn
from pandas import DataFrame



st.title('Retard avion')
col1, col2, col3 = st.columns((1,.3,1))
formulaire ={}
with col1 :    
    formulaire["date"        ] = st.date_input("Date du vol",janvier2016),
    formulaire["heuredep"    ] = st.selectbox("Heure de depart",heure_list),
    formulaire["departstate" ] = st.selectbox("Etat de depart",state_list)
with col3 :
    formulaire["arrivalstate"] = st.selectbox("Etat de destination",state_list),
    formulaire["retard"      ] = st.slider('Minute(s) de retard au depart', 0, 100, 1),
    formulaire["distance"    ] = st.number_input("Distance du vol", min_value=0,step=1),


if st.button("Submit"):
       
       # Utilisation du modèle de prédiction.
       # On appelle la fonction prediction_survie() et on lui passe les réponses de l'utilisateur.
       keys = ["retard","distance"]
       x = np.array([formulaire.get(key) for key in keys]).reshape(1, 2)
       pred = model.predict(x)
       # On inscrit la prédiction dans le dictionnaire.
       if pred:
           formulaire["predict"] = "Retard"
       else:
           formulaire["predict"] = "A l'heure"
       
       # Enregistrement du formulaire en BDD.
       # On appelle la fonction save_formulaire popur enregistrer les réponses de l'utilisateur en BDD
       save_formulaire(conn=conn, features=[i for i in formulaire.values()])
       # Affichage de la prédictions.
       if pred:
           st.header("Retard")
       else:
           st.header("Pas retard")  

sql_query = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM pred_historique
                               ''', conn)
df = pd.DataFrame(sql_query)
st.dataframe(df,use_container_width=True)
if st.button("Reset"):
    delete_formulaire(conn)
    st.experimental_rerun()



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2016/05/20/22/45/airport-1406162_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 