# Import des librairies.
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import streamlit as st
import numpy as np



# ////////////////////////////////////////////////////////////// DATA SQL //////////////////////////////////////////////////////////////////////////// #

### Fonction permettent de créer une table.
### Les paramètres : On donne en paramètre le nom de la table que nous souhaitons créer

def create_table(table_name:str):
    engine=create_engine('mysql+pymysql://root:root@localhost/retardavion')
    inspector=inspect(engine)
    if not table_name in inspector.get_table_names():
        
        # Initialisation des colonnes.
        df = pd.DataFrame({'date':[],'heuredep':[],'departstate':[],'arrivalstate':[],'retard':[] ,'distance':[] , "predict":[]})
        
        # Typage des colonnes de la Table SQL.
        df['date']  = df['date'].astype('str')
        df['heuredep']  = df['heuredep'].astype('str')
        df['departstate']  = df['departstate'].astype('str')
        df['arrivalstate']  = df['arrivalstate'].astype('str')
        df['retard']  = df['retard'].astype('float64')
        df['distance']  = df['distance'].astype('float64')
        df['predict']  = df['predict'].astype('str')

        # envoie du DataFrame sur SQL.
        df.to_sql(name=table_name, con=engine, if_exists='fail', index=False)
    
# //////////////////////////////////////////////////////// Traitement Formulaire ///////////////////////////////////////////////////////////////////// #

### Fonction permettent d'enregistrer le formulaire en BDD (la target et les features).
### Les paramètres : la connexion à la BDD, et une liste des features.    
def save_formulaire(conn, features:list):
    cursor = conn.cursor()
    sql = "INSERT INTO pred_historique (date,heuredep,departstate,arrivalstate,retard, distance, predict) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, features)
    conn.commit()
def delete_formulaire(conn):
    cursor = conn.cursor()
    sql = "DELETE FROM retardavion.pred_historique;"
    cursor.execute(sql)
    conn.commit()
state_list = ['Texas', 'Michigan', 'Washington', 'New York', 'California',
       'Illinois', 'Arizona', 'Missouri', 'Florida', 'Colorado', 'Hawaii',
       'Nevada', 'Utah', 'U.S. Virgin Islands', 'Massachusetts',
       'Oklahoma', 'Pennsylvania', 'North Carolina', 'Virginia',
       'Georgia', 'Tennessee', 'Wyoming', 'New Jersey', 'Puerto Rico',
       'New Mexico', 'Louisiana', 'Indiana', 'Oregon', 'Maryland',
       'Minnesota', 'Wisconsin', 'Iowa', 'Nebraska', 'Kentucky', 'Ohio',
       'Connecticut', 'Idaho', 'Alaska', 'Rhode Island', 'Kansas',
       'Maine', 'South Carolina', 'Alabama', 'Vermont', 'North Dakota',
       'Mississippi', 'Montana', 'Arkansas', 'South Dakota',
       'West Virginia', 'U.S. Pacific Trust Territories and Possessions',
       'New Hampshire']

heure_list = ['00:00',
'00:30',
'01:00',
'01:30',
'02:00',
'02:30',
'03:00',
'03:30',
'04:00',
'04:30',
'05:00',
'05:30',
'06:00',
'06:30',
'07:00',
'07:30',
'08:00',
'08:30',
'09:00',
'09:30',
'10:00',
'10:30',
'11:00',
'11:30',
'12:00',
'12:30',
'13:00',
'13:30',
'14:00',
'14:30',
'15:00',
'15:30',
'16:00',
'16:30',
'17:00',
'17:30',
'18:00',
'18:30',
'19:00',
'19:30',
'20:00',
'20:30',
'21:00',
'21:30',
'22:00',
'22:30',
'23:00',
'23:30' ]