import limpieza_utils

def solucionar():
    # 1. Obtener los datos con profesiones ya normalizadas
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Filtrar exactamente por "Ingeniero"
    # Nuestra limpieza ya quitó el '@' de '@Ingeniero'
    cantidad_ingeniero = df[df['profesion'] == 'Ingeniero'].shape[0]
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 09")
    print(f"Registros con profesión Ingeniero: {cantidad_ingeniero}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()