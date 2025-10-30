import streamlit as st

# Título de la aplicación
st.title("💪 Calculadora de IMC (Índice de Masa Corporal)")

# Entrada de datos: peso y altura
# Se usa 'peso_input' y 'altura_input' como variables según la instrucción
peso_input = st.number_input("Ingrese su peso (kg):", min_value=0.0, step=0.1)
altura_input = st.number_input("Ingrese su altura (m):", min_value=0.0, step=0.01)

# Calcular el IMC solo si se ingresan valores válidos
if peso_input > 0 and altura_input > 0:
    imc = peso_input / (altura_input ** 2)  # Fórmula IMC = peso / altura^2

    # Determinar categoría según el valor del IMC
    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    # Mostrar resultado con st.metric
    st.metric(label="IMC calculado", value=f"{imc:.2f}", delta=categoria)

    # Mensaje adicional según categoría
    st.write("---")  # Línea separadora
    if categoria == "Bajo peso":
        st.warning("Tu IMC indica **bajo peso**. Podrías consultar con un profesional de la salud.")
    elif categoria == "Peso normal":
        st.success("Tu IMC está dentro del **rango saludable**. ¡Sigue así!")
    elif categoria == "Sobrepeso":
        st.info("Tu IMC indica **sobrepeso**. Considera revisar tus hábitos alimenticios y actividad física.")
    else:
        st.error("Tu IMC indica **obesidad**. Es recomendable acudir a un especialista para evaluación.")
else:
    st.write("Por favor, ingresa tu peso y altura para calcular el IMC.")

# --- Fin del programa ---
# Comentarios:
# - Se usan inputs numéricos para peso y altura.
# - El cálculo se realiza solo si ambos valores son positivos.
# - El resultado se muestra con st.metric y un mensaje explicativo.
