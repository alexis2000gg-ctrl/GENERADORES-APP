import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestión de Flota de Generadores", page_icon="⚡", layout="centered")

def load_data():
    grupos = pd.DataFrame([
        # --- HOTELES DUNAS ---
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
            "MODELO_GRUPO": "GDDL 550 AM",
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
            "CONTROLADORA": "GENESAL Ge2000",
            "OPERACION_CONTROLADORA": "• AUTO / MAN: Selecciona el modo de trabajo.\n• ARRANQUE (Verde) / STOP (Rojo): Arranque/Parada manual de taller.\n• STOP (Rojo): Mantenido borra y resetea las alarmas.\n• Control Manual KG (V/G): Conmutación manual de contactores Red/Grupo.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1W777DzFCpfLVeABKfcZnTJPcQbNSc5_-?usp=sharing"
        },
        # G-004
        {
            "ID_GRUPO": "G-004",
            "CLIENTE": "Hoteles Dunas",
            "UBICACIÓN": "Hotel Dunas Suites",
            "NOMBRE_GRUPO": "G-004 | Hotel Dunas Suites (CATERPILLAR 635 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "CAT 3412",
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
            "CONTROLADORA": "Caterpillar EMCP II / EMCP Control Panel",
            "OPERACION_CONTROLADORA": "• RUN / AUTO / OFF: Selector principal de modo.\n• ENGINE CONTROL SWITCH: Posición RUN para arranque manual inmediato.\n• ALARM RESET: Pulsador amarillo/rojo para borrar códigos de falla en pantalla.\n• DISPLAY SCROLL: Navega entre presión de aceite, temp. agua y horómetro.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1W777DzFCpfLVeABKfcZnTJPcQbNSc5_-?usp=sharing"
        },
        # --- LIDL ---
        # G-005
        {
            "ID_GRUPO": "G-005",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Telde Arnao (Gran Canaria)",
            "NOMBRE_GRUPO": "G-005 | LIDL Telde Arnao (CAT 217.5 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE220GC",
            "SERIE_GRUPO": "CATDE220JN7500106",
            "MARCA_MOTOR": "CATERPILLAR (Perkins)",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L)",
            "SERIE_MOTOR": "KRG09407 (Arrangement: 605-2287)",
            "ALTERNADOR": "CATERPILLAR Series SR500 (A2637L41)",
            "SERIE_ALTERNADOR": "N7L00267",
            "POTENCIA_PRIME": "217.5 kVA / 174 kW (Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 314 A (1500 RPM)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "27 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar GCCP 1.2 (Base DSE 4520 MKII)",
            "OPERACION_CONTROLADORA": "• Modo AUTO: Supervisión automática de red e integración con conmutación.\n• Modo MANUAL (Mano) + ARRANQUE (Verde / I): Prueba manual de taller a pie de máquina.\n• Modo STOP / RESET (Rojo / O): Detención del motor y rearme/borrado de códigos de alarma.\n• Navegación (Flechas): Desplazamiento por pantalla LCD para presión de aceite, temp. agua, voltaje y horómetro.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-006
        {
            "ID_GRUPO": "G-006",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Ingenio Carrizal (Gran Canaria)",
            "NOMBRE_GRUPO": "G-006 | LIDL Ingenio Carrizal (PRAMAC 141 kVA)",
            "MARCA": "PRAMAC",
            "MODELO_GRUPO": "GSW145 (SC131TDAV0C)",
            "SERIE_GRUPO": "PEE2455203 (Año 2009)",
            "MARCA_MOTOR": "DEUTZ",
            "MODELO_MOTOR": "BF 6M 1013 E (128 kW / 172 HP)",
            "SERIE_MOTOR": "10793881",
            "ALTERNADOR": "STAMFORD UCI 274E",
            "SERIE_ALTERNADOR": "X08B080125",
            "POTENCIA_PRIME": "134.88 kVA / 107.9 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 204.61 A (50 Hz)",
            "CAPACIDAD_ACEITE": "20 Litros (15W-40 Deutz DQC II/III)",
            "CAPACIDAD_REFRIGERANTE": "27 Litros (Anticongelante Orgánico 50%)",
            "CONTROLADORA": "PRAMAC GC M02-C",
            "OPERACION_CONTROLADORA": "• Selector Rotativo 'A': Funcionamiento Automático por fallo de red.\n• Selector Rotativo 'Candado': Cuadro Desconectado / OFF.\n• Selector Rotativo 'Mano': Arranque manual usando el botón verde START.\n• Botón SILENT RESET (Azul): Reconoce pitido y rearma fallos en el display LCD.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-007
        {
            "ID_GRUPO": "G-007",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Telde Cruce de Melenara (Gran Canaria)",
            "NOMBRE_GRUPO": "G-007 | LIDL Cruce de Melenara (CAT 165 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE165E0",
            "SERIE_GRUPO": "CAT00C7166TPO1987",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L Turbo Intercooler)",
            "SERIE_MOTOR": "KRG06549",
            "ALTERNADOR": "CAT / Leroy Somer Series (R2453L4)",
            "SERIE_ALTERNADOR": "LWK03533",
            "POTENCIA_PRIME": "150 kVA / 120 kW (165 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 50 Hz (1500 RPM)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "21 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar GCCP 1.2 / 1.3",
            "OPERACION_CONTROLADORA": "• Pantalla LCD con control automático por fallo de red.\n• Pulsador Modo Manual / Modo Auto.\n• Botón Stop / Reset para rearme de alarmas de motor.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-008
        {
            "ID_GRUPO": "G-008",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Tamaraceite (Gran Canaria)",
            "NOMBRE_GRUPO": "G-008 | LIDL Tamaraceite (CAT 200 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE200E0",
            "SERIE_GRUPO": "CAT00C71KGTPO1940",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L Turbo Intercooler)",
            "SERIE_MOTOR": "KRG07318",
            "ALTERNADOR": "CAT Series",
            "SERIE_ALTERNADOR": "LWK03290",
            "POTENCIA_PRIME": "180 kVA / 144 kW (200 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 288 A (50 Hz)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "21 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar EMCP 4.2",
            "OPERACION_CONTROLADORA": "• AUTO: Pulsador para dejar en vigilancia de red de la tienda.\n• RUN: Arranque manual directo.\n• STOP: Detención del equipo.\n• ACK/RESET (Campana amarilla): Silencia la sirena y rearma fallos mostrados en la pantalla antes de un nuevo intento.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-009
        {
            "ID_GRUPO": "G-009",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Miller Bajo (Gran Canaria)",
            "NOMBRE_GRUPO": "G-009 | LIDL Miller Bajo (CAT 165 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE165E0",
            "SERIE_GRUPO": "CAT00C71GTP01451",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L Turbo Intercooler)",
            "SERIE_MOTOR": "KRG05294",
            "ALTERNADOR": "CAT Series (LWK)",
            "SERIE_ALTERNADOR": "S/N LWK",
            "POTENCIA_PRIME": "150 kVA / 120 kW (165 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 50 Hz (1500 RPM)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "21 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar GCCP / EMCP",
            "OPERACION_CONTROLADORA": "• Modo Automático: Supervisión de red de tienda.\n• Modo Manual / Run: Arranque directo de prueba.\n• Botón Stop / Reset: Rearme y borrado de alarmas.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-010
        {
            "ID_GRUPO": "G-010",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Jinámar (Gran Canaria)",
            "NOMBRE_GRUPO": "G-010 | LIDL Jinámar (PRAMAC 141 kVA)",
            "MARCA": "PRAMAC",
            "MODELO_GRUPO": "GEW145 / GSW145",
            "SERIE_GRUPO": "PEE24405D4",
            "MARCA_MOTOR": "DEUTZ",
            "MODELO_MOTOR": "BF 6M 1013 E (128 kW / 172 HP)",
            "SERIE_MOTOR": "S/N Deutz 1013",
            "ALTERNADOR": "STAMFORD UCI 274 E1",
            "SERIE_ALTERNADOR": "S/N Stamford",
            "POTENCIA_PRIME": "134.88 kVA / 107.9 kW",
            "TENSIÓN_INTENSIDAD": "400 V / 204.61 A (50 Hz)",
            "CAPACIDAD_ACEITE": "20 Litros (15W-40 Deutz DQC II/III)",
            "CAPACIDAD_REFRIGERANTE": "27 Litros (Anticongelante Orgánico 50%)",
            "CONTROLADORA": "PRAMAC AC21-MP (Panel ACP Automático)",
            "OPERACION_CONTROLADORA": "• Modo Automático: Supervisión constante de red de la tienda.\n• Controles Manuales / Start / Stop en frontal del cuadro ACP.\n• Pulsador de Reset de Alarma: Rearme de fallos de presión o temperatura.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-011
        {
            "ID_GRUPO": "G-011",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Maspalomas (Gran Canaria)",
            "NOMBRE_GRUPO": "G-011 | LIDL Maspalomas (PRAMAC 291 kVA)",
            "MARCA": "PRAMAC",
            "MODELO_GRUPO": "GDW295B/FNE (BC261TFA007)",
            "SERIE_GRUPO": "4925D001608",
            "MARCA_MOTOR": "BAUDOUIN",
            "MODELO_MOTOR": "6M16G6D0/S (9.72L - 6L Turbo)",
            "SERIE_MOTOR": "4925D001608",
            "ALTERNADOR": "MECC ALTE ECO 38 1L4C",
            "SERIE_ALTERNADOR": "H116206",
            "POTENCIA_PRIME": "265 kVA / 212 kW (291 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 50 Hz (1500 RPM)",
            "CAPACIDAD_ACEITE": "24 Litros (15W-40 API CF/E7 Baudouin)",
            "CAPACIDAD_REFRIGERANTE": "35 Litros (Anticongelante Orgánico 50%)",
            "CONTROLADORA": "Deep Sea Electronics DSE 7320 MKII",
            "OPERACION_CONTROLADORA": "• Modo AUTO: Vigilancia de red y arranque automático ante fallo de suministro.\n• Modo MANUAL + START (Verde): Arranque directo de prueba desde el frontal.\n• STOP / RESET (Rojo): Detención del grupo y borrado de fallos de la centralita DSE.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-012
        {
            "ID_GRUPO": "G-012",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Antigua El Castillo (Fuerteventura)",
            "NOMBRE_GRUPO": "G-012 | LIDL Antigua El Castillo (CAT 165 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE165E0",
            "SERIE_GRUPO": "CAT00C71TGTPG1918",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L Turbo Intercooler)",
            "SERIE_MOTOR": "KRG06839",
            "ALTERNADOR": "CAT Series (LWK)",
            "SERIE_ALTERNADOR": "LWK03150",
            "POTENCIA_PRIME": "150 kVA / 120 kW (165 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 50 Hz (1500 RPM)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "21 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar EMCP 4.1",
            "OPERACION_CONTROLADORA": "• AUTO: Vigilancia automática de red de tienda.\n• RUN: Arranque manual directo de prueba.\n• STOP: Detención del equipo.\n• ACK/RESET (Campana): Reconocimiento y rearme de fallos en pantalla LCD de la EMCP 4.1.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-013
        {
            "ID_GRUPO": "G-013",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Corralejo El Guirre (Fuerteventura)",
            "NOMBRE_GRUPO": "G-013 | LIDL Corralejo El Guirre (CAT 200 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE200E0",
            "SERIE_GRUPO": "CAT00C71PECW04376",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L Turbo Intercooler)",
            "SERIE_MOTOR": "KRG08445",
            "ALTERNADOR": "CAT Series (LWK)",
            "SERIE_ALTERNADOR": "LWK04671",
            "POTENCIA_PRIME": "180 kVA / 144 kW (200 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 288 A (50 Hz)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "21 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar EMCP 4.2",
            "OPERACION_CONTROLADORA": "• AUTO: Pulsador para dejar en vigilancia de red de la tienda.\n• RUN: Arranque manual directo.\n• STOP: Detención del equipo.\n• ACK/RESET (Campana amarilla): Silencia la sirena y rearma fallos mostrados en la pantalla antes de un nuevo intento.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-014
        {
            "ID_GRUPO": "G-014",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Puerto del Rosario (Fuerteventura)",
            "NOMBRE_GRUPO": "G-014 | LIDL Puerto del Rosario (CAT 220 kVA)",
            "MARCA": "CATERPILLAR",
            "MODELO_GRUPO": "DE220E0",
            "SERIE_GRUPO": "CAT00C71KECW04377",
            "MARCA_MOTOR": "CATERPILLAR",
            "MODELO_MOTOR": "C7.1 (7.01L - 6L Turbo Intercooler)",
            "SERIE_MOTOR": "KRG08402",
            "ALTERNADOR": "CAT Series (LWK)",
            "SERIE_ALTERNADOR": "LWK04596",
            "POTENCIA_PRIME": "200 kVA / 160 kW (220 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 318 A (50 Hz)",
            "CAPACIDAD_ACEITE": "16.5 Litros (CAT DEO 15W-40)",
            "CAPACIDAD_REFRIGERANTE": "21 Litros (CAT ELC)",
            "CONTROLADORA": "Caterpillar EMCP 4.2",
            "OPERACION_CONTROLADORA": "• AUTO: Pulsador para dejar en vigilancia de red de la tienda.\n• RUN: Arranque manual directo.\n• STOP: Detención del equipo.\n• ACK/RESET (Campana amarilla): Silencia la sirena y rearma fallos mostrados en la pantalla antes de un nuevo intento.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        },
        # G-015
        {
            "ID_GRUPO": "G-015",
            "CLIENTE": "LIDL",
            "UBICACIÓN": "LIDL Playa Blanca (Lanzarote)",
            "NOMBRE_GRUPO": "G-015 | LIDL Playa Blanca (GENESAL 220 kVA)",
            "MARCA": "GENESAL ENERGY",
            "MODELO_GRUPO": "GEN220YI",
            "SERIE_GRUPO": "S/N Genesal",
            "MARCA_MOTOR": "BAUDOUIN",
            "MODELO_MOTOR": "6M16G2D0/S (9.72L - 6L Turbo)",
            "SERIE_MOTOR": "4924A000295",
            "ALTERNADOR": "Stamford / Mecc Alte",
            "SERIE_ALTERNADOR": "S/N Alternador",
            "POTENCIA_PRIME": "200 kVA / 160 kW (220 kVA Standby)",
            "TENSIÓN_INTENSIDAD": "400/230 V / 50 Hz (1500 RPM)",
            "CAPACIDAD_ACEITE": "24 Litros (15W-40 API CF/E7 Baudouin)",
            "CAPACIDAD_REFRIGERANTE": "35 Litros (Anticongelante Orgánico 50%)",
            "CONTROLADORA": "Genesal GEINTEL 2",
            "OPERACION_CONTROLADORA": "• Modo AUTO: Vigilancia constante de red y arranque automático por fallo de suministro.\n• Modo MAN: Arranque y parada manual desde el frontal del cuadro.\n• STOP / RESET: Detención del equipo y borrado/rearme de alarmas en la centralita GEINTEL 2.",
            "MANUAL_URL": "https://drive.google.com/drive/folders/1DVh1bQ7P-NyBA3c6FKZcKC-SMR_JvQJf?usp=sharing"
        }
    ])

    repuestos = pd.DataFrame([
        # G-001 Volvo Penta TAD1341GE
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aceite Principal (x2)", "OEM / ORIGINAL": "Volvo 21707133", "MANN-FILTER": "W 11 102/34", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230 / 901-102", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aceite Bypass (x1)", "OEM / ORIGINAL": "Volvo 21707132", "MANN-FILTER": "WP 11 102/11", "FLEETGUARD": "LF9009", "DONALDSON": "P550425", "FG WILSON": "10000-51231 / 901-103", "BALDWIN / OTRAS": "BALDWIN B7225"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Gasoil Principal (5µ)", "OEM / ORIGINAL": "Volvo 21707134", "MANN-FILTER": "WK 11 010 x", "FLEETGUARD": "FF5632", "DONALDSON": "P550881", "FG WILSON": "10000-59651 / 901-248", "BALDWIN / OTRAS": "BALDWIN BF7814"},
        {"ID_GRUPO": "G-001", "TIPO": "Prefiltro Decantador Gasoil", "OEM / ORIGINAL": "Volvo 21380475", "MANN-FILTER": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010", "FG WILSON": "10000-12609 / 901-228", "BALDWIN / OTRAS": "BALDWIN BF1385-SPS"},
        {"ID_GRUPO": "G-001", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "Volvo 21834205", "MANN-FILTER": "C 30 1530", "FLEETGUARD": "AF26163", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS5387"},

        # G-002 IVECO AIFO 8281SRJ26 (V8)
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Aceite Principal (x2)", "OEM / ORIGINAL": "Iveco 1907584 / 2992242", "MANN-FILTER": "W 11 102", "FLEETGUARD": "LF3880", "DONALDSON": "P550425", "FG WILSON": "10000-51229 / 901-102", "BALDWIN / OTRAS": "BALDWIN B7120"},
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Gasoil Principal (x2)", "OEM / ORIGINAL": "Iveco 1902138", "MANN-FILTER": "WK 842", "FLEETGUARD": "FF5052", "DONALDSON": "P550008", "FG WILSON": "10000-00339 / 901-202", "BALDWIN / OTRAS": "BALDWIN BF825"},
        {"ID_GRUPO": "G-002", "TIPO": "Prefiltro Decantador Gasoil", "OEM / ORIGINAL": "Iveco 1908547", "MANN-FILTER": "WK 1060", "FLEETGUARD": "FS1251", "DONALDSON": "P551329", "FG WILSON": "10000-12609 / 901-228", "BALDWIN / OTRAS": "BALDWIN BF1212"},
        {"ID_GRUPO": "G-002", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "Himoinsa 1903210 / Iveco 1903210", "MANN-FILTER": "C 30 850/2", "FLEETGUARD": "AF25223", "DONALDSON": "P182054", "FG WILSON": "996-452 / 901-016", "BALDWIN / OTRAS": "BALDWIN RS3518"},
        {"ID_GRUPO": "G-002", "TIPO": "Correa Ventilador / Alternador", "OEM / ORIGINAL": "Iveco 4841793", "MANN-FILTER": "GATES 8554-10825", "FLEETGUARD": "DAYCO 13A1075C", "DONALDSON": "CONTITECH AVX13X1075", "FG WILSON": "915-020", "BALDWIN / OTRAS": "OPTIBELT AVX 13 x 1075"},

        # G-003 DEUTZ BF 8 M 1015 CP (V8)
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Aceite Principal (x2)", "OEM / ORIGINAL": "Deutz 01182912", "MANN-FILTER": "W 11 102/16", "FLEETGUARD": "LF3997", "DONALDSON": "P550425", "FG WILSON": "10000-51229 / 901-102", "BALDWIN / OTRAS": "BALDWIN B7180"},
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Gasoil Principal (x2)", "OEM / ORIGINAL": "Deutz 01180597", "MANN-FILTER": "WK 940/20", "FLEETGUARD": "FF5485", "DONALDSON": "P553004", "FG WILSON": "10000-00339 / 901-214", "BALDWIN / OTRAS": "BALDWIN BF7632"},
        {"ID_GRUPO": "G-003", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM / ORIGINAL": "Deutz 04152512", "MANN-FILTER": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010", "FG WILSON": "10000-12609 / 901-228", "BALDWIN / OTRAS": "BALDWIN BF1385-SPS"},
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Aire Principal (V8)", "OEM / ORIGINAL": "Deutz 01180872", "MANN-FILTER": "C 30 1500", "FLEETGUARD": "AF25431", "DONALDSON": "P777868", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3998"},
        {"ID_GRUPO": "G-003", "TIPO": "Filtro Aire Seguridad (Interior)", "OEM / ORIGINAL": "Deutz 01180873", "MANN-FILTER": "CF 1500", "FLEETGUARD": "AF25432", "DONALDSON": "P777869", "FG WILSON": "901-049", "BALDWIN / OTRAS": "BALDWIN RS3999"},

        # G-004 CATERPILLAR 3412TTA (V12)
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Aceite Alta Eficiencia (x2)", "OEM / ORIGINAL": "CAT 1R-1808", "MANN-FILTER": "WD 13 145/4", "FLEETGUARD": "LF9009", "DONALDSON": "P551808", "FG WILSON": "10000-51230 / 901-115", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Gasoil Secundario (x2)", "OEM / ORIGINAL": "CAT 1R-0749", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5319", "DONALDSON": "P551315", "FG WILSON": "10000-59651 / 901-248", "BALDWIN / OTRAS": "BALDWIN BF7587"},
        {"ID_GRUPO": "G-004", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM / ORIGINAL": "CAT 1R-0770 / 133-5673", "MANN-FILTER": "WK 1080/1", "FLEETGUARD": "FS19820", "DONALDSON": "P550625", "FG WILSON": "10000-12609 / 901-228", "BALDWIN / OTRAS": "BALDWIN BF1214"},
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Aire Principal (x2 V12)", "OEM / ORIGINAL": "CAT 6I-2505", "MANN-FILTER": "C 33 920/3", "FLEETGUARD": "AF25138", "DONALDSON": "P532505", "FG WILSON": "996-454 / 901-056", "BALDWIN / OTRAS": "BALDWIN RS3704"},
        {"ID_GRUPO": "G-004", "TIPO": "Filtro Agua / Refrigerante", "OEM / ORIGINAL": "CAT 9N-3366", "MANN-FILTER": "WA 940/1", "FLEETGUARD": "WF2075", "DONALDSON": "P552075", "FG WILSON": "10000-00054 / 901-401", "BALDWIN / OTRAS": "BALDWIN BW5075"},

        # G-005 CATERPILLAR DE220GC (C7.1)
        {"ID_GRUPO": "G-005", "TIPO": "Filtro Gasoil / Decantador Duplex (x2)", "OEM / ORIGINAL": "CAT 478-1422 / Perkins 4461492", "MANN-FILTER": "WK 8156 / WK 9059 x", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-005", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-005", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-006 PRAMAC GSW145 (DEUTZ BF6M1013E)
        {"ID_GRUPO": "G-006", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "Deutz 01182912", "MANN-FILTER": "W 11 102/16", "FLEETGUARD": "LF3997", "DONALDSON": "P553771", "FG WILSON": "10000-51229 / 901-102", "BALDWIN / OTRAS": "BALDWIN B7180"},
        {"ID_GRUPO": "G-006", "TIPO": "Filtro Gasoil Principal", "OEM / ORIGINAL": "Deutz 01180597", "MANN-FILTER": "WK 940/20", "FLEETGUARD": "FF5485", "DONALDSON": "P553004", "FG WILSON": "10000-00339", "BALDWIN / OTRAS": "BALDWIN BF7632"},
        {"ID_GRUPO": "G-006", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM / ORIGINAL": "Deutz 04152512", "MANN-FILTER": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010", "FG WILSON": "10000-12609", "BALDWIN / OTRAS": "BALDWIN BF1385-SPS"},
        {"ID_GRUPO": "G-006", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "Deutz 01180872", "MANN-FILTER": "C 30 1500", "FLEETGUARD": "AF25431", "DONALDSON": "P777868", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3998"},

        # G-007 CATERPILLAR DE165E0 (C7.1)
        {"ID_GRUPO": "G-007", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-007", "TIPO": "Filtro Gasoil Secundario", "OEM / ORIGINAL": "CAT 389-1085", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5788", "DONALDSON": "P551085", "FG WILSON": "10000-59651", "BALDWIN / OTRAS": "BALDWIN BF9880"},
        {"ID_GRUPO": "G-007", "TIPO": "Prefiltro Separador Agua Gasoil", "OEM / ORIGINAL": "CAT 478-1422", "MANN-FILTER": "WK 8156", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-007", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-008 CATERPILLAR DE200E0 (C7.1) - LIDL Tamaraceite
        {"ID_GRUPO": "G-008", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-008", "TIPO": "Filtro Gasoil Secundario", "OEM / ORIGINAL": "CAT 389-1085", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5788", "DONALDSON": "P551085", "FG WILSON": "10000-59651", "BALDWIN / OTRAS": "BALDWIN BF9880"},
        {"ID_GRUPO": "G-008", "TIPO": "Prefiltro Separador Agua Gasoil", "OEM / ORIGINAL": "CAT 478-1422", "MANN-FILTER": "WK 8156", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-008", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-009 CATERPILLAR DE165E0 (C7.1) - LIDL Miller Bajo
        {"ID_GRUPO": "G-009", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-009", "TIPO": "Filtro Gasoil Secundario", "OEM / ORIGINAL": "CAT 389-1085", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5788", "DONALDSON": "P551085", "FG WILSON": "10000-59651", "BALDWIN / OTRAS": "BALDWIN BF9880"},
        {"ID_GRUPO": "G-009", "TIPO": "Prefiltro Separador Agua Gasoil", "OEM / ORIGINAL": "CAT 478-1422", "MANN-FILTER": "WK 8156", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-009", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-010 PRAMAC GEW145 (DEUTZ BF6M1013E) - LIDL Jinámar
        {"ID_GRUPO": "G-010", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "Deutz 01182912", "MANN-FILTER": "W 11 102/16", "FLEETGUARD": "LF3997", "DONALDSON": "P553771", "FG WILSON": "10000-51229 / 901-102", "BALDWIN / OTRAS": "BALDWIN B7180"},
        {"ID_GRUPO": "G-010", "TIPO": "Filtro Gasoil Principal", "OEM / ORIGINAL": "Deutz 01180597", "MANN-FILTER": "WK 940/20", "FLEETGUARD": "FF5485", "DONALDSON": "P553004", "FG WILSON": "10000-00339", "BALDWIN / OTRAS": "BALDWIN BF7632"},
        {"ID_GRUPO": "G-010", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM / ORIGINAL": "Deutz 04152512", "MANN-FILTER": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010", "FG WILSON": "10000-12609", "BALDWIN / OTRAS": "BALDWIN BF1385-SPS"},
        {"ID_GRUPO": "G-010", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "Deutz 01180872", "MANN-FILTER": "C 30 1500", "FLEETGUARD": "AF25431", "DONALDSON": "P777868", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3998"},

        # G-011 PRAMAC GDW295B (BAUDOUIN 6M16) - LIDL Maspalomas
        {"ID_GRUPO": "G-011", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "Baudouin 16224830K", "MANN-FILTER": "W 11 102/16", "FLEETGUARD": "LF4054", "DONALDSON": "P553771", "FG WILSON": "10000-51229", "BALDWIN / OTRAS": "BALDWIN B7180"},
        {"ID_GRUPO": "G-011", "TIPO": "Filtro Gasoil Principal", "OEM / ORIGINAL": "Baudouin 16232128S", "MANN-FILTER": "WK 940/20", "FLEETGUARD": "FF5485", "DONALDSON": "P553004", "FG WILSON": "10000-00339", "BALDWIN / OTRAS": "BALDWIN BF7632"},
        {"ID_GRUPO": "G-011", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM / ORIGINAL": "Baudouin 16232127R", "MANN-FILTER": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010", "FG WILSON": "10000-12609", "BALDWIN / OTRAS": "BALDWIN BF1385-SPS"},
        {"ID_GRUPO": "G-011", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "Baudouin 16232183C", "MANN-FILTER": "C 30 1500", "FLEETGUARD": "AF26159", "DONALDSON": "P604273", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3998"},

        # G-012 CATERPILLAR DE165E0 (C7.1) - LIDL Antigua El Castillo
        {"ID_GRUPO": "G-012", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-012", "TIPO": "Filtro Gasoil Secundario", "OEM / ORIGINAL": "CAT 389-1085", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5788", "DONALDSON": "P551085", "FG WILSON": "10000-59651", "BALDWIN / OTRAS": "BALDWIN BF9880"},
        {"ID_GRUPO": "G-012", "TIPO": "Prefiltro Separador Agua Gasoil", "OEM / ORIGINAL": "CAT 478-1422", "MANN-FILTER": "WK 8156", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-012", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-013 CATERPILLAR DE200E0 (C7.1) - LIDL Corralejo El Guirre
        {"ID_GRUPO": "G-013", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-013", "TIPO": "Filtro Gasoil Secundario", "OEM / ORIGINAL": "CAT 389-1085", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5788", "DONALDSON": "P551085", "FG WILSON": "10000-59651", "BALDWIN / OTRAS": "BALDWIN BF9880"},
        {"ID_GRUPO": "G-013", "TIPO": "Prefiltro Separador Agua Gasoil", "OEM / ORIGINAL": "CAT 478-1422", "MANN-FILTER": "WK 8156", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-013", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-014 CATERPILLAR DE220E0 (C7.1) - LIDL Puerto del Rosario
        {"ID_GRUPO": "G-014", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "CAT 458-7518 / 1R-1808", "MANN-FILTER": "W 950/38", "FLEETGUARD": "LF16015", "DONALDSON": "P550529", "FG WILSON": "10000-51230", "BALDWIN / OTRAS": "BALDWIN B7299"},
        {"ID_GRUPO": "G-014", "TIPO": "Filtro Gasoil Secundario", "OEM / ORIGINAL": "CAT 389-1085", "MANN-FILTER": "WK 8117", "FLEETGUARD": "FF5788", "DONALDSON": "P551085", "FG WILSON": "10000-59651", "BALDWIN / OTRAS": "BALDWIN BF9880"},
        {"ID_GRUPO": "G-014", "TIPO": "Prefiltro Separador Agua Gasoil", "OEM / ORIGINAL": "CAT 478-1422", "MANN-FILTER": "WK 8156", "FLEETGUARD": "FS20007", "DONALDSON": "P551422", "FG WILSON": "20000-12699", "BALDWIN / OTRAS": "BALDWIN BF46062"},
        {"ID_GRUPO": "G-014", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "CAT 458-1093 / 110-6326", "MANN-FILTER": "C 21 004", "FLEETGUARD": "AF25557", "DONALDSON": "P608533", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3870"},

        # G-015 GENESAL GEN220YI (BAUDOUIN 6M16G2D0/S) - LIDL Playa Blanca
        {"ID_GRUPO": "G-015", "TIPO": "Filtro Aceite Motor", "OEM / ORIGINAL": "Baudouin 16224830K", "MANN-FILTER": "W 11 102/16", "FLEETGUARD": "LF4054", "DONALDSON": "P553771", "FG WILSON": "10000-51229", "BALDWIN / OTRAS": "BALDWIN B7180"},
        {"ID_GRUPO": "G-015", "TIPO": "Filtro Gasoil Principal", "OEM / ORIGINAL": "Baudouin 16232128S", "MANN-FILTER": "WK 940/20", "FLEETGUARD": "FF5485", "DONALDSON": "P553004", "FG WILSON": "10000-00339", "BALDWIN / OTRAS": "BALDWIN BF7632"},
        {"ID_GRUPO": "G-015", "TIPO": "Prefiltro Sep. Agua Gasoil", "OEM / ORIGINAL": "Baudouin 16232127R", "MANN-FILTER": "WK 10002 x", "FLEETGUARD": "FS19735", "DONALDSON": "P551010", "FG WILSON": "10000-12609", "BALDWIN / OTRAS": "BALDWIN BF1385-SPS"},
        {"ID_GRUPO": "G-015", "TIPO": "Filtro Aire Principal", "OEM / ORIGINAL": "Baudouin 16232183C", "MANN-FILTER": "C 30 1500", "FLEETGUARD": "AF26159", "DONALDSON": "P604273", "FG WILSON": "901-048", "BALDWIN / OTRAS": "BALDWIN RS3998"}
    ])

    mantenimientos = pd.DataFrame([
        # G-001
        {"ID_GRUPO": "G-001", "INTERVALO": "Diario / 10 Hours", "TAREA": "Comprobar nivel de aceite, refrigerante en vaso de expansión, drenar agua del prefiltro e inspección de fugas."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Cambiar 36L aceite 15W-40 VDS-3/4. Sustituir 2 filtros aceite principales + 1 bypass. Cambiar filtros de gasoil y revisar correas."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Limpieza de radiador e intercooler. Sustituir filtro de aire. Reglaje de válvulas/taqués del motor Volvo."},
        {"ID_GRUPO": "G-001", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 44L refrigerante Volvo VCS y manguitos de radiador."},

        # G-002
        {"ID_GRUPO": "G-002", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite Cárter IVECO V8 (35L) y nivel de radiador. Purgar condensados de cazoleta de gasoil."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 400 Horas / 12 Meses", "TAREA": "Cambio de 35L aceite 15W-40 ACEA E3/E5. Sustituir 2 filtros de aceite W11102 y par de filtros de combustible WK 842."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 800 Horas / 2 Años", "TAREA": "Sustituir filtro de aire C 30 850/2. Ajuste de taqués en culatas de bloque V8 AIFO."},
        {"ID_GRUPO": "G-002", "INTERVALO": "Cada 1.500 Horas / 3 Años", "TAREA": "Cambio de refrigerante al 50% (50L) y revisión de la bomba de agua de engranajes."},

        # G-003
        {"ID_GRUPO": "G-003", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Comprobar nivel de aceite Cárter DEUTZ V8 (45L) e inspeccionar manguitos de aire del intercooler."},
        {"ID_GRUPO": "G-003", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Cambiar 45L aceite Deutz DQC III-10 15W-40. Sustituir 2 filtros de aceite 01182912 y filtros de gasoil 01180597."},
        {"ID_GRUPO": "G-003", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Cambiar cartuchos de aire principal C 30 1500 y de seguridad CF 1500. Limpiar panal exterior del radiador V8."},
        {"ID_GRUPO": "G-003", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 65L de anticongelante orgánico y reglaje de los 8 inyectores bomba PLD."},

        # G-004
        {"ID_GRUPO": "G-004", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Inspección de nivel en cárter V12 (68L CAT DEO 15W-40) y tensión de baterías de arranque 24V."},
        {"ID_GRUPO": "G-004", "INTERVALO": "Cada 250 Horas / 12 Meses", "TAREA": "Sustitución de 68L de aceite CAT DEO. Cambiar par de filtros de aceite CAT 1R-1808 y par de filtros de gasoil 1R-0749."},
        {"ID_GRUPO": "G-004", "INTERVALO": "Cada 500 Horas / 2 Años", "TAREA": "Sustituir los 2 filtros de aire principales CAT 6I-2505 y el cartucho de tratamiento de agua 9N-3366."},
        {"ID_GRUPO": "G-004", "INTERVALO": "Cada 1.500 Horas / 3 Años", "TAREA": "Sustituir 90L de líquido refrigerante CAT ELC (Extended Life Coolant) e inspección de turbocompresores gemelos."},

        # G-005
        {"ID_GRUPO": "G-005", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (27L) y purgar agua de los filtros FG Wilson 20000-12699."},
        {"ID_GRUPO": "G-005", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518 y los 2 filtros de gasoil decantadores FG Wilson 20000-12699."},
        {"ID_GRUPO": "G-005", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Inspeccionar tensión de correa de transmisión y soplado exterior del radiador."},
        {"ID_GRUPO": "G-005", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 27L de anticongelante orgánico CAT ELC y comprobación de inyectores Common Rail."},

        # G-006
        {"ID_GRUPO": "G-006", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter Deutz 1013 (20L), vaso de expansión refrigerante (27L) y purgar agua de decantador."},
        {"ID_GRUPO": "G-006", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 20L de aceite Deutz 15W-40. Cambiar filtro Donaldson P553771 y filtro principal de gasoil Deutz 01180597."},
        {"ID_GRUPO": "G-006", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir cartucho de aire principal y revisar el estado visual de la correa de transmisión / bomba de agua."},
        {"ID_GRUPO": "G-006", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 27L de anticongelante y revisión de presiones y reglaje en bombas de inyección unitarias."},

        # G-007
        {"ID_GRUPO": "G-007", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (21L) y purgar condensados del prefiltro."},
        {"ID_GRUPO": "G-007", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518, filtro secundario CAT 389-1085 y prefiltro CAT 478-1422."},
        {"ID_GRUPO": "G-007", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Inspeccionar estado de correas y limpieza exterior del panel de radiador."},
        {"ID_GRUPO": "G-007", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 21L de anticongelante orgánico CAT ELC y comprobación del sistema de inyección Common Rail."},

        # G-008
        {"ID_GRUPO": "G-008", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (21L) y purgar condensados del prefiltro."},
        {"ID_GRUPO": "G-008", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518, filtro secundario CAT 389-1085 y prefiltro CAT 478-1422."},
        {"ID_GRUPO": "G-008", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Inspeccionar estado de correas y revisar conexiones del módulo de inyección electrónica."},
        {"ID_GRUPO": "G-008", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución de anticongelante ELC y revisión integral mediante software Caterpillar Electronic Technician (CAT ET)."},

        # G-009
        {"ID_GRUPO": "G-009", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (21L) y purgar condensados de cazoleta."},
        {"ID_GRUPO": "G-009", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518, filtro secundario CAT 389-1085 y prefiltro CAT 478-1422."},
        {"ID_GRUPO": "G-009", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Soplar radiador y revisar estado visual de la correa de accesorios."},
        {"ID_GRUPO": "G-009", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 21L de líquido refrigerante CAT ELC y comprobación general del sistema eléctrico."},

        # G-010
        {"ID_GRUPO": "G-010", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter Deutz 1013 (20L), vaso de expansión refrigerante (27L) y purgar agua de decantador."},
        {"ID_GRUPO": "G-010", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 20L de aceite Deutz 15W-40. Cambiar filtro Donaldson P553771 y filtro principal de gasoil Deutz 01180597."},
        {"ID_GRUPO": "G-010", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir cartucho de aire principal y revisar el estado visual de la correa de transmisión / bomba de agua."},
        {"ID_GRUPO": "G-010", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 27L de anticongelante y revisión de presiones en bombas de inyección unitarias."},

        # G-011
        {"ID_GRUPO": "G-011", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite en cárter Baudouin 6M16 (24L), depósito de expansión (35L) y purgar agua del prefiltro."},
        {"ID_GRUPO": "G-011", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 24L de aceite 15W-40 CF/E7. Cambiar filtro de aceite Baudouin 16224830K y filtros de gasoil (principal y prefiltro)."},
        {"ID_GRUPO": "G-011", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire Baudouin 16232183C. Inspección de manguitos de intercooler y tensión de correas."},
        {"ID_GRUPO": "G-011", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 35L de refrigerante orgánico y comprobación general de la instalación eléctrica y alterna Mecc Alte."},

        # G-012
        {"ID_GRUPO": "G-012", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (21L) y purgar condensados de cazoleta."},
        {"ID_GRUPO": "G-012", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518, filtro secundario CAT 389-1085 y prefiltro CAT 478-1422."},
        {"ID_GRUPO": "G-012", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Soplar radiador y revisar estado visual de la correa de accesorios."},
        {"ID_GRUPO": "G-012", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 21L de líquido refrigerante CAT ELC y comprobación general del sistema eléctrico."},

        # G-013
        {"ID_GRUPO": "G-013", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (21L) y purgar condensados de cazoleta."},
        {"ID_GRUPO": "G-013", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518, filtro secundario CAT 389-1085 y prefiltro CAT 478-1422."},
        {"ID_GRUPO": "G-013", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Soplar radiador y revisar estado visual de la correa de accesorios."},
        {"ID_GRUPO": "G-013", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 21L de líquido refrigerante CAT ELC y comprobación general del sistema eléctrico."},

        # G-014
        {"ID_GRUPO": "G-014", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite cárter C7.1 (16.5L CAT DEO 15W-40), vaso de expansión (21L) y purgar condensados de cazoleta."},
        {"ID_GRUPO": "G-014", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 16.5L de aceite 15W-40. Cambiar filtro de aceite CAT 458-7518, filtro secundario CAT 389-1085 y prefiltro CAT 478-1422."},
        {"ID_GRUPO": "G-014", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire CAT 458-1093. Soplar radiador y revisar estado visual de la correa de accesorios."},
        {"ID_GRUPO": "G-014", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 21L de líquido refrigerante CAT ELC y comprobación general del sistema eléctrico."},

        # G-015
        {"ID_GRUPO": "G-015", "INTERVALO": "Diario / Antes de Arranque", "TAREA": "Verificar nivel de aceite en cárter Baudouin 6M16 (24L), depósito de expansión (35L) y purgar agua del prefiltro."},
        {"ID_GRUPO": "G-015", "INTERVALO": "Cada 500 Horas / 12 Meses", "TAREA": "Sustituir 24L de aceite 15W-40 CF/E7. Cambiar filtro de aceite Baudouin 16224830K y filtros de gasoil (principal y prefiltro)."},
        {"ID_GRUPO": "G-015", "INTERVALO": "Cada 1.000 Horas / 2 Años", "TAREA": "Sustituir filtro de aire Baudouin 16232183C. Inspección de manguitos de intercooler y tensión de correas."},
        {"ID_GRUPO": "G-015", "INTERVALO": "Cada 2.000 Horas / 4 Años", "TAREA": "Sustitución completa de 35L de refrigerante orgánico y comprobación general de la instalación eléctrica y alterna."}
    ])

    averias = pd.DataFrame([
        # G-001
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 94 / PPID 6", "SINTOMA": "Baja Presión de Gasoil (pérdida de potencia / tirones)", "SOLUCION": "Cambiar filtro principal (5µ) y prefiltro decantador. Purgar aire manualmente con bomba de cebado."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 100", "SINTOMA": "Baja Presión de Aceite (alarma y parada de emergencia)", "SOLUCION": "Comprobar nivel (36L 15W-40). Cambiar 2 filtros principales + 1 bypass. Inspeccionar presostato."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 102", "SINTOMA": "Baja Presión de Turbo / Sobrealimentación", "SOLUCION": "Revisar manguitos/abrazaderas de admisión, limpiar sensor MAP o comprobar holgura en turbocompresor."},
        {"ID_GRUPO": "G-001", "CODIGO_ERROR": "PID 110", "SINTOMA": "Alta Temperatura de Refrigerante (>98°C)", "SOLUCION": "Rellenar anticongelante Volvo VCS, soplar radiador con aire a presión y revisar tensión de correas."},

        # G-002
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Alarma Presión Aceite Cárter V8", "SINTOMA": "Caída de presión al subir temperatura de motor AIFO", "SOLUCION": "Comprobar grado de viscosidad (usar 15W-40 E3/E5). Cambiar pares de filtros W11102 o revisar válvula reguladora de bomba de aceite."},
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Sobretemperatura Agua en Culatas", "SINTOMA": "Parada por termostato en cuadro Himoinsa CEC7", "SOLUCION": "Limpiar radiador frontal bloqueado por polvo, tensar correa de la bomba de agua 4841793 o cambiar termostatos mecánicos."},
        {"ID_GRUPO": "G-002", "CODIGO_ERROR": "Fallo de Inyección / Humo Blanco", "SINTOMA": "Inestabilidad en ralentí y tirones al coger carga de 440 kVA", "SOLUCION": "Sustituir cartuchos de gasoil WK 842, purgar aire en la bomba lineal Bosch e inspeccionar inyectores de la bancada V8."},

        # G-003
        {"ID_GRUPO": "G-003", "CODIGO_ERROR": "Fallo Regulador Electrónico EMR", "SINTOMA": "Incapacidad para mantener 1500 rpm exactas (50 Hz)", "SOLUCION": "Revisar captador inductivo en volante de inercia, limpiar virutas y verificar actuador electromagnético de la bomba inyectora."},
        {"ID_GRUPO": "G-003", "CODIGO_ERROR": "Baja Presión de Cárter V8 Deutz", "SINTOMA": "Luz de advertencia de presión de aceite encendida en cuadro Genesal", "SOLUCION": "Sustituir inmediatamente los 2 filtros de aceite Deutz 01182912 y verificar que no hay dilución de gasoil en cárter."},
        {"ID_GRUPO": "G-003", "CODIGO_ERROR": "Alta Temperatura de Admisión", "SINTOMA": "Humo negro por el escape y reducción automática de kVA", "SOLUCION": "Limpiar panal de intercooler Air-to-Air y cambiar filtros de aire C 30 1500 / CF 1500."},

        # G-004
        {"ID_GRUPO": "G-004", "CODIGO_ERROR": "CAT Code 39 (Presión Aceite Low)", "SINTOMA": "Parada de emergencia en panel EMCP por baja presión V12", "SOLUCION": "Comprobar nivel en cárter (68L). Cambiar la pareja de filtros CAT 1R-1808. Verificar calibración del sensor de presión de aceite."},
        {"ID_GRUPO": "G-004", "CODIGO_ERROR": "CAT Code 11 (High Coolant Temp)", "SINTOMA": "Disparo por alta temperatura en circuito V12 Biturbo", "SOLUCION": "Comprobar nivel de anticongelante CAT ELC (90L). Limpiar el radiador doble y sustituir el filtro de tratamiento de agua CAT 9N-3366."},
        {"ID_GRUPO": "G-004", "CODIGO_ERROR": "Fallo Arranque / Solenoide Combustible", "SINTOMA": "El motor gira fuerte pero no abre paso de gasoil", "SOLUCION": "Revisar fusible del solenoide de corte de combustible en el bloque 3412 y limpiar par de prefiltros CAT 1R-0770."},

        # G-005
        {"ID_GRUPO": "G-005", "CODIGO_ERROR": "Warning / Shutdown Low Oil Pressure", "SINTOMA": "Disparo por baja presión de aceite en panel GCCP 1.2", "SOLUCION": "Comprobar nivel en cárter C7.1 (16.5L). Sustituir filtro CAT 458-7518 y comprobar sensor de presión en bloque de motor."},
        {"ID_GRUPO": "G-005", "CODIGO_ERROR": "High Coolant Temperature Alarm", "SINTOMA": "Temperatura de agua superior a 98°C bajo carga", "SOLUCION": "Comprobar nivel en vaso de expansión (27L CAT ELC), limpiar radiador exterior y verificar correa de ventilador."},
        {"ID_GRUPO": "G-005", "CODIGO_ERROR": "Fail to Start / Low Battery Voltage", "SINTOMA": "Intento de arranque fallido en cuadro GCCP 1.2", "SOLUCION": "Comprobar cargador de baterías de 24V del cuadro, bornes sulfatados o presencia de aire en el circuito de gasoil Common Rail."},

        # G-006
        {"ID_GRUPO": "G-006", "CODIGO_ERROR": "Disparo Presión Aceite (Display PRAMAC)", "SINTOMA": "Parada inmediata al coger carga y mensaje luminoso rojo de aceite", "SOLUCION": "Verificar varilla nivel aceite. Reemplazar filtro Donaldson P553771 installed e inspeccionar sensor analógico VDO."},
        {"ID_GRUPO": "G-006", "CODIGO_ERROR": "Alarma Alta Temperatura Agua", "SINTOMA": "Aviso de advertencia y posterior parada (>100ºC)", "SOLUCION": "Comprobar correa de ventilador Poly-V. Limpiar celdas exteriores del radiador y verificar que el nivel en botella es correcto."},
        {"ID_GRUPO": "G-006", "CODIGO_ERROR": "Motor gira pero no arranca", "SINTOMA": "Fallo al iniciar en modo Prueba (T) o Manual desde la GC M02-C", "SOLUCION": "Purgar circuito de combustible desde prefiltro, revisar fusible de alimentación del solenoide de pare en motor Deutz BF 6M 1013 E."},

        # G-007
        {"ID_GRUPO": "G-007", "CODIGO_ERROR": "CAT Low Oil Pressure Warning", "SINTOMA": "Aviso de baja presión de aceite en centralita GCCP", "SOLUCION": "Comprobar nivel en cárter C7.1 (16.5L). Reemplazar filtro CAT 458-7518 y revisar sensor de presión."},
        {"ID_GRUPO": "G-007", "CODIGO_ERROR": "CAT High Coolant Temp", "SINTOMA": "Temperatura de motor elevada por encima del límite operativo", "SOLUCION": "Comprobar nivel en depósito de expansión (21L CAT ELC), limpiar panal de radiador y verificar estado de la correa."},
        {"ID_GRUPO": "G-007", "CODIGO_ERROR": "Fuel Pressure / Common Rail Fault", "SINTOMA": "Inestabilidad o fallo de arranque en grupo DE165E0", "SOLUCION": "Sustituir prefiltro CAT 478-1422 y filtro secundario CAT 389-1085 para evitar impurezas en bomba de alta presión."},

        # G-008
        {"ID_GRUPO": "G-008", "CODIGO_ERROR": "EMCP Evento E360 (Low Oil Pressure)", "SINTOMA": "Apagado por protección en EMCP 4.2 debido a baja presión", "SOLUCION": "Verificar nivel de aceite del C7.1. Comprobar que no hay dilución por gasoil, sustituir filtro 458-7518 y resetear fallo con botón amarillo ACK."},
        {"ID_GRUPO": "G-008", "CODIGO_ERROR": "EMCP Evento E361 (High Coolant Temp)", "SINTOMA": "Alta temperatura de refrigerante detectada por el sensor del bloque", "SOLUCION": "Verificar nivel de refrigerante CAT ELC. Limpiar radiador exterior y purgar aire del circuito de refrigeración."},
        {"ID_GRUPO": "G-008", "CODIGO_ERROR": "Data Link Fault / FMI 9", "SINTOMA": "Pérdida de comunicación entre la EMCP 4.2 y la ECU del motor C7.1", "SOLUCION": "Revisar los conectores J1939 (Data Link) en el cableado trasero del panel y en el módulo electrónico del motor para detectar falsos contactos."},

        # G-009
        {"ID_GRUPO": "G-009", "CODIGO_ERROR": "CAT Low Oil Pressure Warning", "SINTOMA": "Aviso o parada por baja presión de aceite en bloque C7.1", "SOLUCION": "Comprobar nivel en cárter (16.5L). Sustituir filtro CAT 458-7518 y verificar estado del sensor analógico."},
        {"ID_GRUPO": "G-009", "CODIGO_ERROR": "CAT High Coolant Temp", "SINTOMA": "Temperatura del refrigerante por encima de 98°C", "SOLUCION": "Comprobar nivel en depósito (21L CAT ELC), limpiar celdas del radiador y verificar tensión de la correa de la bomba."},
        {"ID_GRUPO": "G-009", "CODIGO_ERROR": "Fuel Rail Pressure Low", "SINTOMA": "Fallo de arranque o tirones al asumir carga en grupo DE165E0", "SOLUCION": "Sustituir prefiltro separador CAT 478-1422 y filtro secundario CAT 389-1085 para purgar impurezas en Common Rail."},

        # G-010
        {"ID_GRUPO": "G-010", "CODIGO_ERROR": "Disparo Presión Aceite (Panel AC21)", "SINTOMA": "Parada del generador por baja presión de aceite en motor Deutz", "SOLUCION": "Revisar varilla de nivel, sustituir filtro de aceite Deutz 01182912 y comprobar estado del presostato."},
        {"ID_GRUPO": "G-010", "CODIGO_ERROR": "Alarma Alta Temperatura de Agua", "SINTOMA": "Sobrecalentamiento (>100°C) registrado en centralita Pramac", "SOLUCION": "Limpiar celdas del radiador, comprobar nivel de refrigerante y verificar tensión de la correa del ventilador."},
        {"ID_GRUPO": "G-010", "CODIGO_ERROR": "Fallo de Arranque / Solenoide", "SINTOMA": "El motor de arranque gira pero el grupo no enciende", "SOLUCION": "Purgar aire en el circuito de gasoil, revisar prefiltro decantador y comprobar fusible de alimentación de la bomba inyectora."},

        # G-011
        {"ID_GRUPO": "G-011", "CODIGO_ERROR": "DSE Low Oil Pressure Warning / Shutdown", "SINTOMA": "Disparo en centralita DSE 7320 por baja presión de aceite en motor Baudouin", "SOLUCION": "Comprobar nivel en cárter (24L). Sustituir filtro Baudouin 16224830K y revisar cableado del sensor de presión."},
        {"ID_GRUPO": "G-011", "CODIGO_ERROR": "DSE High Coolant Temp Trip", "SINTOMA": "Parada por alta temperatura de refrigerante (>95°C) bajo carga en Maspalomas", "SOLUCION": "Verificar nivel en depósito de expansión (35L), limpiar panal exterior del radiador y comprobar estado del termostato."},
        {"ID_GRUPO": "G-011", "CODIGO_ERROR": "DSE Fail to Start Alarm", "SINTOMA": "El motor gira en el intento de arranque pero no llega combustible", "SOLUCION": "Purgar el circuito de gasoil desde el prefiltro separador de agua y comprobar el estado de los filtros Baudouin."},

        # G-012
        {"ID_GRUPO": "G-012", "CODIGO_ERROR": "EMCP 4.1 E360 (Low Oil Pressure)", "SINTOMA": "Parada de protección en cuadro EMCP 4.1 por baja presión en C7.1", "SOLUCION": "Verificar varilla de nivel (16.5L CAT DEO), cambiar filtro CAT 458-7518 y rearme con pulsador ACK."},
        {"ID_GRUPO": "G-012", "CODIGO_ERROR": "EMCP 4.1 E361 (High Coolant Temp)", "SINTOMA": "Temperatura del refrigerante excedida en la pantalla de la centralita", "SOLUCION": "Comprobar nivel en depósito (21L CAT ELC), limpiar celdas del radiador y revisar ventilación del shelter."},
        {"ID_GRUPO": "G-012", "CODIGO_ERROR": "EMCP 4.1 Fuel Rail Pressure", "SINTOMA": "Inestabilidad o fallo de arranque en Antigua El Castillo", "SOLUCION": "Sustituir prefiltro CAT 478-1422 y filtro secundario CAT 389-1085 para purgar el sistema Common Rail."},

        # G-013
        {"ID_GRUPO": "G-013", "CODIGO_ERROR": "EMCP 4.2 Evento E360 (Low Oil Pressure)", "SINTOMA": "Parada de protección en panel EMCP 4.2 por baja presión de aceite en C7.1", "SOLUCION": "Verificar nivel en cárter (16.5L CAT DEO), sustituir filtro CAT 458-7518 y borrar código de evento con botón ACK."},
        {"ID_GRUPO": "G-013", "CODIGO_ERROR": "EMCP 4.2 Evento E361 (High Coolant Temp)", "SINTOMA": "Sobrecalentamiento del bloque C7.1 detectado por el sensor del termostato", "SOLUCION": "Comprobar nivel en depósito de expansión (21L CAT ELC), limpiar celdas del radiador y verificar flujo de aire en el shelter."},
        {"ID_GRUPO": "G-013", "CODIGO_ERROR": "EMCP 4.2 Data Link / Fuel Rail Fault", "SINTOMA": "Alarma de comunicación con ECU o presión de rampa baja en Corralejo", "SOLUCION": "Revisar conectores J1939 y sustituir prefiltro CAT 478-1422 y filtro secundario CAT 389-1085."},

        # G-014
        {"ID_GRUPO": "G-014", "CODIGO_ERROR": "EMCP 4.2 Evento E360 (Low Oil Pressure)", "SINTOMA": "Parada de protección en panel EMCP 4.2 por baja presión de aceite en C7.1", "SOLUCION": "Verificar nivel en cárter (16.5L CAT DEO), sustituir filtro CAT 458-7518 y borrar código de evento con botón ACK."},
        {"ID_GRUPO": "G-014", "CODIGO_ERROR": "EMCP 4.2 Evento E361 (High Coolant Temp)", "SINTOMA": "Sobrecalentamiento del bloque C7.1 detectado por el sensor del termostato", "SOLUCION": "Comprobar nivel en depósito de expansión (21L CAT ELC), limpiar celdas del radiador y verificar flujo de aire en el shelter."},
        {"ID_GRUPO": "G-014", "CODIGO_ERROR": "EMCP 4.2 Data Link / Fuel Rail Fault", "SINTOMA": "Alarma de comunicación con ECU o presión de rampa baja en Puerto del Rosario", "SOLUCION": "Revisar conectores J1939 y sustituir prefiltro CAT 478-1422 y filtro secundario CAT 389-1085."},

        # G-015
        {"ID_GRUPO": "G-015", "CODIGO_ERROR": "GEINTEL 2 Baja Presión de Aceite", "SINTOMA": "Disparo en centralita GEINTEL 2 por baja presión en motor Baudouin", "SOLUCION": "Comprobar nivel en cárter (24L 15W-40), sustituir filtro Baudouin 16224830K y revisar presostato."},
        {"ID_GRUPO": "G-015", "CODIGO_ERROR": "GEINTEL 2 Alta Temperatura Agua", "SINTOMA": "Parada por sobrecalentamiento en tienda de Playa Blanca", "SOLUCION": "Verificar nivel en depósito de expansión (35L), limpiar panal exterior del radiador y comprobar termostato."},
        {"ID_GRUPO": "G-015", "CODIGO_ERROR": "GEINTEL 2 Fallo de Arranque (Fail to Start)", "SINTOMA": "El motor gira pero no se produce la puesta en marcha", "SOLUCION": "Purgar circuito de combustible, verificar estado de prefiltro decantador Baudouin y comprobar alimentación eléctrica del cuadro GEINTEL 2."}
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

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Ficha Técnica", "📦 Repuestos Multimarca", "🛠️ Mantenimiento", "🚨 Averías", "📖 Manuales"])

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
    st.markdown("### 📦 Enciclopedia de Recambios y Compatibilidad Multimarca")
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
    st.link_button(f"📂 Abrir Carpeta de Manuales en Google Drive ({selected_grupo['CLIENTE']})", selected_grupo["MANUAL_URL"])
