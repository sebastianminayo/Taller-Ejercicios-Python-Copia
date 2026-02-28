import limpieza_utils

def solucionar():
    # 1. Obtener los datos limpios (Descifrados y sin símbolos)
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Encontrar el apellido más frecuente
    # value_counts() cuenta cuántas veces aparece cada apellido y ordena de mayor a menor
    conteo_apellidos = df['apellido'].value_counts()
    
    # Extraemos el nombre del apellido y su frecuencia
    apellido_ganador = conteo_apellidos.idxmax()
    frecuencia_ganador = conteo_apellidos.max()
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 05")
    print(f"Apellido más frecuente: {apellido_ganador}")
    print(f"Cantidad de apariciones: {frecuencia_ganador}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()