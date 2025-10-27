import streamlit as st

st.title("Calculadora de Costos")

# Inputs
costo_materiales = st.number_input("Costo de materiales ($)", min_value=0)
horas_trabajo = st.number_input("Horas de trabajo", min_value=0.0, step=0.5)
tarifa_hora = st.number_input("Tarifa por hora ($)", min_value=0)

# Procesamiento
costo_total = costo_materiales + (horas_trabajo * tarifa_hora)
precio_sugerido = costo_total * 1.5  # 50% de margen

# Output
st.metric("Costo Total", f"${costo_total:,.0f}")
st.metric("Precio Sugerido", f"${precio_sugerido:,.0f}")
