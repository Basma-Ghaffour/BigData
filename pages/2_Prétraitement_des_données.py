import streamlit as st 

st.subheader("Prétraitement des données")

st.markdown("Variables quantitatives : \n\n"
            "- Conversion de la durée en variable quantitative (en min)\n"
            "- Conversion du budget en $ pour tous les films (problèmes de conversion)\n"
            )

st.markdown("Variables qualitatives pour les pays d'origine et les genres : \n\n"
            "- Les pays d'origine des films peuvent être une liste de plusieurs pays\n"
            "- Les genres des films peuvent être une liste de plusieurs genres\n"
            "- Variables Genre et Genres (de même pour les variables Réalisateur et Réalisateurs)\n"
            "- Création de variables binaires pour chaque pays et chaque genre\n"
            )

st.markdown("Particularités : \n\n"
            "- Conservation des variables d\'origine (utile pour l'application)\n"
            "- Variable contenant pour chaque film le chemin d'un fichier (utile pour l'application) \n"
            )
