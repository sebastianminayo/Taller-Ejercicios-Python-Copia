import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[
    (df['nombre'] == 'Jose') &
    (df['apellido'] == 'Garcia')
].shape[0]
print(f"Registros con nombre 'Jose' y apellido 'Garcia': {cantidad}")