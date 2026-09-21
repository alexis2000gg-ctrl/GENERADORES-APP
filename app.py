import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Gestión de Generadores", page_icon="⚡", layout="centered")

EXCEL_FILE = "Estructura_Base_Grupos.xlsx"

def get_full_data():
    grupos = pd.DataFrame([
        {
            "ID_GRUPO": "G-001",
            "NOMBRE_GRUPO": "Grupo 1 - GESAN GDDL 550 TAM",
            "MARCA": "GESAN",
            "MODELO_GRUPO": "GDDL 550 TAM",
            "MARCA_MOTOR": "VOLVO PENTA",
            "MODELO_MOTOR": "TAD1341GE",
            "ALTERNADOR": "Stamford",
            "POTENCIA_PRIME": "500 kVA / 400 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 720 A",
            "CAPACIDAD_ACEITE": "36 Litros (15W-40 VDS-3/VDS-4)",
            "CAPACIDAD_REFRIGERANTE": "44 Litros (Volvo VCS Amarillo)",
            "UBICACIÓN": "Planta General"
        },
        {
            "ID_GRUPO": "G-002",
            "NOMBRE_GRUPO": "Grupo 2 - ELECTRA MOLINS EMON-1000",
            "MARCA": "ELECTRA MOLINS S.A.",
            "MODELO_GRUPO": "EMON-1000 AUT-MP10",
            "MARCA_MOTOR": "PERKINS",
            "MODELO_MOTOR": "4008TAG1 (V8)",
            "ALTERNADOR": "STAMFORD LL 8124A",
            "POTENCIA_PRIME": "1000 kVA / 800 kW",
            "TENSIÓN_INTENSIDAD": "380 V / 1519 A",
            "CAPACIDAD_ACEITE": "127 Litros (15W-40 API CH-4/CI-4)",
            "CAPACIDAD_REFRIGERANTE": "143 Litros (Anticongelante 50%)",
            "UBICACIÓN": "Ciudad Deportiva 7 Palmas (Estadio G.C.)"
        }
    ])

    repuestos = pd.DataFrame([
        # G-001
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aceite Principal (x2)", "OEM": "Volvo 21707133", "MANN": "W 11 102/34", "FLEETGUARD": "LF16015", "DONALDSON": "P550529"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aceite Bypass (x1)", "OEM": "Volvo 21707132", "MANN": "WP 11 102/11", "FLEETGUARD": "LF9009", "DONALDSON": "P550425"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Gasoil Principal (5µ)", "OEM": "Volvo 21707134", "MANN": "WK 11 010 x", "FLEETGUARD": "FF5632", "DONALDSON": "P550881"},
        {"ID_GRUPO": "G-001", "TIPO": "Prefiltro Decantador Gasoil", "OEM": "Volvo 21380475", "MANN": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aire Principal", "OEM": "Volvo 21834205", "MANN": "C 30 1530", "FLEETGUARD": "AF26163", "DONALDSON": "P608533"},
        {"ID_GRUPO": "G-001", "TIPO": "Correa Alternador / Ventilador", "OEM": "Volvo 21408603", "MANN": "-", "FLEETGUARD": "-", "DONALDSON": "-"},
        
        # G-002
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Aceite Principal (x3-4)", "OEM": "Perkins CH10929", "MANN": "WD 13 145", "FLEETGUARD": "LF3828", "DONALDSON": "P550388"},
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Gasoil Principal", "OEM": "Perkins 26560143", "MANN": "WK 8110", "FLEETGUARD": "FF5052", "DONALDSON": "P550008"},
        {"ID_GRUPO": "G-002", "TIPO": "Prefiltro Decantador Gasoil", "OEM": "Perkins 26560201", "MANN": "-", "FLEETGUARD": "FS1251", "DONALDSON": "P551329"},
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Aire Principal (x2)", "OEM": "Perkins SEV551/4", "MANN": "C 30 850/2", "FLEETGUARD": "AF25223", "DONALDSON": "P182054"},
        {"ID_GRUPO": "G-002", "TIPO": "Diodos Rectificadores Alternador", "OEM": "Stamford RSK6001", "MANN": "-", "FLEETGUARD": "-", "DONALDSON": "-"},
        {"ID_GRUPO": "G-002", "TIPO": "Regulador Tensión AVR", "OEM": "Stamford MX321/MX341", "MANN": "-", "FLEETGUARD": "-", "DONALDSON": "-"}
    ])

    mantenimientos = pd.DataFrame([
        # G-001
        {"ID_GRUPO": "G-001", "INTERVALO": "Diario / 10 Hours", "TAREA": "Comprobar nivel de aceite, refrigerante en vaso de expansión, drenar agua del prefiltro e inspección de fugas."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Cambiar 36L aceite 15W-40 VDS-3/4. Sustituir 2 filtros aceite principales + 1 bypass. Cambiar filtros de gasoil y revisar correas."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Limpieza de radiador e intercooler. Sustituir filtro de aire. Reglaje de válvulas/taqués del motor Volvo."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 44L refrigerante Volvo VCS y manguitos de radiador."},
        
        # G-002
        {"ID_GRUPO": "G-002", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite (127L) y refrigerante (143L). Comprobar tensión de baterías 24V e inspección de fugas en bloque V8."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Cambiar 127L aceite 15W-40. Sustituir filtros de aceite Perkins CH10929 y filtros de combustible. Rearmar alarmas en cuadro AUT-MP10."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir los 2 filtros de aire de admisión (SEV551/4). Reglaje de taqués/inyectores en las 8 culatas independientes."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 143L de líquido refrigerante al 50% y limpieza del gran radiador frontal."}
    ])

    averias = pd.DataFrame([
        # G-001
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 94 / PPID 6", "SINTOMA": "Baja Presión de Gasoil (pérdida de potencia / tirones)", "SOLUCION": "Cambiar filtro principal (5µ) y prefiltro decantador. Purgar aire manualmente con bomba de cebado."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 100", "SINTOMA": "Baja Presión de Aceite (alarma y parada de emergencia)", "SOLUCION": "Comprobar nivel (36L 15W-40). Cambiar filtros principales y bypass. Inspeccionar presostato."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 110", "SINTOMA": "Alta Temperatura de Refrigerante (>98°C)", "SOLUCION": "Rellenar anticongelante Volvo VCS, soplar radiador con aire a presión y revisar tensión de correas."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 105", "SINTOMA": "Alta Temperatura en Aire de Admisión (humo negro)", "SOLUCION": "Limpiar panal intercooler Air-to-Air y apretar/cambiar manguitos post-turbo."},
        
        # G-002
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Fallo de Arranque (AUT-MP10)", "SINTOMA": "El cuadro intenta 3 arranques y bloquea el grupo", "SOLUCION": "Aire en colector V8 o prefiltro atascado. Cambiar filtro 26560143 y purgar bomba manual."},
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Alarma Alta Temp / Sobrecalentamiento", "SINTOMA": "Parada por sonda de temperatura en cuadro MP10", "SOLUCION": "Comprobar nivel en circuito de 143L. Tensar correas del ventilador y limpiar superficie del radiador."},
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Fallo de Tensión / Sin Excitación", "SINTOMA": "El motor gira a 1500 rpm pero no genera 380V", "SOLUCION": "Revisar puente de diodos RSK6001 del alternador Stamford o ajustar/sustituir AVR MX321."}
    ])
    
    return grupos, repuestos, mantenimientos, averias

def save_data(grupos, repuestos, mantenimientos, averias):
    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl") as writer:
        grupos.to_excel(writer, sheet_name="Grupos", index=False)
        repuestos.to_excel(writer, sheet_name="Repuestos", index=False)
        mantenimientos.to_excel(writer, sheet_name="Mantenimientos", index=False)
        averias.to_excel(writer, sheet_name="Averias", index=False)

def load_data():
    if os.path.exists(EXCEL_FILE):
        try:
            grupos = pd.read_excel(EXCEL_FILE, sheet_name="Grupos")
            if "ELECTRA MOLINS" in grupos.to_string():
                repuestos = pd.read_excel(EXCEL_FILE, sheet_name="Repuestos")
                mantenimientos = pd.read_excel(EXCEL_FILE, sheet_name="Mantenimientos")
                averias = pd.read_excel(EXCEL_FILE, sheet_name="Averias")
                return grupos, repuestos, mantenimientos, averias
        except Exception:
            pass
            
    grupos, repuestos, mantenimientos, averias = get_full_data()
    save_data(grupos, repuestos, mantenimientos, averias)
    return grupos, repuestos, mantenimientos, averias

st.title("⚡ Gestión de Flota de Generadores")

grupos, repuestos, mantenimientos, averias = load_data()

# Navegación Lateral
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
        
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Ficha Técnica", "📦 Repuestos", "🛠️ Mantenimiento", "🚨 Averías"])
        
        with tab1:
            st.markdown("### Datos Técnicos del Equipo")
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**ID Grupo:** `{selected_grupo['ID_GRUPO']}`")
                st.write(f"**Marca Ensamblador:** {selected_grupo['MARCA']}")
                st.write(f"**Modelo Grupo:** {selected_grupo['MODELO_GRUPO']}")
                st.write(f"**Potencia Prime:** {selected_grupo['POTENCIA_PRIME']}")
                st.write(f"**Tensión / Intensidad:** {selected_grupo.get('TENSIÓN_INTENSIDAD', 'N/D')}")
            with col2:
                st.write(f"**Marca Motor:** {selected_grupo['MARCA_MOTOR']}")
                st.write(f"**Modelo Motor:** {selected_grupo['MODELO_MOTOR']}")
                st.write(f"**Alternador:** {selected_grupo.get('ALTERNADOR', 'N/D')}")
                st.write(f"**Capacidad Aceite:** {selected_grupo['CAPACIDAD_ACEITE']}")
                st.write(f"**Capacidad Refrigerante:** {selected_grupo['CAPACIDAD_REFRIGERANTE']}")
            
            if 'UBICACIÓN' in selected_grupo and pd.notna(selected_grupo['UBICACIÓN']):
                st.info(f"**Ubicación:** {selected_grupo['UBICACIÓN']}")
                
        with tab2:
            st.markdown("### 📦 Enciclopedia de Recambios y Filtros")
            rep_m = repuestos[repuestos["ID_GRUPO"] == grupo_id]
            if rep_m.empty:
                st.info("No hay repuestos registrados para este grupo.")
            else:
                rep_display = rep_m.drop(columns=["ID_GRUPO"])
                st.dataframe(rep_display, use_container_width=True, hide_index=True)
                
        with tab3:
            st.markdown("### Plan de Mantenimiento Preventivo")
            maint_m = mantenimientos[mantenimientos["ID_GRUPO"] == grupo_id]
            if maint_m.empty:
                st.info("No hay tareas registradas para este grupo.")
            else:
                for idx, row in maint_m.iterrows():
                    with st.expander(f"⏱️ {row['INTERVALO']}"):
                        st.write(f"**Tarea:** {row['TAREA']}")
                        
        with tab4:
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
        marca = st.text_input("Marca Ensamblador", value="")
        modelo_g = st.text_input("Modelo Grupo", value="")
        marca_m = st.text_input("Marca Motor", value="")
        modelo_m = st.text_input("Modelo Motor", value="")
        alternador = st.text_input("Alternador", value="")
        potencia = st.text_input("Potencia Prime", value="")
        tension = st.text_input("Tensión / Intensidad", value="")
        aceite = st.text_input("Capacidad Aceite", value="")
        refrig = st.text_input("Capacidad Refrigerante", value="")
        ubicacion = st.text_input("Ubicación", value="")
        
        submitted = st.form_submit_button("Guardar Grupo")
        if submitted:
            new_row = pd.DataFrame([{
                "ID_GRUPO": new_id,
                "NOMBRE_GRUPO": f"{nombre} - {marca}",
                "MARCA": marca,
                "MODELO_GRUPO": modelo_g,
                "MARCA_MOTOR": marca_m,
                "MODELO_MOTOR": modelo_m,
                "ALTERNADOR": alternador,
                "POTENCIA_PRIME": potencia,
                "TENSIÓN_INTENSIDAD": tension,
                "CAPACIDAD_ACEITE": aceite,
                "CAPACIDAD_REFRIGERANTE": refrig,
                "UBICACIÓN": ubicacion
            }])
            grupos = pd.concat([grupos, new_row], ignore_index=True)
            save_data(grupos, repuestos, mantenimientos, averias)
            st.success(f"¡Grupo {new_id} guardado correctamente!")
            st.rerun()
