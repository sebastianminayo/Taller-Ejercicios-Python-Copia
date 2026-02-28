import limpieza_utils

def solucionar():
    df = limpieza_utils.obtener_df_limpio()
    top_nombre = df['nombre'].value_counts()
    
    nombre = top_nombre.idxmax()
    cantidad = top_nombre.max()
    
    print(f"Nombre más frecuente: {nombre} ({cantidad} veces)")

if __name__ == "__main__":
    solucionar()