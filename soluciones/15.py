import limpieza_utils

def solucionar():
    # 1. Obtener el DataFrame con los salarios ya convertidos a números
    df = limpieza_utils.obtener_df_limpio()
    
    # 2. Encontrar el valor máximo en la columna 'salario_limpio'
    # .max() busca el número más alto ignorando los valores nulos (NaN)
    salario_maximo = df['salario_limpio'].max()
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 15")
    print(f"El salario máximo encontrado es: ${salario_maximo:,.2f}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()