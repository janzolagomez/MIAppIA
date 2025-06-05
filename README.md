# 🧠 Experiencia de Aprendizaje Personalizado con IA

Esta aplicación construida en **Streamlit** permite a estudiantes identificar su estilo de aprendizaje, elegir temas relevantes en el área de ventas e inteligencia artificial, y recibir automáticamente una ruta de aprendizaje personalizada con contenido adaptado y una actividad evaluativa.

## 🚀 ¿Qué hace esta app?

1. **Diagnóstico personalizado**: A través de un pequeño cuestionario, la app identifica el estilo de aprendizaje dominante (visual, auditivo, kinestésico, lector/escritor).
2. **Selección temática**: El estudiante elige entre temas actuales vinculados a IA aplicada a ventas.
3. **Generación automática**:
   - Ruta de aprendizaje de 3 pasos.
   - Contenido adaptado al estilo de aprendizaje.
   - Actividad de aprendizaje con evaluación reflexiva.

## 📚 Temas disponibles

- Uso de herramientas de IA para segmentar clientes.
- Automatización con asistentes virtuales (Zapier).
- Modelos predictivos para anticipar la demanda.
- Análisis de datos en tiempo real para decisiones comerciales.

## 🛠️ Tecnologías usadas

- `Python`
- `Streamlit`
- `Transformers` (pipeline de generación de texto con GPT-2)

## 📦 Requisitos

Crea un archivo `requirements.txt` con el siguiente contenido:

```txt
streamlit
transformers
torch
