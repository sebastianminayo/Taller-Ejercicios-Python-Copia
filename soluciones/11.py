import limpieza_utils

def solucionar():
    # 1. Obtener el DataFrame con las profesiones ya normalizadas
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Ejercicio 11: ¿Cuántas profesiones únicas existen tras la limpieza?
    # nunique() cuenta los valores diferentes ignorando duplicados y basura eliminada
    profesiones_unicas = df['profesion'].nunique()
    
    # Opcional: Si quieres ver la lista de profesiones en consola
    # print(df['profesion'].unique())
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 11")
    print(f"Número de profesiones únicas: {profesiones_unicas}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()