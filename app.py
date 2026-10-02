import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Gestión de Flota - Grupos Electrógenos",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Control de Flota y Mantenimiento de Grupos Electrógenos")
st.caption("Herramienta de consulta rápida para lubricación, recambios y diagnóstico en campo.")

# -----------------------------------------------------------------------------
# BASE DE DATOS DE LA FLOTA Y RECAMBIOS
# -----------------------------------------------------------------------------

RECAMBIOS_DATA = [
    {
        "Motor": "Deutz BF 6M 1013 E",
        "Grupos": "G-006 (Carrizal), G-010 (Jinámar)",
        "Aceite Litros": "20 L (15W-40)",
        "Filtro Aceite": "Donaldson P553771 / MANN W 11 102/16 / Fleetguard LF3997",
        "Prefiltro Decantador": "Donaldson P550900 / MANN WK 10 002 z / Fleetguard FS19820",
        "Filtro Gasoil": "Donaldson P550345 / MANN WK 940/5 / Fleetguard FF5485",
        "Filtro Aire": "Donaldson P782104 / MANN C 25 710 / Fleetguard AF25708"
    },
    {
        "Motor": "Caterpillar C7.1",
        "Grupos": "G-005 (Telde Arnao), G-008 (Tamaraceite)",
        "Aceite Litros": "16.5 L (15W-40)",
        "Filtro Aceite": "CAT 1R-1807 / Donaldson P551807 / MANN W 950/38",
        "Prefiltro Decantador": "CAT 326-1644 / Donaldson P551425 / Fleetguard FS19837",
        "Filtro Gasoil": "CAT 1R-0751 / Donaldson P551315 / Fleetguard FF5324",
        "Filtro Aire": "CAT 110-6326 / Donaldson P533882 / MANN C 24 650"
    },
    {
        "Motor": "Volvo Penta TAD1341GE",
        "Grupos": "G-001, G-002 (Hoteles Dunas)",
        "Aceite Litros": "36 L (15W-40)",
        "Filtro Aceite": "Volvo 21707133 / Donaldson P550425 / MANN W 11 102/4",
        "Prefiltro Decantador": "Volvo 20808382 / Donaldson P550881 / Fleetguard FS19735",
        "Filtro Gasoil": "Volvo 22480372 / Donaldson P550529 / Fleetguard FF5507",
        "Filtro Aire": "Volvo 21702911 / Donaldson P606720 / MANN C 31 1258"
    },
    {
        "Motor": "IVECO Vector 8 / NEF",
        "Grupos": "G-003, G-004",
        "Aceite Litros": "12 L - 15 L (15W-40)",
        "Filtro Aceite": "Iveco 2992242 / Donaldson P550588 / MANN W 940/62",
        "Prefiltro Decantador": "Iveco 504033400 / Donaldson P550901 / Fleetguard FS19821",
        "Filtro Gasoil": "Iveco 1908547 / Donaldson P550388 / MANN WK 842/2",
        "Filtro Aire": "Iveco 8041407 / Donaldson P771508 / MANN C 20 500"
    },
    {
        "Motor": "Baudouin 6M16",
        "Grupos": "G-011, G-012",
        "Aceite Litros": "30 L (15W-40)",
        "Filtro Aceite": "Baudouin 15009800 / Donaldson P550938 / Fleetguard LF16015",
        "Prefiltro Decantador": "Baudouin 15009805 / Donaldson P550881 / Fleetguard FS19735",
        "Filtro Gasoil": "Baudouin 15009802 / Donaldson P550388 / MANN WK 940/2",
        "Filtro Aire": "Baudouin 15009810 / Donaldson P782106 / MANN C 27 920"
    }
]

df_recambios = pd.DataFrame(RECAMBIOS_DATA)

# -----------------------------------------------------------------------------
# MENÚ LATERAL Y NAVEGACIÓN
# -----------------------------------------------------------------------------

st.sidebar.header("🔍 Navegación")
opcion = st.sidebar.radio(
    "Selecciona una sección:",
    ["Buscador de Recambios", "Protocolo Mantenimiento Deutz", "Diagnóstico Rápido"]
)

# -----------------------------------------------------------------------------
# SECCIÓN 1: BUSCADOR DE RECAMBIOS
# -----------------------------------------------------------------------------
if opcion == "Buscador de Recambios":
    st.subheader("📦 Equivalencias de Filtros y Capacidades de Aceite")
    
    motor_sel = st.selectbox(
        "Selecciona el Motor o Ubicación:",
        df_recambios["Motor"].tolist()
    )
    
    info_motor = df_recambios[df_recambios["Motor"] == motor_sel].iloc[0]
    
    st.info(f"**Ubicación/Grupos:** {info_motor['Grupos']}")
    st.success(f"**Capacidad Cárter Aceite:** {info_motor['Aceite Litros']}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🛢️ Lubricación y Gasoil")
        st.write(f"**Filtro de Aceite:** {info_motor['Filtro Aceite']}")
        st.write(f"**Prefiltro Decantador:** {info_motor['Prefiltro Decantador']}")
        st.write(f"**Filtro Gasoil Principal:** {info_motor['Filtro Gasoil']}")
        
    with col2:
        st.markdown("### 🌬️ Admisión")
        st.write(f"**Filtro de Aire:** {info_motor['Filtro Aire']}")
        
    st.markdown("---")
    st.subheader("📋 Tabla General de Recambios de la Flota")
    st.dataframe(df_recambios, use_container_width=True)

# -----------------------------------------------------------------------------
# SECCIÓN 2: PROTOCOLO DE MANTENIMIENTO DEUTZ (BF 6M 1013 E)
# -----------------------------------------------------------------------------
elif opcion == "Protocolo Mantenimiento Deutz":
    st.subheader("🛠️ Guía de Mantenimiento: Deutz BF 6M 1013 E (G-006 / G-010)")
    
    tab1, tab2, tab3 = st.tabs(["🛢️ Aceite y Filtros", "⚓ Decantador P550900", "❄️ Refrigeración"])
    
    with tab1:
        st.markdown("""
        * **Capacidad total:** 20 Litros (Aceite 15W-40 API CI-4).
        * **Filtro de aceite:** Usar solo **MANN W 11 102/16** o **Donaldson P553771**. *(Nunca usar W 962/8 por riesgo de fuga en junta)*.
        * **Procedimiento:**
          1. Drenar cárter en caliente.
          2. Cambiar filtro de aceite aplicando película limpia en la junta de goma. Apriete a mano.
          3. Repostar 18 L iniciales, verificar nivel, arrancar 15s, parar y rellenar los 2 L restantes hasta nivel MAX.
        """)
        
    with tab2:
        st.markdown("""
        * **Referencia:** **Donaldson P550900** (Filtro decantador de papel con grifo *Twist & Drain*).
        * **Procedimiento de cambio:**
          1. **JAMÁS pre-llenar** el filtro con gasoil de garrafa para evitar contaminación de inyectores.
          2. Impregnar la junta superior de goma con gasoil limpio y roscar **totalmente seco** a mano.
          3. Aflojar purga del cabezal de aluminio y cebar con la bomba manual hasta eliminar burbujas.
          4. Apresurar purga y presurizar con 5 bombadas extra.
        """)
        
    with tab3:
        st.markdown("""
        * **Refrigerante:** Uso de anticongelante 50% orgánico (Capacidad circuito ~21L).
        * **Electroválvulas de refrigeración:** **NO LLEVA**. El control de temperatura es $100\%$ mediante termostato mecánico de cera (Apertura ~83°C - 95°C).
        * En los tests de mantenimiento, marcar **NO / No Aplica** en la casilla de electroválvula de agua.
        """)

# -----------------------------------------------------------------------------
# SECCIÓN 3: DIAGNÓSTICO RÁPIDO
# -----------------------------------------------------------------------------
elif opcion == "Diagnóstico Rápido":
    st.subheader("⚡ Rescates Frecuentes y Diagnóstico en Campo")
    
    st.error("🔴 **Fallo: Parpadeo de Luces en Cuadro / El Grupo No Arranca (Caso Jinámar G-010)**")
    st.markdown("""
    * **Causa:** Tensión fantasma de batería (marca 12.6V en reposo pero colapsa a menos de 8V al activar el solenoide de arranque).
    * **Efecto:** La placa **PRAMAC AC-01** sufre *Brown-out* (micro-reset), haciendo tiritar los relés de maniobra y disparando por error la conmutación de la tienda.
    * **Solución:** Sustituir batería de arranque de 12V.
    """)
    
    st.warning("🟠 **Fallo: Message 'CONTROL PARADO PARA REAJUST SUCESOS' (Caterpillar G-008 Tamaraceite)**")
    st.markdown("""
    * **Causa:** Parada por evento crítico grabada en la placa EMCP 4.2 (Ej: Parada de emergencia o aviso de 500 horas).
    * **Solución:**
      1. Pulsar **ACK** (campana) para silenciar la alarma.
      2. Pulsar **RESET** durante 2-3 segundos hasta limpiar pantalla.
      3. Pulsar **AUTO** para dejar en vigilancia.
    """)
