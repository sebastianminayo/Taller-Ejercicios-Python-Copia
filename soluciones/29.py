import sys
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

df = obtener_df_limpio()

cantidad = df[df['email_limpio'].str.endswith('@gmail.com')].shape[0]
print(f"Registros con email de dominio 'gmail.com': {cantidad}")