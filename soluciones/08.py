import limpieza_utils

def solucionar():
    # 1. Obtener el DataFrame con las ciudades ya normalizadas y sin símbolos
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Ejercicio 08: ¿Cuántas ciudades únicas existen tras la limpieza?
    # El método nunique() cuenta cuántos nombres de ciudades distintos quedaron
    ciudades_unicas = df['ciudad'].nunique()
    
    # Opcional: Para tu curiosidad, podemos ver cuáles son
    # lista_ciudades = df['ciudad'].unique()
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 08")
    print(f"Número de ciudades únicas: {ciudades_unicas}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()