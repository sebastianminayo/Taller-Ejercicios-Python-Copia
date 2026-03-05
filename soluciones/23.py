import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[
    (df['nombre'] == 'Carlos') &
    (df['ciudad'] == 'Cali')
].shape[0]
print(f"Registros con nombre 'Carlos' y ciudad 'Cali': {cantidad}")