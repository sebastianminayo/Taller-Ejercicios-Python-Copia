import sys
sys.path.insert(0, ".")
import limpieza_utils

def solucionar():
    # 1. Obtener el DataFrame con las ciudades ya normalizadas
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Ejercicio 07: ¿Cuántos registros tienen la ciudad "Medellin"?
    # Nota: El taller usa "Medellin" sin tilde para estandarizar
    ciudad_objetivo = "Medellin"
    
    # Filtramos y contamos las filas
    cantidad_medellin = df[df['ciudad'] == ciudad_objetivo].shape[0]
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 07")
    print(f"Registros en {ciudad_objetivo}: {cantidad_medellin}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()