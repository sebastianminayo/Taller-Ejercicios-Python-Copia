import pandas as pd

def solucionar():
    # 1. Cargamos el CSV original para ver los errores "reales"
    df = pd.read_csv('data/personas.csv')
    
    # 2. Identificamos los emails que tienen espacios
    # Usamos .astype(str) para evitar errores si hay celdas vacías
    # La regex \s busca espacios, tabs o saltos de línea
    contiene_espacios = df['email'].astype(str).str.contains(r'\s', na=False)
    
    # 3. Contamos cuántos dieron True
    cantidad_con_espacios = contiene_espacios.sum()
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 12")
    print(f"Emails con espacios adicionales: {cantidad_con_espacios}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()