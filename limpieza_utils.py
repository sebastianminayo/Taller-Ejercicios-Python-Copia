import pandas as pd
import codecs
import re

def obtener_df_limpio():
    df = pd.read_csv('./data/personas.csv')

    # ── 1. NOMBRES Y APELLIDOS (ROT13 + quitar caracteres sucios) ───────────
    def limpiar_nombre(texto):
        if pd.isna(texto): return ''
        t = codecs.decode(str(texto), 'rot_13')
        t = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', t)
        return t.strip().title()

    df['nombre']   = df['nombre_cifrado'].apply(limpiar_nombre)
    df['apellido'] = df['apellido_cifrado'].apply(limpiar_nombre)

    # ── 2. CIUDAD ────────────────────────────────────────────────────────────
    # Algunas ciudades aparecen truncadas (sin vocales), se normalizan con mapa
    CIUDAD_MAP = {
        'Armni':       'Armenia',
        'Bogot':       'Bogota',
        'Brrnquill':   'Barranquilla',
        'Bucrmng':     'Bucaramanga',
        'Cli':         'Cali',
        'Crtgn':       'Cartagena',
        'Cucut':       'Cucuta',
        'Ibgu':        'Ibague',
        'Mdllin':      'Medellin',
        'Mnizls':      'Manizales',
        'Montri':      'Monteria',
        'Niv':         'Neiva',
        'Popyn':       'Popayan',
        'Prir':        'Pereira',
        'Psto':        'Pasto',
        'Sincljo':     'Sincelejo',
        'Snt Mrt':     'Santa Marta',
        'Tunj':        'Tunja',
        'Villvicncio': 'Villavicencio',
        'Vlldupr':     'Valledupar',
    }

    def limpiar_ciudad(texto):
        if pd.isna(texto): return ''
        t = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', str(texto)).strip().title()
        return CIUDAD_MAP.get(t, t)

    df['ciudad'] = df['ciudad'].apply(limpiar_ciudad)

    # ── 3. PROFESION ─────────────────────────────────────────────────────────
    # Igual que ciudades: variantes truncadas se mapean al nombre correcto
    PROFESION_MAP = {
        'Abogdo':       'Abogado',
        'Administrdor': 'Administrador',
        'Arquitcto':    'Arquitecto',
        'Chf':          'Chef',
        'Contdor':      'Contador',
        'Crpintro':     'Carpintero',
        'Disndor':      'Disenador',
        'Economist':    'Economista',
        'Elctricist':   'Electricista',
        'Enfrmro':      'Enfermero',
        'Ingniro':      'Ingeniero',
        'Mcnico':       'Mecanico',
        'Mdico':        'Medico',
        'Plomro':       'Plomero',
        'Priodist':     'Periodista',
        'Profsor':      'Profesor',
        'Progrmdor':    'Programador',
        'Trductor':     'Traductor',
        'Vtrinrio':     'Veterinario',
    }

    def limpiar_profesion(texto):
        if pd.isna(texto): return ''
        t = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', str(texto)).strip().title()
        return PROFESION_MAP.get(t, t)

    df['profesion'] = df['profesion'].apply(limpiar_profesion)

    # ── 4. SALARIO ───────────────────────────────────────────────────────────
    # Casos sucios:
    #   - Coma decimal:    '14024383,00'  -> 14024383
    #   - Letra l -> 1:    'l0088323'     -> 10088323
    #   - Letra O -> 0:    '125O9422'     -> 12509422
    #   - Caracteres extra: '$8728702', '@14142618', 'aprox.1977777'
    def limpiar_salario(valor):
        if pd.isna(valor): return None
        s = str(valor).strip()
        # Coma como separador decimal: tomar solo la parte entera
        if re.match(r'^\d+,\d+$', s):
            return float(s.split(',')[0])
        # Sustituir letras confundidas con dígitos
        s = s.replace('l', '1').replace('O', '0')
        # Quitar todo lo que no sea dígito
        num = re.sub(r'\D', '', s)
        return float(num) if num else None

    df['salario_limpio'] = df['salario'].apply(limpiar_salario)

    # ── 5. FECHA DE NACIMIENTO ───────────────────────────────────────────────
    # Formatos encontrados:
    #   YYYY-MM-DD  (limpio)
    #   YYYY/MM/DD  -> normalizar separador
    #   YYYY.MM.DD  -> normalizar separador
    #   YY YY-MM-DD -> espacio en el año ('19 92' -> '1992')
    #   @YYYY-MM-DD, ~YYYY-MM-DD, YYYY-MM-DD% -> quitar basura al inicio/fin
    def limpiar_fecha(valor):
        if pd.isna(valor): return pd.NaT
        s = str(valor).strip()
        # Quitar caracteres no numéricos del inicio y del fin
        s = re.sub(r'^[^0-9]+', '', s)
        s = re.sub(r'[^0-9]+$', '', s)
        # Pegar espacios dentro del año: '19 92' -> '1992'
        s = re.sub(r'(\d{2})\s(\d{2})', r'\1\2', s)
        # Normalizar separadores / y . a -
        s = re.sub(r'[/\.]', '-', s)
        return pd.to_datetime(s, format='%Y-%m-%d', errors='coerce')

    df['fecha_dt'] = df['fecha_nacimiento'].apply(limpiar_fecha)

    # ── 6. ACTIVO ────────────────────────────────────────────────────────────
    # Valores True: true, 1, yes, si (y variantes con mayúsculas o basura)
    # Valores False: false, 0, no (y variantes)
    VERDADERO = {'true', '1', 'yes', 'si'}

    def normalizar_activo(valor):
        # Quitar todo carácter no alfanumérico y pasar a minúsculas
        v = re.sub(r'[^a-zA-Z0-9]', '', str(valor)).lower()
        return v in VERDADERO

    df['activo_bool'] = df['activo'].apply(normalizar_activo)

    # ── 7. EMAIL ─────────────────────────────────────────────────────────────
    # Eliminar todos los espacios y pasar a minúsculas
    def limpiar_email(texto):
        if pd.isna(texto): return ''
        return re.sub(r'\s+', '', str(texto)).lower()

    df['email_limpio'] = df['email'].apply(limpiar_email)

    return df