import xgboost as xgb
import streamlit as st
import pandas as pd

# import datetime
# from datetime import date
# janvier2016 = date(2016, 1, 1)


# #Loading up the Regression model we created
@st.cache_resource
def import_model() :
    model = xgb.XGBClassifier()
    model.load_model('./data/xgb_model.json')
    return model
model = import_model()

# #Caching the model for faster loading
# @st.cache_data
def load_data(pkl_name):
    df = pd.read_pickle(pkl_name)
    return df
X_test = load_data("./data/X_test.pkl")

def predict(number):
    #Predicting the price of the carat
    prediction = model.predict(X_test.iloc[[number]])
    retard =  "est en retard" if prediction else "n'est pas en retard"
    return retard


st.title('Retard avion')
ligne = st.number_input('la ligne chacal', min_value=1, max_value=100, value=1)
# flight_date = st.date_input('Start date', janvier2016 )
# departstate = st.selectbox('Depart state', datall.ORIGIN_STATE_NM.unique())
# departcity = st.selectbox('Depart city', datall[datall["ORIGIN_STATE_NM"] == departstate ].ORIGIN_CITY_NAME.unique())
if st.button('Retard ou pas ?'):
    retard = predict(ligne)
    st.success(f'Votre avion {retard}')
