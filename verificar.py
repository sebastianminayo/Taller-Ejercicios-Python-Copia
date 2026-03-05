"""
verificar.py
Ejecuta y muestra las respuestas de los 30 ejercicios en una sola corrida.
Uso: uv run python verificar.py
"""

import sys
import time
import pandas as pd
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

print("=" * 60)
print("  TALLER DE PYTHON — Verificación de los 30 Ejercicios")
print("=" * 60)
print("⏳ Cargando y limpiando dataset (300.000 registros)...")

t0 = time.time()
df = obtener_df_limpio()
t1 = time.time()
print(f"✅ Dataset listo en {t1 - t0:.2f}s\n")

resultados = {}

# ── 01 ──────────────────────────────────────────────────────────────────────
resultados[1] = df[df['id'].astype(str).str.contains(r'[^0-9]', na=False)].shape[0]

# ── 02 ──────────────────────────────────────────────────────────────────────
resultados[2] = df[df['nombre'] == 'Maria'].shape[0]

# ── 03 ──────────────────────────────────────────────────────────────────────
resultados[3] = df[df['nombre'] == 'Juan'].shape[0]

# ── 04 ──────────────────────────────────────────────────────────────────────
nom = df['nombre'].value_counts()
resultados[4] = f"{nom.idxmax()} - {nom.max()}"

# ── 05 ──────────────────────────────────────────────────────────────────────
ape = df['apellido'].value_counts()
resultados[5] = f"{ape.idxmax()} - {ape.max()}"

# ── 06 ──────────────────────────────────────────────────────────────────────
resultados[6] = df[df['ciudad'] == 'Bogota'].shape[0]

# ── 07 ──────────────────────────────────────────────────────────────────────
resultados[7] = df[df['ciudad'] == 'Medellin'].shape[0]

# ── 08 ──────────────────────────────────────────────────────────────────────
resultados[8] = df['ciudad'].nunique()

# ── 09 ──────────────────────────────────────────────────────────────────────
resultados[9] = df[df['profesion'] == 'Ingeniero'].shape[0]

# ── 10 ──────────────────────────────────────────────────────────────────────
resultados[10] = df[df['profesion'] == 'Programador'].shape[0]

# ── 11 ──────────────────────────────────────────────────────────────────────
resultados[11] = df['profesion'].nunique()

# ── 12 ──────────────────────────────────────────────────────────────────────
resultados[12] = df[df['email'].astype(str).str.contains(r'\s', na=False)].shape[0]

# ── 13 ──────────────────────────────────────────────────────────────────────
resultados[13] = df[df['salario'].astype(str).str.contains(r'[^0-9]', na=False)].shape[0]

# ── 14 ──────────────────────────────────────────────────────────────────────
resultados[14] = round(df['salario_limpio'].mean(), 2)

# ── 15 ──────────────────────────────────────────────────────────────────────
resultados[15] = int(df['salario_limpio'].max())

# ── 16 ──────────────────────────────────────────────────────────────────────
resultados[16] = int(df['salario_limpio'].min())

# ── 17 ──────────────────────────────────────────────────────────────────────
resultados[17] = int(df['activo_bool'].sum())

# ── 18 ──────────────────────────────────────────────────────────────────────
resultados[18] = int((~df['activo_bool']).sum())

# ── 19 ──────────────────────────────────────────────────────────────────────
resultados[19] = df[
    ~df['fecha_nacimiento'].astype(str).str.match(r'^\d{4}-\d{2}-\d{2}$', na=False)
].shape[0]

# ── 20 ──────────────────────────────────────────────────────────────────────
resultados[20] = df[
    (df['fecha_dt'].dt.year >= 1990) & (df['fecha_dt'].dt.year <= 2000)
].shape[0]

# ── 21 ──────────────────────────────────────────────────────────────────────
resultados[21] = df[df['fecha_dt'].dt.year < 1960].shape[0]

# ── 22 ──────────────────────────────────────────────────────────────────────
resultados[22] = df[df['fecha_dt'] < pd.Timestamp('1976-02-26')].shape[0]

# ── 23 ──────────────────────────────────────────────────────────────────────
resultados[23] = df[(df['nombre'] == 'Carlos') & (df['ciudad'] == 'Cali')].shape[0]

# ── 24 ──────────────────────────────────────────────────────────────────────
resultados[24] = df[(df['nombre'] == 'Ana') & (df['profesion'] == 'Medico')].shape[0]

# ── 25 ──────────────────────────────────────────────────────────────────────
resultados[25] = df[
    (df['profesion'] == 'Abogado') & (df['salario_limpio'] > 10_000_000)
].shape[0]

# ── 26 ──────────────────────────────────────────────────────────────────────
resultados[26] = df[
    (df['ciudad'] == 'Barranquilla') &
    (df['activo_bool'] == True) &
    (df['fecha_dt'].dt.year > 1980)
].shape[0]

# ── 27 ──────────────────────────────────────────────────────────────────────
ing = df[df['profesion'] == 'Ingeniero']
resultados[27] = ing['ciudad'].value_counts().idxmax()

# ── 28 ──────────────────────────────────────────────────────────────────────
resultados[28] = df.groupby('profesion')['salario_limpio'].mean().idxmax()

# ── 29 ──────────────────────────────────────────────────────────────────────
resultados[29] = df[df['email_limpio'].str.endswith('@gmail.com')].shape[0]

# ── 30 ──────────────────────────────────────────────────────────────────────
resultados[30] = df[(df['nombre'] == 'Jose') & (df['apellido'] == 'Garcia')].shape[0]

# ── IMPRIMIR RESULTADOS ──────────────────────────────────────────────────────
preguntas = {
    1:  'IDs con caracteres no numéricos',
    2:  'Apariciones del nombre "Maria"',
    3:  'Apariciones del nombre "Juan"',
    4:  'Nombre más frecuente',
    5:  'Apellido más frecuente',
    6:  'Registros ciudad "Bogota"',
    7:  'Registros ciudad "Medellin"',
    8:  'Ciudades únicas',
    9:  'Registros profesión "Ingeniero"',
    10: 'Registros profesión "Programador"',
    11: 'Profesiones únicas',
    12: 'Emails con espacios adicionales',
    13: 'Salarios con caracteres no numéricos',
    14: 'Salario promedio',
    15: 'Salario máximo',
    16: 'Salario mínimo',
    17: 'Activo = True',
    18: 'Activo = False',
    19: 'Fechas con formato diferente a YYYY-MM-DD',
    20: 'Nacidos entre 1990 y 2000',
    21: 'Nacidos antes de 1960',
    22: 'Personas con más de 50 años',
    23: 'Carlos en Cali',
    24: 'Ana con profesión Medico',
    25: 'Abogados con salario > 10,000,000',
    26: 'Barranquilla, activos, nacidos después de 1980',
    27: 'Ciudad con más Ingenieros',
    28: 'Profesión con salario promedio más alto',
    29: 'Emails con dominio gmail.com',
    30: 'Jose Garcia',
}

print(f"{'#':<4} {'Ejercicio':<45} {'Respuesta'}")
print("-" * 70)
for i in range(1, 31):
    print(f"{i:<4} {preguntas[i]:<45} {resultados[i]}")

print("-" * 70)
print(f"✅ {len(resultados)}/30 ejercicios completados")
print(f"⏱️  Tiempo total: {time.time() - t0:.2f}s")
print("=" * 60)
