import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("Présentation des bases de données")


@st.cache_data
def charger_json():
    chemin_fichier = "..\Scrapping\data_2_all_movie.json"
    df = pd.read_json(chemin_fichier)
    return df


df = charger_json()

st.write(df)


@st.cache_data
def charger_json2():
    chemin_fichier = "..\\Scrapping\\data_commentaire_prov.json"
    df = pd.read_json(chemin_fichier)
    return df


df2 = charger_json2()

st.write(df2)
