import streamlit as st

# ------------------ Título e introducción ------------------
st.title("Impacto Tecnológico Futuro")

st.write("""
Este proyecto muestra cómo las nuevas tecnologías están transformando sectores clave como Salud, Educación, Transporte y Empleo. 
Selecciona un sector y activa la casilla para ver información detallada y una imagen representativa.
""")

# ------------------ Diccionario de textos ------------------
info_sectores = {
    "Salud": (
        "La telemedicina ha revolucionado el acceso a consultas médicas, especialmente en zonas rurales o con dificultad para desplazarse. "
        "La inteligencia artificial mejora los diagnósticos analizando imágenes médicas y detectando patrones que pueden pasar desapercibidos para el ojo humano. "
        "Además, la robótica asiste en cirugías de alta precisión, aumentando la seguridad y eficiencia de los procedimientos. "
        "La tecnología wearable permite el monitoreo constante de la salud, mejorando el cuidado preventivo."
    ),
    "Educación": (
        "El e-learning democratiza el acceso a la educación, permitiendo que personas de todo el mundo aprendan a su ritmo. "
        "La realidad virtual y aumentada crean entornos inmersivos que facilitan la comprensión de conceptos complejos. "
        "La inteligencia artificial personaliza el aprendizaje, adaptando el contenido a las necesidades y habilidades de cada estudiante, fomentando un aprendizaje más efectivo y motivador. "
        "Además, las plataformas colaborativas potencian el trabajo en equipo y el intercambio de conocimientos."
    ),
    "Transporte": (
        "Los vehículos autónomos prometen reducir accidentes de tráfico y mejorar la eficiencia en el uso de energía. "
        "Los drones se utilizan para entregas rápidas y para monitoreo en zonas difíciles de alcanzar. "
        "Las aplicaciones de optimización de rutas permiten reducir tiempos de traslado y emisiones contaminantes, fomentando un transporte más sostenible. "
        "Además, la integración de sistemas inteligentes en el transporte público mejora la experiencia del usuario y la gestión del tráfico."
    ),
    "Empleo": (
        "La automatización y la robótica están transformando sectores industriales, liberando a las personas de tareas repetitivas y peligrosas. "
        "Surgen nuevas profesiones relacionadas con la gestión de tecnologías avanzadas, análisis de datos y desarrollo de software. "
        "El teletrabajo se ha consolidado como una modalidad flexible que facilita la conciliación de la vida laboral y personal, además de reducir costos y emisiones asociadas al transporte. "
        "Sin embargo, también plantea retos en formación y adaptación."
    )
}

# ------------------ Imágenes representativas ------------------
imagenes_sectores = {
    "Salud": "https://cdn.pixabay.com/photo/2017/08/06/00/47/stethoscope-2584943_1280.jpg",
    "Educación": "https://cdn.pixabay.com/photo/2016/03/27/21/16/learn-1280976_1280.jpg",
    "Transporte": "https://cdn.pixabay.com/photo/2018/02/07/21/50/train-3139781_1280.jpg",
    "Empleo": "https://cdn.pixabay.com/photo/2015/01/08/18/29/startup-593327_1280.jpg"
}

# ------------------ Selector de sector ------------------
sector = st.selectbox("Selecciona un sector:", ["Salud", "Educación", "Transporte", "Empleo"])
st.write(f"Has seleccionado el sector: **{sector}**")

# ------------------ Checkbox para mostrar info ------------------
mostrar_info = st.checkbox("Mostrar información detallada")

if mostrar_info:
    st.subheader(f"Información detallada sobre {sector}")
    st.write(info_sectores[sector])
    st.image(
        imagenes_sectores[sector],
        caption=f"Ejemplo de tecnología en el sector {sector}",
        use_container_width=True
    )
