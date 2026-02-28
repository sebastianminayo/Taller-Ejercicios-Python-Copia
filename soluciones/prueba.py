import limpieza_utils
df = limpieza_utils.obtener_df_limpio()
# Buscamos la fila que tiene ese salario máximo
rico = df[df['salario_limpio'] == df['salario_limpio'].max()]
print(rico[['nombre', 'apellido', 'profesion', 'salario_limpio']])