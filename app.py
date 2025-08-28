import streamlit as st

# Título de la app
st.title("Impacto Tecnológico Futuro")

# Descripción
st.write("""
Esta aplicación te permite explorar cómo las tecnologías emergentes impactan en diferentes sectores de la sociedad.
""")

# Selección de sector
sector = st.selectbox("Selecciona un sector", ["Salud", "Educación", "Transporte", "Empleo"])

# Visualización base
st.write(f"Has seleccionado el sector: **{sector}**")

# Filtro básico
filtro = st.checkbox("Mostrar información detallada")

if filtro:
    st.write(f"Aquí se mostrará más información sobre el sector **{sector}**.")
else:
    st.write("Activa el filtro para ver más detalles.")
