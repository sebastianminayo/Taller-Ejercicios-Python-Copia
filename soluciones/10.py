import sys
sys.path.insert(0, ".")
import limpieza_utils

def solucionar():
    df = limpieza_utils.obtener_df_limpio()
    
    # En tu tabla vimos 'Programador' y ' Programador' (con espacio)
    # limpieza_utils ya se encargó de dejarlo como 'Programador'
    cantidad_programador = df[df['profesion'] == 'Programador'].shape[0]
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 10")
    print(f"Registros con profesión Programador: {cantidad_programador}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()