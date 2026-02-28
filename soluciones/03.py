import limpieza_utils

def solucionar():
    # 1. Obtenemos los datos procesados
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Contamos la frecuencia exacta del nombre "Juan"
    cantidad_juan = df[df['nombre'] == 'Juan'].shape[0]
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 03")
    print(f"El nombre 'Juan' aparece: {cantidad_juan} veces")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()