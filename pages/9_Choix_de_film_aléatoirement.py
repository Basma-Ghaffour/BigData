import streamlit as st
import pandas as pd
import numpy as np
import random
from streamlit_elements import elements, mui, html
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


df['imageRep'] = df['imageRep'].apply(lambda x: '\\'.join(x.split('\\')[-3:]))#changement du liens pour le deploiment


import random

ligne_select = df.iloc[99]
colonne_1b, colonne_2b, colonne_3b = st.columns([0.5, 0.8, 0.2])

with colonne_1b:
    st.write("")
with colonne_2b:
    bouton = st.button("Recommandation de film de façon aléatoire")

with colonne_3b:
    st.write("")

    st.write("")

st.text("")

if bouton:
    colonne_1, colonne_2, colonne_3 = st.columns([0.5, 0.01, 0.7])
    nombre_aleatoire = random.randint(0, 99)
    ligne_select = df.iloc[nombre_aleatoire]
    with colonne_1:
        repertoire=os.getcwd()
        chemin_image=os.path.join(repertoire,chemin_image)
        chemin_image=os.path.normpath(chemin_image)
        st.image(chemin_image, caption="", width=325)

    with colonne_2:
        st.write("")

    with colonne_3:
        info_realisateur = ligne_select["Réalisateur "]
        info_classement = ligne_select["classement"]
        info_note = ligne_select["note"]
        info_duree = ligne_select["Durée "]
        info_pays = ligne_select["Pays d'origine "]
        info_genre = ligne_select["Genre "]
        info_annee = ligne_select["Année "]
        info_budget = ligne_select["Budget Int"]
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Réalisateur(s) : {info_realisateur} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Classement : {info_classement} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Note : {info_note} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Durée : {info_duree} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Pay(s) d\'origine : {info_pays} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Genre(s) : {info_genre} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Année : {info_annee} </span>',
            unsafe_allow_html=True,
        )
        st.write(
            f'<span style="font-size:25px; font-weight: bold;">Budget : {info_budget} $</span>',
            unsafe_allow_html=True,
        )


# if bouton:
#   st.table(ligne_selectionnee)
@st.cache_data
def charger_json2():
    repertoire_base = os.getcwd()
    chemin_repertoire_scrapping = os.path.join(repertoire_base, "Scrapping")
    chemin_fichier = os.path.join(chemin_repertoire_scrapping, "data_commentaire_prov.json")
    df = pd.read_json(chemin_fichier)
    return df

df2 = charger_json2()

if bouton:
    nombre_aleatoire = random.randint(0, 11)  # 10 commentaire sur la
    df_sel = df2[df2["titre"] == ligne_select["titre"]]
    observation_aleatoire = df_sel.sample(n=1, random_state=random.randint(0, 100))
    commentaire_aleatoire = observation_aleatoire.iloc[0]["commentaires"]
    with elements("style_mui_sx"):
        mui.Box(
            commentaire_aleatoire,
            sx={
                "bgcolor": "background.paper",
                "boxShadow": 1,
                "borderRadius": 2,
                "p": 3,
                "minWidth": 500,
                "fontSize": 20,
            },
        )


