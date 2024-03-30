import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Première page")


@st.cache_data
def charger_json():
    chemin_fichier = "C:\\Users\\basma\\Desktop\\Master 2\\semestre 2\\Projet_Big_Data2\\Scrapping\\data_2_all_movie.json"
    df = pd.read_json(chemin_fichier)
    return df


df = charger_json()

st.subheader(f"Distribution des variables quantitatives")
col1, col2 = st.columns([0.5, 0.5])

variables_quantitatives = ["Budget Int", "Durée min", "Année ", "note"]
axe_x = {
    "Budget Int": "Budget en $",
    "Durée min": "Durée en minutes",
    "Année ": "Année",
    "note": "Note",
}
variable_choisie = st.selectbox(
    "Choisissez une variable quantitative :", variables_quantitatives
)

if variable_choisie:
    fig_hist = px.histogram(
        df, x=variable_choisie, nbins=50, color_discrete_sequence=["#FF4B4B"]
    )
    fig_hist.update_xaxes(title_text=axe_x[variable_choisie])
    fig_hist.update_yaxes(title_text="Effectif")
    fig_hist.update_layout(title_text=f"Distribution de la variable {variable_choisie}")
    st.plotly_chart(fig_hist)
