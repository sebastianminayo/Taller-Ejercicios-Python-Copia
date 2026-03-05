import sys
sys.path.insert(0, ".")
import limpieza_utils

def solucionar():
    # 1. Obtenemos los datos procesados (ROT13 descifrado + Limpieza de símbolos)
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Contamos la frecuencia exacta del nombre "Maria"
    # Al usar limpieza_utils, comparamos strings limpios y normalizados
    cantidad_maria = df[df['nombre'] == 'Maria'].shape[0]
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 02")
    print(f"El nombre 'Maria' aparece: {cantidad_maria} veces")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()
