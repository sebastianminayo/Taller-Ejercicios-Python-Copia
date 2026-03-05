"""
visualizaciones.py
Genera 4 gráficas del análisis del dataset personas.csv
Uso: uv run python visualizaciones.py
"""

import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
sys.path.insert(0, '.')
from limpieza_utils import obtener_df_limpio

print("⏳ Cargando dataset...")
df = obtener_df_limpio()
print("✅ Dataset listo. Generando visualizaciones...\n")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Análisis del Dataset — Personas (300.000 registros)", fontsize=16, fontweight='bold', y=0.98)

COLOR_PRINCIPAL = "#4C72B0"
COLOR_SECUNDARIO = "#DD8452"

# ── 1. Salario promedio por profesión ────────────────────────────────────────
ax1 = axes[0, 0]
prom = df.groupby('profesion')['salario_limpio'].mean().sort_values(ascending=True)
bars = ax1.barh(prom.index, prom.values / 1_000_000, color=COLOR_PRINCIPAL, edgecolor='white')
ax1.set_title("Salario Promedio por Profesión", fontweight='bold')
ax1.set_xlabel("Salario promedio (millones COP)")
ax1.xaxis.set_major_formatter(mticker.FormatStrFormatter('$%.1fM'))
# Destacar la profesión con mayor salario
max_idx = list(prom.index).index(prom.idxmax())
bars[max_idx].set_color(COLOR_SECUNDARIO)
ax1.tick_params(axis='y', labelsize=8)

# ── 2. Distribución de registros por ciudad ──────────────────────────────────
ax2 = axes[0, 1]
ciudad_count = df['ciudad'].value_counts().sort_values(ascending=True)
ax2.barh(ciudad_count.index, ciudad_count.values, color=COLOR_PRINCIPAL, edgecolor='white')
ax2.set_title("Registros por Ciudad", fontweight='bold')
ax2.set_xlabel("Cantidad de personas")
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax2.tick_params(axis='y', labelsize=8)

# ── 3. Distribución de salarios (histograma) ─────────────────────────────────
ax3 = axes[1, 0]
ax3.hist(df['salario_limpio'] / 1_000_000, bins=50, color=COLOR_PRINCIPAL, edgecolor='white', alpha=0.85)
ax3.axvline(df['salario_limpio'].mean() / 1_000_000, color=COLOR_SECUNDARIO,
            linestyle='--', linewidth=2, label=f"Promedio: ${df['salario_limpio'].mean()/1_000_000:.1f}M")
ax3.set_title("Distribución de Salarios", fontweight='bold')
ax3.set_xlabel("Salario (millones COP)")
ax3.set_ylabel("Frecuencia")
ax3.xaxis.set_major_formatter(mticker.FormatStrFormatter('$%.0fM'))
ax3.legend()

# ── 4. Activo vs Inactivo por las 5 ciudades más grandes ─────────────────────
ax4 = axes[1, 1]
top5 = df['ciudad'].value_counts().head(5).index
df_top5 = df[df['ciudad'].isin(top5)]
activos   = df_top5[df_top5['activo_bool'] == True]['ciudad'].value_counts().reindex(top5, fill_value=0)
inactivos = df_top5[df_top5['activo_bool'] == False]['ciudad'].value_counts().reindex(top5, fill_value=0)

x = range(len(top5))
width = 0.4
ax4.bar([i - width/2 for i in x], activos.values,  width=width, label='Activos',   color=COLOR_PRINCIPAL, edgecolor='white')
ax4.bar([i + width/2 for i in x], inactivos.values, width=width, label='Inactivos', color=COLOR_SECUNDARIO, edgecolor='white')
ax4.set_title("Activos vs Inactivos — Top 5 Ciudades", fontweight='bold')
ax4.set_ylabel("Cantidad de personas")
ax4.set_xticks(list(x))
ax4.set_xticklabels(top5, rotation=15, ha='right')
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))
ax4.legend()

plt.tight_layout()
output_path = "analisis_personas.png"
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"✅ Visualizaciones guardadas en: {output_path}")
plt.show()
