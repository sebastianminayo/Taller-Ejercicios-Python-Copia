import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

salario_min = df['salario_limpio'].min()
print(f"Salario mínimo: {salario_min:.2f}")