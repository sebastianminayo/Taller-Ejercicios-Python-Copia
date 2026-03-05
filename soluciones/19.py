import sys
import pandas as pd
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

# Verificar directamente sobre la columna original sin limpiar
patron_correcto = r'^\d{4}-\d{2}-\d{2}$'
cantidad = df[~df['fecha_nacimiento'].astype(str).str.match(patron_correcto, na=False)].shape[0]
print(f"Registros con fecha en formato diferente a YYYY-MM-DD: {cantidad}")