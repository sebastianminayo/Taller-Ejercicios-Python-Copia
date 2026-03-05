import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[
    (df['ciudad'] == 'Barranquilla') &
    (df['activo_bool'] == True) &
    (df['fecha_dt'].dt.year > 1980)
].shape[0]
print(f"Registros en Barranquilla, activos y nacidos después de 1980: {cantidad}")