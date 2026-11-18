"""
Comparative Analysis and Selection of Solar PV Modules
Reproducible Python analysis of a curated, published case-study dataset.

Run:
    pip install pandas matplotlib
    python analyze_solar_modules.py

The source values are transcribed from an open-access 2021 case study.
This is a two-case comparison, not a statistically representative market survey.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "curated_module_comparison.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["module_area_m2"] = df["module_length_m"] * df["module_width_m"]
df["power_density_W_per_m2"] = df["module_rating_W"] / df["module_area_m2"]
df["installed_cost_per_W_USD"] = df["system_initial_cost_USD_per_kW"] / 1000

print("\\nMODULE COMPARISON")
cols = ["technology", "module_rating_W", "efficiency_pct",
        "power_density_W_per_m2", "system_initial_cost_USD_per_kW",
        "annual_energy_yield_kWh_per_kW",
        "annual_energy_yield_kWh_per_m2", "payback_period_years"]
print(df[cols].round(2).to_string(index=False))

mono = df.iloc[0]
poly = df.iloc[1]
print("\\nKEY DIFFERENCES")
print(f"Mono efficiency advantage: {(mono.efficiency_pct/poly.efficiency_pct-1)*100:.2f}%")
print(f"Mono power-density advantage: {(mono.power_density_W_per_m2/poly.power_density_W_per_m2-1)*100:.2f}%")
print(f"Mono annual energy per area advantage: {(mono.annual_energy_yield_kWh_per_m2/poly.annual_energy_yield_kWh_per_m2-1)*100:.2f}%")
print(f"Mono system cost per kW premium: {(mono.system_initial_cost_USD_per_kW/poly.system_initial_cost_USD_per_kW-1)*100:.2f}%")
print(f"Mono payback is {mono.payback_period_years-poly.payback_period_years:.2f} years longer in this case study.")

plots = [
    ("efficiency_pct", "Module efficiency (%)", "Module efficiency"),
    ("power_density_W_per_m2", "Rated power density (W/m²)", "Rated power density"),
    ("annual_energy_yield_kWh_per_m2", "Annual energy yield (kWh/m²)", "Annual energy yield per area"),
    ("system_initial_cost_USD_per_kW", "Initial system cost (USD/kW)", "Initial system cost per kW"),
]
for col, ylabel, title in plots:
    plt.figure(figsize=(7, 4))
    plt.bar(["Mono-Si", "Poly-Si"], df[col])
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(OUT / f"{col}.png", dpi=180)
    plt.close()

print(f"\\nCharts saved in: {OUT}")
