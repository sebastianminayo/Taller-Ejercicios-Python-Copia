import sys
sys.path.insert(0, '.')
import limpieza_utils

def solucionar():
    df = limpieza_utils.obtener_df_limpio()
    
    cantidad_ingeniero = df[df['profesion'] == 'Ingeniero'].shape[0]
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 09")
    print(f"Registros con profesión Ingeniero: {cantidad_ingeniero}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()