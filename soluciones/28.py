import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

promedio_por_profesion = df.groupby('profesion')['salario_limpio'].mean()
profesion_max = promedio_por_profesion.idxmax()
salario_prom  = promedio_por_profesion.max()
print(f"Profesión con salario promedio más alto: {profesion_max} (promedio: {salario_prom:,.2f})")