import pandas as pd

def solucionar():
    df = pd.read_csv('data/personas.csv')
    # Un ID es "numérico" SOLO si todos sus caracteres son dígitos 0-9
    # .str.isdigit() devuelve False si hay paréntesis, puntos, signos $ o letras
    es_valido = df['id'].astype(str).str.isdigit()
    cantidad_no_num = (~es_valido).sum()
    
    print(f"Resultado Ejercicio 01: {cantidad_no_num}")

if __name__ == "__main__":
    solucionar()