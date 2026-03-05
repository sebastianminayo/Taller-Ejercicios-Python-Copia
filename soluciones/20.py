import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[
    (df['fecha_dt'].dt.year >= 1990) &
    (df['fecha_dt'].dt.year <= 2000)
].shape[0]
print(f"Personas nacidas entre 1990 y 2000 (inclusive): {cantidad}")