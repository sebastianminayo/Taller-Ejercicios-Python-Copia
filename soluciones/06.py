import sys
sys.path.insert(0, ".")
import limpieza_utils

def solucionar():
    # 1. Obtener el DataFrame con la limpieza de símbolos ya aplicada
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Rectificación: Asegurar que quitamos espacios fantasma 
    # y convertimos a un formato estándar para comparar.
    # Usamos .str.strip() por si acaso quedó algún espacio de más
    ciudades_limpias = df['ciudad'].astype(str).str.strip()
    
    # 3. Contamos exactamente "Bogota"
    # Nota: No usamos tildes porque en el CSV viene como 'Bogota'
    cantidad_bogota = (ciudades_limpias == "Bogota").sum()
    
    print(f"--- RECTIFICACIÓN EJERCICIO 06 ---")
    print(f"Registros exactos de Bogota: {cantidad_bogota}")
    print(f"----------------------------------")

if __name__ == "__main__":
    solucionar()