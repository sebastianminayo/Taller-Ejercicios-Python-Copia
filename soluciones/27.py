import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

ingenieros = df[df['profesion'] == 'Ingeniero']
ciudad_max = ingenieros['ciudad'].value_counts().idxmax()
cantidad   = ingenieros['ciudad'].value_counts().max()
print(f"Ciudad con más Ingenieros: {ciudad_max} ({cantidad} ingenieros)")