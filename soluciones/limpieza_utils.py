import pandas as pd
import codecs
import re

def limpiar_texto_general(texto):
    """
    Limpia símbolos, espacios y basura de columnas de texto 
    (nombres, apellidos, ciudades, profesiones, email).
    """
    if pd.isna(texto): 
        return ""
    
    texto_str = str(texto)
    
    # 1. Quitar 'aprox.' y otros prefijos comunes detectados en tu data
    texto_str = re.sub(r'(?i)aprox\.?|mailto:', '', texto_str)
    
    # 2. Quitar caracteres especiales solicitados (@, %, #) 
    # y los detectados en tu tabla ($, *, ( ), [ ], !, <, >, ~, ., -)
    # Dejamos las letras y espacios
    limpio = re.sub(r'[@%#$*()~\[\]!<>.\-_+]', '', texto_str)
    
    # 3. Quitar espacios extra al inicio, final y dobles espacios internos
    return " ".join(limpio.split()).strip()

def descifrar_rot13(texto):
    """Aplica el descifrado ROT13 a nombres y apellidos"""
    if pd.isna(texto): 
        return ""
    return codecs.decode(str(texto), 'rot_13')

def obtener_df_limpio():
    """
    Carga el dataset y devuelve un DataFrame con la limpieza 
    base aplicada a todas las columnas.
    """
    # Cargamos el CSV (300,000 registros)
    df = pd.read_csv('data/personas.csv')
    
    # --- PROCESAMIENTO DE COLUMNAS ---
    
    # 1. Nombres y Apellidos (ROT13 + Limpieza de símbolos)
    df['nombre'] = df['nombre_cifrado'].apply(descifrar_rot13).apply(limpiar_texto_general)
    df['apellido'] = df['apellido_cifrado'].apply(descifrar_rot13).apply(limpiar_texto_general)
    
    # 2. Ciudad y Profesión (Limpieza de símbolos)
    df['ciudad'] = df['ciudad'].apply(limpiar_texto_general)
    df['profesion'] = df['profesion'].apply(limpiar_texto_general)
    
    # 3. Email (Mantenemos el @ y el punto pero quitamos espacios y basura)
    # Nota: Aquí no usamos limpiar_texto_general porque borraría el @ del correo
    df['email'] = df['email'].apply(lambda x: re.sub(r'[\s()<>#%*]', '', str(x)).lower() if pd.notna(x) else "")

    return df