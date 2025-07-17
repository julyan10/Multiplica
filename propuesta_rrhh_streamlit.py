
import streamlit as st

# Título principal
st.title("📊 Propuesta: Human Resources Data Analyst – Multiplica")

# Sección: Objetivos
st.header("🎯 Objetivos como líder del proceso")
st.markdown("""
- 🛠️ **Identificar y corregir datos incorrectos** como duplicidad en la información, campos vacíos, formatos inconsistentes o registros con valores no válidos, para asegurar la integridad de la base de personas.
- 📆 **Establecer una rutina mensual de validación** por parte de las People Managers, con lineamientos claros para el ingreso y actualización de datos directamente en el HRIS, asignando responsables por región.
- 🔒 **Crear reglas de obligatoriedad y estandarización** en el HRIS (si lo permite), que eviten campos vacíos y errores de origen desde la captura del dato.
- 📡 **Garantizar información confiable para los stakeholders**, comunicando formalmente la limpieza y estandarización de los datos para apoyar decisiones estratégicas.
""")

# Sección: Mensaje a stakeholders
st.subheader("📬 Mensaje a stakeholders")
st.info("""
"Estimados Stakeholders, la base de datos ha sido depurada y estandarizada, lo que permite contar con información confiable, oportuna y lista para apoyar decisiones estratégicas sobre talento, operaciones y finanzas, fortaleciendo así una cultura organizacional basada en datos y poniendo siempre a las personas en el centro."
""")

st.write("""
Estos objetivos no sólo abordan los errores actuales en la base de datos, sino que proponen un enfoque preventivo y sostenible para el futuro. Al implementar este sistema, Multiplica podrá contar con un modelo de gestión de datos de People más robusto, que potencie la toma de decisiones informadas, promueva la eficiencia operativa y, sobre todo, respalde una experiencia coherente y humana para cada persona que hace parte del equipo.
""")

# Sección: KPIs críticos
st.header("📈 KPIs Críticos de RRHH")

st.subheader("📌 1. Tasa de rotación voluntaria")
st.markdown("""
**📐 Fórmula:** Tasa de rotación (%) = (Número de personas con estatus “Renuncia voluntaria” en el periodo / Total de personas activas en el mismo periodo) × 100  
**💡 Relevancia:** Permite al equipo C-Level y a People Global anticipar riesgos de pérdida de talento clave y evaluar la efectividad de los procesos de experiencia y retención.  
**🚀 Acción concreta:** Si la tasa aumenta en un país o unidad específica, activar un plan de revisión del clima laboral y rediseñar procesos de onboarding o gestión del talento.
""")

st.subheader("📌 2. Costo anual promedio por persona")
st.markdown("""
**📐 Fórmula:** Costo promedio anual = SUMA(Costo anual) / Número total de personas (activas o por cargo)  
**💡 Relevancia:** Informa a Finanzas y Operaciones sobre el impacto financiero de la estructura de personal y permite ajustar presupuestos o evaluar modelos de contratación.  
**🚀 Acción concreta:** Si el costo anual por persona supera el 20% respecto al promedio regional, se deberá revisar el esquema de contratación o renegociar condiciones con freelancers.
""")

st.subheader("📌 3. Tiempo promedio de permanencia (tenure)")
st.markdown("""
**📐 Fórmula:** Tenure promedio (meses) = Promedio de días laborados / 30  
**💡 Relevancia:** Brinda al Chief People Officer y al Employee Experience Lead un indicador claro sobre la estabilidad del talento y la eficacia de las iniciativas de cultura y experiencia.  
**🚀 Acción concreta:** Si el tiempo promedio de permanencia es menor a un año, se deberán implementar entrevistas de permanencia y fortalecer los procesos de acompañamiento a nuevos ingresos.
""")

# Sección final: Visualización Power BI
st.header("📊 Visualización en Power BI")

st.write("""
Como plus y verificación de las fórmulas anteriores, se generó una visualización en Power BI con la base de datos entregada, demostrando el alcance de la información.
""")

st.image("BI_People.gif", caption="Visualización de KPIs en Power BI", use_container_width=True)


