import limpieza_utils

def solucionar():
    # 1. Obtener el DataFrame con los salarios ya convertidos a float
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Calcular el promedio de la columna 'salario_limpio'
    # .mean() es la función de Pandas para obtener el promedio
    promedio_total = df['salario_limpio'].mean()
    
    # 3. Formateamos el resultado para que sea legible (con 2 decimales)
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 14")
    print(f"Promedio salarial total: ${promedio_total:,.2f}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()