import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")


@st.cache_data
def charger_json():
    chemin_fichier = "Scrapping\\data_2_all_movie.json"
    df = pd.read_json(chemin_fichier)
    return df


df = charger_json()

st.subheader("Représentation des relations entre les variables quantitatives")

variables = ["Budget Int", "note", "classement", "Durée min", "Année "]
axe = {
    "Budget Int": "Budget en $",
    "Durée min": "Durée en minutes",
    "Année ": "Année",
    "note": "Note",
    "classement": "classement",
}

var_select = st.multiselect(
    "Choisir deux variables pour le nuage de points :",
    variables,
    default=["Budget Int", "Année "],
)

if len(var_select) == 2:
    fig = px.scatter(
        df,
        x=var_select[0],
        y=var_select[1],
        title=f"Nuage de points de la variable {var_select[1]} en fonction de la variable {var_select[0]}",
    )
    fig.update_xaxes(title_text=axe[var_select[0]])
    fig.update_yaxes(title_text=axe[var_select[1]])
    fig.update_traces(marker=dict(color="#FF4B4B"))
    st.plotly_chart(fig)
elif len(var_select) > 2:
    st.error("Vous ne pouvez sélectionner que deux variables.")
elif len(var_select) < 2:
    st.error("Vous devez séléctionner deux variables")
