import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[
    (df['profesion'] == 'Abogado') &
    (df['salario_limpio'] > 10_000_000)
].shape[0]
print(f"Registros con profesión 'Abogado' y salario > 10,000,000: {cantidad}")