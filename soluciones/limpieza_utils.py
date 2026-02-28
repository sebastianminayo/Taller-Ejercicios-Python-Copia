import pandas as pd
import codecs
import re

def obtener_df_limpio():
    df = pd.read_csv('./data/personas.csv')

    # --- 1. Nombres, Apellidos, Ciudades y Profesiones ---
    def limpiar_texto(texto, es_cifrado=False):
        if pd.isna(texto): return ""
        t = str(texto)
        if es_cifrado:
            t = codecs.decode(t, 'rot_13')
        # Quitamos basura pero mantenemos letras, tildes, ñ y espacios
        limpio = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]', '', t)
        return limpio.strip().title()

    df['nombre'] = df['nombre_cifrado'].apply(lambda x: limpiar_texto(x, True))
    df['apellido'] = df['apellido_cifrado'].apply(lambda x: limpiar_texto(x, True))
    df['ciudad'] = df['ciudad'].apply(limpiar_texto)
    df['profesion'] = df['profesion'].apply(limpiar_texto)

    # --- 2. Salarios (Crucial para Ejercicios 14-16) ---
    def limpiar_salario(valor):
        if pd.isna(valor): return None
        num = re.sub(r'\D', '', str(valor)) # Solo dígitos
        return float(num) if num != '' else None

    df['salario_limpio'] = df['salario'].apply(limpiar_salario)

    # --- 3. Fechas (Crucial para Ejercicios 21-25) ---
    def limpiar_fecha(valor):
        if pd.isna(valor): return pd.NaT
        # Quitamos basura y espacios: '@1960-04-29' -> '1960-04-29'
        limpia = re.sub(r'[^0-9\-]', '', str(valor))
        return pd.to_datetime(limpia, errors='coerce')

    df['fecha_dt'] = df['fecha_nacimiento'].apply(limpiar_fecha)

    # --- 4. Activo (Crucial para Ejercicios 17-18) ---
    def normalizar_activo(valor):
        v = str(valor).lower().strip().replace('#', '')
        if v in ['true', '1', 'yes', 'si']: return True
        return False

    df['activo_bool'] = df['activo'].apply(normalizar_activo)

    return df