import pandas as pd

def solucionar():
    # 1. Cargamos el CSV original sin limpiar para detectar los errores
    df = pd.read_csv('data/personas.csv')
    
    # 2. Definimos qué es un número puro
    # Usamos una expresión regular: ^\d+$ significa que desde el inicio 
    # hasta el final solo debe haber dígitos.
    # Cualquier cosa como "14.000" o "$1200" dará False.
    es_numero_puro = df['salario'].astype(str).str.match(r'^\d+$', na=False)
    
    # 3. El resultado son los que NO son números puros
    cantidad_sucios = (~es_numero_puro).sum()
    
    print(f"========================================")
    print(f"RESULTADO EJERCICIO 13")
    print(f"Salarios con formato no numérico: {cantidad_sucios}")
    print(f"========================================")

if __name__ == "__main__":
    solucionar()