import openai
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
import streamlit as st

# Configura tu API Key directamente
openai.api_key = "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"

# Título de la página
st.title("Prompting con OpenAI - Few-Shot y Chain of Thought")

# Cargar datos desde un CSV
file_path = st.file_uploader("Sube tu archivo CSV", type=["csv"])
if file_path is not None:
    data = pd.read_csv(file_path)

    st.write("Datos cargados exitosamente:", data.head())

    # Opción para elegir entre Few-Shot y Chain of Thought
    option = st.selectbox("Elige el tipo de prompting", ["Few-Shot", "Chain of Thought"])

    if option == "Few-Shot":
        st.subheader("Implementación de Few-Shot Prompting")

        def few_shot_duration_classification(model, duration):
            messages = [
                {"role": "system", "content": "Eres un asistente que clasifica la duración de carga en 'Short', 'Medium', o 'Long'."},
                {"role": "user", "content": "Clasifica la duración de carga de los vehículos según el tiempo promedio. Responde solo con una palabra: 'Short', 'Medium', o 'Long'."},
                {"role": "user", "content": "El modelo Tesla Model 3 tiene una duración promedio de carga de 1.5 horas."},
                {"role": "assistant", "content": "Short"},
                {"role": "user", "content": "El modelo Nissan Leaf tiene una duración promedio de carga de 3.0 horas."},
                {"role": "assistant", "content": "Medium"},
                {"role": "user", "content": "El modelo Audi e-tron tiene una duración promedio de carga de 5.0 horas."},
                {"role": "assistant", "content": "Long"},
                {"role": "user", "content": f"El modelo {model} tiene una duración promedio de carga de {duration} horas."}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=messages,
                max_tokens=10,
                temperature=0.0
            )

            return response.choices[0].message["content"].strip()

        if st.button("Clasificar Duración de Carga"):
            st.write("Clasificando las duraciones de carga...")
            data['Prediction'] = data.apply(lambda row: few_shot_duration_classification(row['Vehicle Model'], row['Charging Duration']), axis=1)

            data['True Classification'] = data['True Classification'].str.strip().str.lower()
            data['Prediction'] = data['Prediction'].str.strip().str.lower()

            st.write("Reporte de clasificación:")
            st.text(classification_report(data['True Classification'], data['Prediction']))

            accuracy = accuracy_score(data['True Classification'], data['Prediction'])
            st.write(f"Accuracy: {accuracy:.2f}")

    elif option == "Chain of Thought":
        st.subheader("Implementación de Chain of Thought Prompting")

        prompt = """
        Los datos incluyen información sobre vehículos eléctricos, estaciones de carga, y sesiones de carga.
        Quiero validar esta hipótesis:
        "Las estaciones de carga con mayor ventas."
        Desglosa paso a paso cómo analizar esto:
        1. ¿Qué columnas son necesarias?
        2. ¿Qué pasos debo seguir para calcularlo?
        3. ¿Qué métricas puedo usar para comprobar esta hipótesis?
        Responde razonando paso a paso.
        """

        if st.button("Analizar con Chain of Thought"):
            st.write("Desglosando análisis de la hipótesis...")
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            st.write("Respuesta:", response.choices[0].message["content"])
