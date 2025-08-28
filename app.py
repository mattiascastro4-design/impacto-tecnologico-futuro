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
  if sector == "Salud":
    st.write("Aquí va información detallada sobre Salud: avances en telemedicina, IA en diagnósticos, etc.")
  elif sector == "Educación":
    st.write("Aquí va información detallada sobre Educación: e-learning, realidad virtual, personalización del aprendizaje, etc.")
  elif sector == "Transporte":
    st.write("Aquí va información detallada sobre Transporte: vehículos autónomos, drones, optimización de rutas, etc.")
  elif sector == "Empleo":
    st.write("Aquí va información detallada sobre Empleo: automatización, nuevas profesiones, teletrabajo, etc.")
else:
  st.write("Activa el filtro para ver más detalles.")
