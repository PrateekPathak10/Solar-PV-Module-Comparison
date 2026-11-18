# Comparative Analysis and Selection of Solar PV Modules

## Project scope
A Python-based comparison of one monocrystalline and one polycrystalline rooftop PV system from a published, open-access case study. The analysis compares module efficiency, rated power density, installed capacity, system cost per installed kW, energy yield and payback period.

## Dataset provenance
The CSV is a curated secondary dataset transcribed from:
Shi, K., Li, C., & Koo, C. (2021). A Techno-Economic Feasibility Analysis of Mono-Si and Poly-Si Photovoltaic Systems in the Rooftop Area of Commercial Building under the Feed-In Tariff Scheme. *Sustainability*, 13(9), 4709.
https://doi.org/10.3390/su13094709

The article is open access under CC BY. Values used are reported in the article's module specification, installation, cost and results sections. This is not a raw multi-vendor market dataset. It is a two-system case study based on CSUN355-72M and CSUN310-72P modules in a Hong Kong commercial-building scenario.

## Run the analysis
```bash
pip install pandas matplotlib
python analyze_solar_modules.py
```

## Main findings
- Mono-Si module efficiency: 18.30%; Poly-Si: 16.00%.
- Same module dimensions were reported (1.96 m × 0.99 m); rated power density is calculated from nameplate rating divided by module area.
- The mono system has higher installed capacity and reported annual energy yield per module area.
- The poly system has lower estimated initial system cost per kW and a slightly shorter payback period in the specific Hong Kong feed-in-tariff case study.
- The evidence does not support a universal winner. Mono is attractive where roof area and energy per area matter; poly performed slightly better on cost/payback in this particular historical scenario.

## Important limitations
- Only two specific module/system configurations are compared; this is not a statistical comparison of all mono and poly products.
- Economic inputs reflect a 2020-era Hong Kong project and policy environment. They must not be represented as current Indian market prices.
- Cost values are system-level initial investment estimates, not module-only retail prices.
- Results depend on the building, irradiance, shading, system design, tariffs and assumptions in the source study.
- A current procurement recommendation requires current Indian supplier quotations, warranties, product datasheets, temperature coefficients, degradation rates, BOS costs and site-specific solar resource data.

## Suggested resume wording
**Comparative Analysis and Selection of Solar PV Modules | Python, Pandas, Matplotlib**
- Analysed published mono-Si and poly-Si rooftop PV case-study data using Python to compare module efficiency, power density, installed capacity, system cost and energy yield.
- Calculated rated power density from module specifications and visualised performance and cost trade-offs to support application-specific module selection.
