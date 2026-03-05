import sys
import pandas as pd
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

# Fecha de referencia indicada por el enunciado
fecha_ref = pd.Timestamp('2026-02-26')
fecha_corte = pd.Timestamp('1976-02-26')  # Nacidos antes de esta fecha tienen más de 50 años

cantidad = df[df['fecha_dt'] < fecha_corte].shape[0]
print(f"Personas con más de 50 años (al 2026-02-26): {cantidad}")