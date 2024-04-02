import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")

st.header("Présentation des bases de données")


@st.cache_data
def charger_json():
    repertoire_base = os.getcwd()
    chemin_repertoire_scrapping = os.path.join(repertoire_base, "Scrapping")
    chemin_fichier = os.path.join(chemin_repertoire_scrapping, "data_2_all_movie.json")
    df = pd.read_json(chemin_fichier)
    return df



df = charger_json()

st.write(df)


@st.cache_data
def charger_json2():
    repertoire_base = os.getcwd()
    chemin_repertoire_scrapping = os.path.join(repertoire_base, "Scrapping")
    chemin_fichier = os.path.join(chemin_repertoire_scrapping, "data_commentaire_prov.json")
    df = pd.read_json(chemin_fichier)
    return df


df2 = charger_json2()

st.write(df2)
