#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from transformers import pipeline
import random

# Simulador de detección de estilos de aprendizaje
learning_styles = [
    "Visual", "Auditivo", "Kinestésico", "Lector/Escritor"
]

style_questions = {
    "Me gusta aprender viendo diagramas, gráficos o mapas": "Visual",
    "Prefiero escuchar explicaciones o grabaciones": "Auditivo",
    "Aprendo mejor escribiendo o leyendo textos": "Lector/Escritor",
    "Necesito moverme, tocar o practicar con las manos": "Kinestésico"
}

# Generador de ruta con LLM (simulado con un pipeline de texto)
generator = pipeline("text-generation", model="gpt2")  # Puedes cambiar por GPT-4 vía API

st.title("🧠 Experiencia de Aprendizaje Personalizado con IA")
st.subheader("Paso 1: Descubre tu estilo de aprendizaje")

responses = {}

with st.form("estilos"):
    for question in style_questions:
        responses[question] = st.radio(question, ["Sí", "No"])
    submitted = st.form_submit_button("Analizar estilo")

if submitted:
    style_score = {style: 0 for style in learning_styles}
    for question, answer in responses.items():
        if answer == "Sí":
            style_score[style_questions[question]] += 1
    preferred_style = max(style_score, key=style_score.get)
    st.success(f"Tu estilo de aprendizaje dominante es: **{preferred_style}**")

    st.subheader("Paso 2: Elige un contenido que quieres aprender")
    topic = st.selectbox("¿Sobre qué tema quieres aprender?", [
        "Uso de herramientas de IA para segmentar clientes y entender su comportamiento",
        "Uso de asistentes virtuales y herramientas como Zapier para automatizar embudos de ventas y seguimiento a clientes",
        "Utilización de modelos predictivos de IA para anticipar demandas y adaptar estrategias comerciales",
        "Implementación de análisis de datos en tiempo real para tomar decisiones ágiles y mejorar los resultados de ventas"
    ])

    if topic:
        st.subheader("Paso 3: Tu ruta personalizada de aprendizaje")

        # Prompt de ejemplo para generar ruta
        prompt = f"Genera una ruta de aprendizaje de 3 pasos sobre {topic} para un estudiante con estilo de aprendizaje {preferred_style}."
        route = generator(prompt, max_length=100, do_sample=True)[0]['generated_text']
        st.markdown("### 🛣️ Ruta de Aprendizaje")
        st.write(route)

        st.markdown("### 📘 Contenido generado")
        st.write(f"Aquí tienes una explicación sencilla sobre **{topic}** adaptada a tu estilo de aprendizaje:")
        if preferred_style == "Visual":
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Photosynthesis.gif/500px-Photosynthesis.gif", caption="Imagen ilustrativa")
        elif preferred_style == "Auditivo":
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        else:
            st.write(f"[Texto explicativo de muestra sobre {topic}]\n\n(En una versión real se cargaría contenido adaptado aquí).")

        st.markdown("### 🎯 Actividad de aprendizaje y evaluación")
        st.write("**Actividad:** Crea una presentación / resumen / podcast / prototipo sobre lo que aprendiste.")
        st.write("**Evaluación:** Sube tu producción, reflexiona sobre lo aprendido y responde a 3 preguntas clave:")
        st.write("1. ¿Qué aprendiste?")
        st.write("2. ¿Cómo te sentiste aprendiendo así?")
        st.write("3. ¿Qué quisieras aprender después?")

