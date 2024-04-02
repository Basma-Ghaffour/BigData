import streamlit as st
import pandas as pd
import numpy as np
import random
from streamlit_elements import elements, mui, html
import os


st.set_page_config(layout="wide", page_title="app")


@st.cache_data
def charger_json():
    repertoire_base = os.getcwd()
    chemin_repertoire_scrapping = os.path.join(repertoire_base, "Scrapping")
    chemin_fichier = os.path.join(chemin_repertoire_scrapping, "data_2_all_movie.json")
    df = pd.read_json(chemin_fichier)
    return df


df = charger_json()

df['imageRep'] = df['imageRep'].apply(lambda x: '\\'.join(x.split('\\')[-3:]))#changement du liens pour le deploiment


colonne_1, colonne_2, colonne_3 = st.columns([0.31, 0.06, 0.67])


with colonne_1:
    clef_widget_pays = hash(tuple(df.iloc[:, 37:52].columns))
    pays_select = st.multiselect(
        "Choisissez un ou plusieurs pays",
        df.iloc[:, 37:52].columns,
        key=clef_widget_pays,
    )
    # Filtrer les films pour les pays sélectionnés
    if pays_select:
        filtre_pays = set(df[df[pays_select].any(axis=1)].index.tolist())
    else:
        filtre_pays = set(
            df.index.tolist()
        )  # Affichage des films de tous les pays par défault

    # Filtre choix genres avec selection mutiple
    cle_widget_genre = hash(tuple(df.iloc[:, 11:36].columns))
    genre_select = st.multiselect(
        "Choisissez un ou plusieurs genre",
        df.iloc[:, 11:36].columns,
        key=cle_widget_genre,
    )
    if genre_select:
        filtre_genre = set(df[df[genre_select].any(axis=1)].index.tolist())
    else:
        filtre_genre = set(
            df.index.tolist()
        )  # Affichage des film de tous els genres par défault

    # Choisir un interval de l'année de sortie
    annee_min = df["Année "].min()
    annee_max = df["Année "].max()
    interval_annee_select = st.slider(
        "Choisissez un intervalle d'années",
        min_value=annee_min,
        max_value=annee_max,
        value=(annee_min, annee_max),
    )
    filtre_annee = set(
        df[
            (df["Année "] >= interval_annee_select[0])
            & (df["Année "] <= interval_annee_select[1])
        ].index.tolist()
    )

    # Choisir la durée maximale
    duree_min_min = df["Durée min"].min()
    duree_min_max = df["Durée min"].max()
    duree_max_select = st.slider(
        "Choisissez un intervalle maximal pour la durée (en min)",
        min_value=duree_min_min,
        max_value=duree_min_max,
        value=duree_min_max,
    )
    filtre_duree = set(df[df["Durée min"] <= duree_max_select].index.tolist())

    # Choisir la note minimal
    note_min_min = df["note"].min()
    note_min_max = df["note"].max()
    note_min_select = st.slider(
        "Choisissez une note minimale (sur 10)",
        min_value=note_min_min,
        max_value=note_min_max,
        value=note_min_min,
    )
    filtre_note = set(df[df["note"] >= note_min_select].index.tolist())

    # Choisir un Budget minimal
    budget_min_min = df["Budget Int"].min()
    budget_min_max = df["Budget Int"].max()
    budget_min_select = st.slider(
        "Choisissez un budget minimal (en $)",
        min_value=budget_min_min,
        max_value=budget_min_max,
        value=budget_min_min,
    )
    filtre_budget = set(df[df["Budget Int"] >= budget_min_select].index.tolist())

    # Choisir le classement minimal
    class_min_min = df["classement"].min()
    class_min_max = df["classement"].max()
    class_max_select = st.slider(
        "Choisissez un classement maximal",
        min_value=class_min_min,
        max_value=class_min_max,
        value=class_min_max,
    )
    filtre_class = set(df[df["classement"] <= class_max_select].index.tolist())

    # Selection des lignes
    intersection_indices = (
        filtre_pays
        & filtre_genre
        & filtre_duree
        & filtre_note
        & filtre_budget
        & filtre_annee
        & filtre_class
    )
    intersection_indices_list = list(intersection_indices)
    df_select = df.iloc[intersection_indices_list]
    df_select = df_select.sort_values(by="classement", ascending=True)

with colonne_2:
    st.write("")

with colonne_3:
    if not df_select.empty:
        film_select = st.selectbox("Choisissez un film", df_select["titre"])
        if film_select:
            st.markdown(
                f"<h1 style='text-align: center;'>{film_select}</h1>",
                unsafe_allow_html=True,
            )
    else:
        st.warning("Aucun film trouvé pour les critères sélectionnés.")

    colonne_11, colonne_12, colonne_13 = st.columns([0.48, 0.04, 0.48])

    with colonne_11:
        if not df_select.empty:
            chemin_image = df_select[df_select["titre"] == film_select].iloc[0][
                "imageRep"
            ]
            repertoire=os.getcwd()
            chemin_image=os.path.join(repertoire,chemin_image)
            st.image(chemin_image, caption="", width=300)

    with colonne_12:
        st.write("")

    with colonne_13:
        if not df_select.empty:
            if film_select:
                info_realisateur = df_select[df_select["titre"] == film_select].iloc[0][
                    "Réalisateur "
                ]
                info_classement = df_select[df_select["titre"] == film_select].iloc[0][
                    "classement"
                ]
                info_note = df_select[df_select["titre"] == film_select].iloc[0]["note"]
                info_duree = df_select[df_select["titre"] == film_select].iloc[0][
                    "Durée "
                ]
                info_pays = df_select[df_select["titre"] == film_select].iloc[0][
                    "Pays d'origine "
                ]
                info_genre = df_select[df_select["titre"] == film_select].iloc[0][
                    "Genre "
                ]
                info_annee = df_select[df_select["titre"] == film_select].iloc[0][
                    "Année "
                ]
                info_budget = df_select[df_select["titre"] == film_select].iloc[0][
                    "Budget Int"
                ]
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Réalisateur : {info_realisateur} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Classement : {info_classement} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Note : {info_note} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Durée : {info_duree} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Pays d\'origine : {info_pays} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Genre : {info_genre} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Année : {info_annee} </span>',
                    unsafe_allow_html=True,
                )
                st.write(
                    f'<span style="font-size:23px; font-weight: bold;">Budget : {info_budget} $</span>',
                    unsafe_allow_html=True,
                )

# st.write(df.iloc[intersection_indices_list])


@st.cache_data
def charger_json2():
    repertoire_base = os.getcwd()
    chemin_repertoire_scrapping = os.path.join(repertoire_base, "Scrapping")
    chemin_fichier = os.path.join(chemin_repertoire_scrapping, "data_commentaire_prov.json")
    df = pd.read_json(chemin_fichier)
    return df



df2 = charger_json2()

if not df_select.empty:
    if film_select:
        nombre_aleatoire = random.randint(
            0, 11
        )  # 10  commnentaire disponible pour la base de données provisoire
        df_sel = df2[df2["titre"] == film_select]
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
