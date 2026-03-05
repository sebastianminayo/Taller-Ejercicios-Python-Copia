import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[df['fecha_dt'].dt.year < 1960].shape[0]
print(f"Personas nacidas antes de 1960: {cantidad}")