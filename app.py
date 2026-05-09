import streamlit as st

st.title("¡Hola desde Streamlit!")
st.subheader("Esta es mi primera aplicación web")
st.write("Si puedes ver esto, tu despliegue fue un éxito.")

nombre = st.text_input("Escribe tu nombre:")
if nombre:
    st.write(f"¡Mucho gusto, {nombre}!")
