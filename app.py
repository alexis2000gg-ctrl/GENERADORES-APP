import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Gestión de Generadores", page_icon="⚡", layout="centered")

EXCEL_FILE = "Estructura_Base_Grupos.xlsx"

def load_data():
    if os.path.exists(EXCEL_FILE):
        grupos = pd.read_excel(EXCEL_FILE, sheet_name="Grupos")
        mantenimientos = pd.read_excel(EXCEL_FILE, sheet_name="Mantenimientos")
        averias = pd.read_excel(EXCEL_FILE, sheet_name="Averias")
    else:
        # Default data if file not found
        grupos = pd.DataFrame([{
            "ID_GRUPO": "G-001",
            "NOMBRE_GRUPO": "Grupo 1 - GESAN",
            "MARCA": "GESAN",
            "MODELO_GRUPO": "GDDL 550 TAM",
            "MARCA_MOTOR": "VOLVO PENTA",
            "MODELO_MOTOR": "TAD1341GE",
            "POTENCIA_PRIME": "500 kVA / 400 kW",
            "CAPACIDAD_ACEITE": "36 Litros (15W-40 VDS-3)",
            "CAPACIDAD_REFRIGERANTE": "44 Litros"
        }])
        mantenimientos = pd.DataFrame([{
            "ID_MANTENIMIENTO": "M-001",
            "ID_GRUPO": "G-001",
            "INTERVALO": "Diario / 10h",
            "TAREA": "Inspección visual general y nivel de aceite"
        }])
        averias = pd.DataFrame([{
            "ID_AVERIA": "A-001",
            "ID_GRUPO": "G-001",
            "CODIGO_ERROR": "PID 94",
            "SINTOMA": "Baja Presión de Gasoil",
            "SOLUCION": "Sustituir filtro principal (5µ) y prefiltro decantador"
        }])
    return grupos, mantenimientos, averias

def save_data(grupos, mantenimientos, averias):
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl") as writer:
        grupos.to_excel(writer, sheet_name="Grupos", index=False)
        mantenimientos.to_excel(writer, sheet_name="Mantenimientos", index=False)
        averias.to_excel(writer, sheet_name="Averias", index=False)

st.title("⚡ Gestión de Generadores")

grupos, mantenimientos, averias = load_data()

# Navigation / Selection
st.sidebar.header("Navegación")
option = st.sidebar.radio("Ir a:", ["Ver Generadores", "➕ Añadir Nuevo Grupo"])

if option == "Ver Generadores":
    if grupos.empty:
        st.warning("No hay grupos registrados.")
    else:
        grupo_names = grupos["NOMBRE_GRUPO"].tolist()
        selected_name = st.selectbox("Selecciona un Generador:", grupo_names)
        
        selected_grupo = grupos[grupos["NOMBRE_GRUPO"] == selected_name].iloc[0]
        grupo_id = selected_grupo["ID_GRUPO"]
        
        st.subheader(f"📍 {selected_grupo['NOMBRE_GRUPO']}")
        
        tab1, tab2, tab3 = st.tabs(["📋 Ficha Técnica", "🛠️ Mantenimiento", "🚨 Averías"])
        
        with tab1:
            st.markdown("### Datos del Equipo")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**ID Grupo:** {selected_grupo['ID_GRUPO']}")
                st.write(f"**Marca:** {selected_grupo['MARCA']}")
                st.write(f"**Modelo Grupo:** {selected_grupo['MODELO_GRUPO']}")
                st.write(f"**Potencia Prime:** {selected_grupo['POTENCIA_PRIME']}")
            with col2:
                st.write(f"**Marca Motor:** {selected_grupo['MARCA_MOTOR']}")
                st.write(f"**Modelo Motor:** {selected_grupo['MODELO_MOTOR']}")
                st.write(f"**Capacidad Aceite:** {selected_grupo['CAPACIDAD_ACEITE']}")
                st.write(f"**Capacidad Refrigerante:** {selected_grupo['CAPACIDAD_REFRIGERANTE']}")
                
        with tab2:
            st.markdown("### Plan de Mantenimiento Preventivo")
            maint_m = mantenimientos[mantenimientos["ID_GRUPO"] == grupo_id]
            if maint_m.empty:
                st.info("No hay tareas registradas para este grupo.")
            else:
                for idx, row in maint_m.iterrows():
                    with st.expander(f"⏱️ {row['INTERVALO']}"):
                        st.write(f"**Tarea:** {row['TAREA']}")
                        
        with tab3:
            st.markdown("### Guía de Averías y Diagnóstico")
            aver_m = averias[averias["ID_GRUPO"] == grupo_id]
            if aver_m.empty:
                st.info("No hay averías registradas para este grupo.")
            else:
                for idx, row in aver_m.iterrows():
                    with st.expander(f"🔴 {row['CODIGO_ERROR']} - {row['SINTOMA']}"):
                        st.write(f"**Solución de taller:** {row['SOLUCION']}")

elif option == "➕ Añadir Nuevo Grupo":
    st.subheader("Registrar Nuevo Generador")
    with st.form("nuevo_grupo_form"):
        new_id = f"G-{len(grupos)+1:03d}"
        nombre = st.text_input("Nombre / Referencia", value=f"Grupo {len(grupos)+1}")
        marca = st.text_input("Marca Grupo", value="")
        modelo_g = st.text_input("Modelo Grupo", value="")
        marca_m = st.text_input("Marca Motor", value="")
        modelo_m = st.text_input("Modelo Motor", value="")
        potencia = st.text_input("Potencia Prime", value="")
        aceite = st.text_input("Capacidad Aceite", value="")
        refrig = st.text_input("Capacidad Refrigerante", value="")
        
        submitted = st.form_submit_button("Guardar Grupo")
        if submitted:
            new_row = pd.DataFrame([{
                "ID_GRUPO": new_id,
                "NOMBRE_GRUPO": f"{nombre} - {marca}",
                "MARCA": marca,
                "MODELO_GRUPO": modelo_g,
                "MARCA_MOTOR": marca_m,
                "MODELO_MOTOR": modelo_m,
                "POTENCIA_PRIME": potencia,
                "CAPACIDAD_ACEITE": aceite,
                "CAPACIDAD_REFRIGERANTE": refrig
            }])
            grupos = pd.concat([grupos, new_row], ignore_index=True)
            save_data(grupos, mantenimientos, averias)
            st.success(f"¡Grupo {new_id} guardado correctamente!")
            st.rerun()
