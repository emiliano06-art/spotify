import os
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageOps

st.set_page_config(page_title="Spotify Clone", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #121212; color: white; }
    [data-testid="stSidebar"] { background-color: #000000; }
    h1, h2, h3, p, label, span { color: white !important; }
    .stButton > button {
        background-color: #1DB954; color: black; border: none;
        border-radius: 500px; font-weight: bold; padding: 0.4rem 1.5rem;
    }
    .stButton > button:hover { background-color: #1ed760; color: black; }
</style>
""", unsafe_allow_html=True)

canciones = [
    {"titulo": "Luther", "artista": "Kendrick Lamar y SZA", "genero": "Hip hop",
     "archivo": "luther.mp3", "portada": "luther.jpg",
     "spotify": "45J4avUb9Ni0bnETYaYFVJ"},
    {"titulo": "Hablan mal de mi", "artista": "Yandel", "genero": "Reggaeton",
     "archivo": "hablan_mal_de_mi.mp3", "portada": "hablan_mal_de_mi.jpg",
     "spotify": "1b4pDHikv9vOImTp5DgESJ"},
    {"titulo": "Dont Be Dumb", "artista": "A$AP Rocky", "genero": "Hip hop",
     "archivo": "dont_be_dumb.mp3", "portada": "dont_be_dumb.jpg",
     "spotify": "2JfyjfqbQrTXMzH8n0fOht"},
    {"titulo": "Solo guapo y cachondo", "artista": "Yeyo", "genero": "Urbano",
     "archivo": "solo_guapo_y_cachondo.mp3", "portada": "solo_guapo_y_cachondo.jpg",
     "spotify": "2TGmtUeiETXlrvUS6AsUNu"}
]

def ruta(c):
    return os.path.join("musica", c["archivo"])

def portada(c, i):
    p = os.path.join("portadas", c["portada"])
    if os.path.exists(p):
        img = Image.open(p).convert("RGB")
        return ImageOps.fit(img, (300, 300))
    return f"https://picsum.photos/seed/{i + 10}/300"

if "actual" not in st.session_state:
    st.session_state.actual = None
if "favoritas" not in st.session_state:
    st.session_state.favoritas = []

st.sidebar.title("Spotify")
menu = st.sidebar.radio("Menu", ["Inicio", "Buscar", "Tus favoritas"])

if menu == "Inicio":
    cols = st.columns(len(canciones))
    for i, c in enumerate(canciones):
        with cols[i]:
            st.image(portada(c, i), use_container_width=True)
            st.markdown(f"**{c['titulo']}**")
            st.caption(c["artista"])
            if st.button("Play", key=f"play{i}"):
                st.session_state.actual = i
            if st.button("Favorita", key=f"fav{i}"):
                if c["titulo"] not in st.session_state.favoritas:
                    st.session_state.favoritas.append(c["titulo"])

elif menu == "Buscar":
    st.title("Buscar")
    texto = st.text_input("Que quieres escuchar?")
    for i, c in enumerate(canciones):
        if texto.lower() in c["titulo"].lower() or texto.lower() in c["artista"].lower():
            col0, col1, col2 = st.columns([1, 4, 1])
            col0.image(portada(c, i), width=70)
            col1.markdown(f"**{c['titulo']}** - {c['artista']} - _{c['genero']}_")
            if col2.button("Play", key=f"b{i}"):
                st.session_state.actual = i

elif menu == "Tus favoritas":
    st.title("Tus favoritas")
    if st.session_state.favoritas:
        for f in st.session_state.favoritas:
            st.write(f"- {f}")
    else:
        st.info("Aun no tienes canciones favoritas.")

st.divider()
if st.session_state.actual is not None:
    i = st.session_state.actual
    c = canciones[i]
    st.markdown(f"### Reproduciendo: {c['titulo']} - {c['artista']}")
    if c.get("spotify"):
        components.iframe(
            "https://open.spotify.com/embed/track/" + c["spotify"],
            height=152,
        )
    elif os.path.exists(ruta(c)):
        with open(ruta(c), "rb") as f:
            st.audio(f.read(), format="audio/mp3")
    else:
        st.warning("No se encontro el archivo: " + ruta(c))
else:
    st.markdown("### Selecciona una cancion para reproducir")



# estructura: app.py, carpeta portadas y requirements.txt

# sidebar: menu lateral con Inicio, Buscar y Tus favoritas
