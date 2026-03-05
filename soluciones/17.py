import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df['activo_bool'].sum()
print(f"Registros con activo = True: {cantidad}")