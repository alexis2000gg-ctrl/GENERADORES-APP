import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestión de Flota de Generadores", page_icon="⚡", layout="centered")

def load_data():
    grupos = pd.DataFrame([
        # G-001
        {
            "ID_GRUPO": "G-001",
            "CLIENTE": "Hoteles Dunas",
            "UBICACIÓN": "Hotel Don Gregory",
            "NOMBRE_GRUPO": "G-001 | Hotel Don Gregory (GESAN 550 kVA)",
            "MARCA": "GESAN",
            "MODELO_GRUPO": "GDDL 550 TAM",
            "SERIE_GRUPO": "S/N General",
            "MARCA_MOTOR": "VOLVO PENTA",
            "MODELO_MOTOR": "TAD1341GE",
            "SERIE_MOTOR": "TAD1341GE",
            "ALTERNADOR": "Stamford",
            "SERIE_ALTERNADOR": "S/N Stamford",
            "POTENCIA_PRIME": "550 kVA / 440 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 720 A",
            "CAPACIDAD_ACEITE": "36 Litros (15W-40 VDS-3/VDS-4)",
            "CAPACIDAD_REFRIGERANTE": "44 Litros (Volvo VCS Amarillo)",
            "CONTROLADORA": "Deep Sea Electronics DSE 7320",
            "OPERACION_CONTROLADORA": "• AUTO: Arranque automático por fallo de red.\n• MANUAL + START (I): Arranque manual de prueba.\n• STOP (O): Parada y rearmado de alarmas.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1W777DzFCpfLVeABKfcZnTJPcQbNSc5_-?usp=sharing"
        },
        # G-002
        {
            "ID_GRUPO": "G-002",
            "CLIENTE": "Hoteles Dunas",
            "UBICACIÓN": "Hotel Dunas Mirador",
            "NOMBRE_GRUPO": "G-002 | Hotel Dunas Mirador (HIMOINSA 440 kVA)",
            "MARCA": "HIMOINSA",
            "MODELO_GRUPO": "EST-STO",
            "SERIE_GRUPO": "9710001716",
            "MARCA_MOTOR": "IVECO",
            "MODELO_MOTOR": "AIFO 8281SRJ26 (V8 Turbo)",
            "SERIE_MOTOR": "385320",
            "ALTERNADOR": "MECC ALTE ECN 40 5B/4",
            "SERIE_ALTERNADOR": "706253",
            "POTENCIA_PRIME": "440 kVA / 352 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 635 A",
            "CAPACIDAD_ACEITE": "35 Litros (15W-40 ACEA E3/E5)",
            "CAPACIDAD_REFRIGERANTE": "50 Litros (Anticongelante 50%)",
            "CONTROLADORA": "Himoinsa CEC7 / Cuadro Automático",
            "OPERACION_CONTROLADORA": "• Modo AUTO: Vigilancia constante de red.\n• Pulsador RESET: Reseteo de fallos de sobretemperatura y presión.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1W777DzFCpfLVeABKfcZnTJPcQbNSc5_-?usp=sharing"
        },
        # G-003
        {
            "ID_GRUPO": "G-003",
            "CLIENTE": "Hoteles Dunas",
            "UBICACIÓN": "Hotel Maspalomas Resort",
            "NOMBRE_GRUPO": "G-003 | Hotel Maspalomas Resort (GENESAL 550 kVA)",
            "MARCA": "DEUTZ / GENESAL",
            "MODELO_GRUPO": "GDDL550",
            "SERIE_GRUPO": "1808",
            "MARCA_MOTOR": "DEUTZ",
            "MODELO_MOTOR": "BF 8 M 1015 CP (V8 Turbo Intercooler)",
            "SERIE_MOTOR": "4798/00 9146100",
            "ALTERNADOR": "LEROY SOMER LSA 47.2M7C6/4",
            "SERIE_ALTERNADOR": "158934/4",
            "POTENCIA_PRIME": "550 kVA / 440 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 793 A",
            "CAPACIDAD_ACEITE": "45 Litros (15W-40 Deutz DQC III-10)",
            "CAPACIDAD_REFRIGERANTE": "65 Litros (Circuito V8)",
            "CONTROLADORA": "Centralita Automática Genesal / DSE",
            "OPERACION_CONTROLADORA": "• Selector Manual/Auto.\n• Test en vacío semanal recomendado.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1W777DzFCpfLVeABKfcZnTJPcQbNSc5_-?usp=sharing"
        },
        # G-004
        {
            "ID_GRUPO": "G-004",
            "CLIENTE": "Hoteles Dunas",
            "UBICACIÓN": "Hotel Dunas Suites",
            "NOMBRE_GRUPO": "G-004 | Hotel Dunas Suites (CATERPILLAR 635 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "CAT 635",
            "SERIE_GRUPO": "S/N CAT",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "3412TTA (V12 Biturbo)",
            "SERIE_MOTOR": "1EZ021896",
            "ALTERNADOR": "CATERPILLAR",
            "SERIE_ALTERNADOR": "9DW00353",
            "POTENCIA_PRIME": "635 kVA / 508 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 916 A",
            "CAPACIDAD_ACEITE": "68 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "90 Litros (CAT ELC Orgánico)",
            "CONTROLADORA": "Caterpillar EMCP / Control Panel",
            "OPERACION_CONTROLADORA": "• Panel EMCP: Diagnóstico numérico por códigos CAT.\n• Pulsador Parada de Emergencia en frontal.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1W777DzFCpfLVeABKfcZnTJPcQbNSc5_-?usp=sharing"
        }
    ])

    repuestos = pd.DataFrame([
        # G-001 Volvo Penta TAD1341GE
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aceite Principal (x2)", "OEM": "Volvo 21707133", "MANN": "W 11 102/34", "FLEETGUARD": "LF16015", "DONALDSON": "P550529"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aceite Bypass (x1)", "OEM": "Volvo 21707132", "MANN": "WP 11 102/11", "FLEETGUARD": "LF9009", "DONALDSON": "P550425"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Gasoil Principal (5µ)", "OEM": "Volvo 21707134", "MANN": "WK 11 010 x", "FLEETGUARD": "FF5632", "DONALDSON": "P550881"},
        {"ID_GRUPO": "G-001", "TIPO": "Prefiltro Decantador Gasoil", "OEM": "Volvo 21380475", "MANN": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aire Principal", "OEM": "Volvo 21834205", "MANN": "C 30 1530", "FLEETGUARD": "AF26163", "DONALDSON": "P608533"},

        # G-002 IVECO AIFO 8281SRJ26 (V8)
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Aceite Principal (x2)", "OEM": "Iveco 1907584 / 2992242", "MANN": "W 11 102", "FLEETGUARD": "LF3880", "DONALDSON": "P550425"},
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Gasoil Principal (x2)", "OEM": "Iveco 1902138", "MANN": "WK 842", "FLEETGUARD": "FF5052", "DONALDSON": "P550008"},
        {"ID_GRUPO": "G-002", "TIPO": "Prefiltro Decantador Gasoil", "OEM": "Iveco 1908547", "MANN": "WK 1060", "FLEETGUARD": "FS1251", "DONALDSON": "P551329"},
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Aire Principal", "OEM": "Himoinsa 1903210", "MANN": "C 30 850/2", "FLEETGUARD": "AF25223", "DONALDSON": "P182054"},
        {"ID_GRUPO": "G-002", "TIPO": "Correa Ventilador / Alternador", "OEM": "Iveco 4841793", "MANN": "-", "FLEETGUARD": "-", "DONALDSON": "-"},

        # G-003 DEUTZ BF 8 M 1015 CP (V8)
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Aceite Principal (x2)", "OEM": "Deutz 01182912", "MANN": "W 11 102/16", "FLEETGUARD": "LF3997", "DONALDSON": "P550425"},
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Gasoil Principal (x2)", "OEM": "Deutz 01180597", "MANN": "WK 940/20", "FLEETGUARD": "FF5485", "DONALDSON": "P553004"},
        {"ID_GRUPO": "G-003", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM": "Deutz 04152512", "MANN": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010"},
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Aire Principal (V8)", "OEM": "Deutz 01180872", "MANN": "C 30 1500", "FLEETGUARD": "AF25431", "DONALDSON": "P777868"},
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Aire Seguridad (Interior)", "OEM": "Deutz 01180873", "MANN": "CF 1500", "FLEETGUARD": "AF25432", "DONALDSON": "P777869"},

        # G-004 CATERPILLAR 3412TTA (V12)
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Aceite Alta Eficiencia (x2)", "OEM": "CAT 1R-1808", "MANN": "WD 13 145/4", "FLEETGUARD": "LF9009", "DONALDSON": "P551808"},
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Gasoil Secundario (x2)", "OEM": "CAT 1R-0749", "MANN": "WK 8117", "FLEETGUARD": "FF5319", "DONALDSON": "P551315"},
        {"ID_GRUPO": "G-004", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM": "CAT 1R-0770 / 133-5673", "MANN": "WK 1080/1", "FLEETGUARD": "FS19820", "DONALDSON": "P550625"},
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Aire Principal (x2 V12)", "OEM": "CAT 6I-2505", "MANN": "C 33 920/3", "FLEETGUARD": "AF25138", "DONALDSON": "P532505"},
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Agua / Refrigerante", "OEM": "CAT 9N-3366", "MANN": "WA 940/1", "FLEETGUARD": "WF2075", "DONALDSON": "P552075"}
    ])

    mantenimientos = pd.DataFrame([
        # G-001 Volvo
        {"ID_GRUPO": "G-001", "INTERVALO": "Diario / 10 Hours", "TAREA": "Comprobar nivel de aceite, refrigerante en vaso de expansión, drenar agua del prefiltro e inspección de fugas."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Cambiar 36L aceite 15W-40 VDS-3/4. Sustituir 2 filtros aceite principales + 1 bypass. Cambiar filtros de gasoil y revisar correas."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Limpieza de radiador e intercooler. Sustituir filtro de aire. Reglaje de válvulas/taqués del motor Volvo."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 44L refrigerante Volvo VCS y manguitos de radiador."},

        # G-002 IVECO
        {"ID_GRUPO": "G-002", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite Cárter IVECO V8 (35L) y nivel de radiador. Purgar condensados de cazoleta de gasoil."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 400 Horas / 12 Meses", "TAREA": "Cambio de 35L aceite 15W-40 ACEA E3/E5. Sustituir 2 filtros de aceite W11102 y par de filtros de combustible WK 842."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 800 Horas / 2 Años", "TAREA": "Sustituir filtro de aire C 30 850/2. Ajuste de taqués en culatas de bloque V8 AIFO."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 1.500 Horas / 3 Años", "TAREA": "Cambio de refrigerante al 50% (50L) y revisión de la bomba de agua de engranajes."},

        # G-003 DEUTZ
        {"ID_GRUPO": "G-003", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Comprobar nivel de aceite Cárter DEUTZ V8 (45L) e inspeccionar manguitos de aire del intercooler."},
        {"ID_GRUPO": "G-003", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Cambiar 45L aceite Deutz DQC III-10 15W-40. Sustituir 2 filtros de aceite 01182912 y filtros de gasoil 01180597."},
        {"ID_GRUPO": "G-003", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Cambiar cartuchos de aire principal C 30 1500 y de seguridad CF 1500. Limpiar panal exterior del radiador V8."},
        {"ID_GRUPO": "G-003", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 65L de anticongelante orgánico y reglaje de los 8 inyectores bomba PLD."},

        # G-004 CATERPILLAR
        {"ID_GRUPO": "G-004", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Inspección de nivel en cárter V12 (68L CAT DEO 15W-40) y tensión de baterías de arranque 24V."},
        {"ID_GRUPO": "G-004", "INTERVALO": "Cada 250 Horas / 12 Meses", "TAREA": "Sustitución de 68L de aceite CAT DEO. Cambiar par de filtros de aceite CAT 1R-1808 y par de filtros de gasoil 1R-0749."},
        {"ID_GRUPO": "G-004", "INTERVALO": "Cada 500 Horas / 2 Años", "TAREA": "Sustituir los 2 filtros de aire principales CAT 6I-2505 y el cartucho de tratamiento de agua 9N-3366."},
        {"ID_GRUPO": "G-004", "INTERVALO": "Cada 1.500 Horas / 3 Años", "TAREA": "Sustituir 90L de líquido refrigerante CAT ELC (Extended Life Coolant) e inspección de turbocompresores gemelos."}
    ])

    averias = pd.DataFrame([
        # G-001 Volvo
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 94 / PPID 6", "SINTOMA": "Baja Presión de Gasoil (pérdida de potencia / tirones)", "SOLUCION": "Cambiar filtro principal (5µ) y prefiltro decantador. Purgar aire manualmente con bomba de cebado."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 100", "SINTOMA": "Baja Presión de Aceite (alarma y parada de emergencia)", "SOLUCION": "Comprobar nivel (36L 15W-40). Cambiar 2 filtros principales + 1 bypass. Inspeccionar presostato."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 102", "SINTOMA": "Baja Presión de Turbo / Sobrealimentación", "SOLUCION": "Revisar manguitos/abrazaderas de admisión, limpiar sensor MAP o comprobar holgura en turbocompresor."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 110", "SINTOMA": "Alta Temperatura de Refrigerante (>98°C)", "SOLUCION": "Rellenar anticongelante Volvo VCS, soplar radiador con aire a presión y revisar tensión de correas."},

        # G-002 IVECO
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Alarma Presión Aceite Cárter V8", "SINTOMA": "Caída de presión al subir temperatura de motor AIFO", "SOLUCION": "Comprobar grado de viscosidad (usar 15W-40 E3/E5). Cambiar pares de filtros W11102 o revisar válvula reguladora de bomba de aceite."},
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Sobretemperatura Agua en Culatas", "SINTOMA": "Parada por termostato en cuadro Himoinsa CEC7", "SOLUCION": "Limpiar radiador frontal bloqueado por polvo, tensar correa de la bomba de agua 4841793 o cambiar termostatos mecánicos."},
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Fallo de Inyección / Humo Blanco", "SINTOMA": "Inestabilidad en ralentí y tirones al coger carga de 440 kVA", "SOLUCION": "Sustituir cartuchos de gasoil WK 842, purgar aire en la bomba lineal Bosch e inspeccionar inyectores de la bancada V8."},

        # G-003 DEUTZ
        {"ID_GRUPO": "G-003", "CODIGO_ERROR": "Fallo Regulador Electrónico EMR", "SINTOMA": "Incapacidad para mantener 1500 rpm exactas (50 Hz)", "SOLUCION": "Revisar captador inductivo en volante de inercia, limpiar virutas y verificar actuador electromagnético de la bomba inyectora."},
        {"ID_GRUPO": "G-003", "CODIGO_ERROR": "Baja Presión de Cárter V8 Deutz", "SINTOMA": "Luz de advertencia de presión de aceite encendida en cuadro Genesal", "SOLUCION": "Sustituir inmediatamente los 2 filtros de aceite Deutz 01182912 y verificar que no hay dilución de gasoil en cárter."},
        {"ID_GRUPO": "G-003", "CODIGO_ERROR": "Alta Temperatura de Admisión", "SINTOMA": "Humo negro por el escape y reducción automática de kVA", "SOLUCION": "Limpiar panal de intercooler Air-to-Air y cambiar filtros de aire C 30 1500 / CF 1500."},

        # G-004 CATERPILLAR
        {"ID_GRUPO": "G-004", "CODIGO_ERROR": "CAT Code 39 (Presión Aceite Low)", "SINTOMA": "Parada de emergencia en panel EMCP por baja presión V12", "SOLUCION": "Comprobar nivel en cárter (68L). Cambiar la pareja de filtros CAT 1R-1808. Verificar calibración del sensor de presión de aceite."},
        {"ID_GRUPO": "G-004", "CODIGO_ERROR": "CAT Code 11 (High Coolant Temp)", "SINTOMA": "Disparo por alta temperatura en circuito V12 Biturbo", "SOLUCION": "Comprobar nivel de anticongelante CAT ELC (90L). Limpiar el radiador doble y sustituir el filtro de tratamiento de agua CAT 9N-3366."},
        {"ID_GRUPO": "G-004", "CODIGO_ERROR": "Fallo Arranque / Solenoide Combustible", "SINTOMA": "El motor gira fuerte pero no abre paso de gasoil", "SOLUCION": "Revisar fusible del solenoide de corte de combustible en el bloque 3412 y limpiar par de prefiltros CAT 1R-0770."}
    ])
    
    return grupos, repuestos, mantenimientos, averias

st.title("⚡ Gestión de Flota de Generadores")

grupos, repuestos, mantenimientos, averias = load_data()

st.sidebar.header("🏢 Filtro de Navegación")

# Filtro 1: Cliente
clientes_disponibles = grupos["CLIENTE"].unique().tolist()
selected_cliente = st.sidebar.selectbox("Selecciona Cliente:", clientes_disponibles)

# Filtro 2: Generador del Cliente
grupos_filtrados = grupos[grupos["CLIENTE"] == selected_cliente]
generadores_disponibles = grupos_filtrados["NOMBRE_GRUPO"].tolist()
selected_grupo_nombre = st.sidebar.selectbox("Selecciona Generador:", generadores_disponibles)

selected_grupo = grupos_filtrados[grupos_filtrados["NOMBRE_GRUPO"] == selected_grupo_nombre].iloc[0]
grupo_id = selected_grupo["ID_GRUPO"]

st.subheader(f"📍 {selected_grupo['UBICACIÓN']} — {selected_grupo['MARCA']}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Ficha Técnica", "📦 Repuestos", "🛠️ Mantenimiento", "🚨 Averías", "📖 Manuales"])

with tab1:
    st.markdown("### Datos Técnicos Oficiales")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Cliente / Cadena:** {selected_grupo['CLIENTE']}")
        st.write(f"**Ubicación:** {selected_grupo['UBICACIÓN']}")
        st.write(f"**ID Equipo:** `{selected_grupo['ID_GRUPO']}`")
        st.write(f"**Marca / Modelo Grupo:** {selected_grupo['MARCA']} {selected_grupo['MODELO_GRUPO']}")
        st.write(f"**Nº Serie Grupo:** `{selected_grupo['SERIE_GRUPO']}`")
        st.write(f"**Potencia Prime:** {selected_grupo['POTENCIA_PRIME']}")
        st.write(f"**Tensión / Intensidad:** {selected_grupo['TENSIÓN_INTENSIDAD']}")
    with col2:
        st.write(f"**Marca Motor:** {selected_grupo['MARCA_MOTOR']}")
        st.write(f"**Modelo Motor:** {selected_grupo['MODELO_MOTOR']}")
        st.write(f"**Nº Serie Motor:** `{selected_grupo['SERIE_MOTOR']}`")
        st.write(f"**Alternador:** {selected_grupo['ALTERNADOR']}")
        st.write(f"**Nº Serie Alternador:** `{selected_grupo['SERIE_ALTERNADOR']}`")
        st.write(f"**Capacidad Aceite:** {selected_grupo['CAPACIDAD_ACEITE']}")
        st.write(f"**Capacidad Refrigerante:** {selected_grupo['CAPACIDAD_REFRIGERANTE']}")

    st.markdown("---")
    st.markdown("### 🎛️ Centralita y Cuadro de Control")
    st.success(f"**Modelo de Controladora:** {selected_grupo.get('CONTROLADORA', 'N/D')}")
    st.write(selected_grupo.get('OPERACION_CONTROLADORA', ''))

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

with tab5:
    st.markdown("### 📖 Manuales y Documentación Taller")
    st.write("Acceso a la carpeta compartida de Google Drive del cliente:")
    st.link_button(f"📂 Abrir Carpeta de Manuales en Google Drive (Hoteles Dunas)", selected_grupo["MANUAL_URL"])
