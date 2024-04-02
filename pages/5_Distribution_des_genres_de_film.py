import streamlit as st 
import pandas as pd 
import plotly.express as px
import os


st.set_page_config(layout="wide")


@st.cache_data
def charger_json():
    repertoire_base = os.getcwd()
    chemin_repertoire_scrapping = os.path.join(repertoire_base, "Scrapping")
    chemin_fichier = os.path.join(chemin_repertoire_scrapping, "data_2_all_movie.json")
    df = pd.read_json(chemin_fichier)
    return df


df = charger_json()

#Création de la base de données pour la figure
st.subheader("Distribution des genres des films")
df_somme_variables_binaires = df.iloc[:, 11:36].sum()
df_total_genre = pd.DataFrame({'Genre de film': df_somme_variables_binaires.index, 'Somme': df_somme_variables_binaires.values})
df_total_genre = df_total_genre.sort_values(by='Somme', ascending=False)

#Création de la figure
couleur_gradient = ["#FF5733", "#33FF57"]
fig = px.bar(df_total_genre, y='Genre de film', x='Somme', color='Genre de film')
fig.update_xaxes(title_text="Effectif")
fig.update_layout(title_text="Fréquence des Genres de Films")
st.plotly_chart(fig)