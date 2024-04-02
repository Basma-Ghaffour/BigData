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

st.subheader("Distribution des pays d'origine des films")

# Création de la base de données pour la carte
variables_pays = df.iloc[:, 37:53]
pays = variables_pays.columns
total_pays = variables_pays.sum()
df_carte = pd.DataFrame({"Pays": pays, "Total": total_pays})
iso_pays = {
    "Australie": "AUS",
    "République fédérale d'Allemagne": "DEU",
    "États-Unis": "USA",
    "Italie": "ITA",
    "France": "FRA",
    "Belgique": "BEL",
    "Union Soviétique": "RUS",
    "Allemagne": "DEU",
    "Canada": "CAN",
    "Japon": "JPN",
    "Corée du Sud": "KOR",
    "Hong Kong": "HKG",
    "Singapour": "SGP",
    "Espagne": "ESP",
    "Royaume-Uni": "GBR",
    "Nouvelle-Zélande": "NZL",
}
df_carte["ISO"] = df_carte["Pays"].apply(lambda x: iso_pays.get(x, ""))

#Création de la carte
couleurs = [[0.0, "#5F0000"], [0.5, "#FF4B4B"], [1.0, "#FFA5A5"]] 
fig = px.choropleth(
    df_carte,
    locations="ISO",
    color="Total",
    hover_name="Pays",
    color_continuous_scale=couleurs,  # Use custom color scale
    title="Carte du nombre de films par pays",
    template="seaborn",
)

# Création base de données pour le graphique en barre
somme_variables_binaires = df.iloc[:, 37:53].sum()
df_barre = pd.DataFrame(
    {"Pays": somme_variables_binaires.index, "Somme": somme_variables_binaires.values}
)
df_barre = df_barre.sort_values(by="Somme", ascending=False)

#Création de la figure pour le graphique en barre
couleur_gradient = ["#FF5733", "#33FF57"]
fig2 = px.bar(df_barre, y="Pays", x="Somme", color="Pays")
fig2.update_xaxes(title_text="Effectif")
fig2.update_layout(title_text="Fréquence des pays d'origine ")

#Selection de la figure
choix = ["Carte", "Graphique en barre"]
representation = st.selectbox(
    "Choisissez  une représentation pour la distribution des pays d'origine des films:",
    choix,
)

if representation == "Carte":
    st.plotly_chart(fig)

if representation == "Graphique en barre":
    st.plotly_chart(fig2)
