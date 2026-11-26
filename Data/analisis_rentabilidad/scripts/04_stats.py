#!/usr/bin/env python3
"""Estadistica y econometria: depreciacion, tests, VIF y anomalias."""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import config as cfg


def vif(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    import statsmodels.api as sm

    out = []
    X = df[cols].dropna()
    for c in cols:
        y = X[c]
        x = sm.add_constant(X.drop(columns=[c]))
        try:
            r2 = sm.OLS(y, x).fit().rsquared
            out.append((c, 1 / (1 - r2) if r2 < 1 else np.inf))
        except Exception:
            out.append((c, np.nan))
    return pd.DataFrame(out, columns=["variable", "VIF"]).round(2)


def main():
    df = pd.read_parquet(cfg.DATA / "listings_clean.parquet")
    d = df[(df["source_type"] == "usado") & (df["canal"] == "local") & df["price_usd"].gt(0) & df["car_age"].notna()].copy()
    d["log_price"] = np.log(d["price_usd"])
    d = d[d["car_age"].between(0, 40)]

    modelo = pd.DataFrame()
    if len(d) > 30:
        try:
            import statsmodels.formula.api as smf

            formula = "log_price ~ car_age"
            if d["mileage_km"].notna().sum() > 30:
                formula += " + np.log1p(mileage_km)"
            if d["hp"].notna().sum() > 30:
                formula += " + hp"
            if d["condition_score"].notna().sum() > 30:
                formula += " + condition_score"
            if d["brand_tier"].nunique() > 1:
                formula += " + C(brand_tier)"
            fit = smf.ols(formula, data=d).fit()
            modelo = pd.DataFrame(
                {
                    "termino": fit.params.index,
                    "coeficiente": fit.params.values.round(4),
                    "p_valor": fit.pvalues.values.round(4),
                    "intervalo_bajo": fit.conf_int()[0].values.round(4),
                    "intervalo_alto": fit.conf_int()[1].values.round(4),
                }
            )
            (cfg.TABLES / "modelo_resumen.txt").write_text(str(fit.summary()), encoding="utf-8")
        except Exception as e:
            modelo = pd.DataFrame([{"termino": "ERROR", "coeficiente": str(e)}])

    if modelo.empty:
        modelo = pd.DataFrame([{"termino": "sin datos suficientes", "coeficiente": None}])
    modelo.to_csv(cfg.TABLES / "modelo_depreciacion.csv", index=False)

    num = ["car_age", "mileage_km", "price_usd", "hp", "condition_score"]
    cols = [c for c in num if d[c].notna().sum() > 30]
    vif_df = vif(d, cols) if len(cols) > 1 else pd.DataFrame([{"variable": "-", "VIF": None}])
    vif_df.to_csv(cfg.TABLES / "vif.csv", index=False)

    tests = []
    if d["brand_tier"].nunique() > 1 and len(d) > 30:
        groups = [g["price_usd"].values for _, g in d.groupby("brand_tier") if len(g) > 5]
        if len(groups) >= 2:
            h, p = stats.kruskal(*groups)
            tests.append(("Kruskal-Wallis precio por tier", round(h, 3), round(p, 5)))
    if d["is_new"].nunique() > 1:
        a = d[d["is_new"] == 0]["price_usd"]
        b = d[d["is_new"] == 1]["price_usd"]
        if len(a) > 5 and len(b) > 5:
            t, p = stats.ttest_ind(a, b, equal_var=False)
            tests.append(("Welch t-test usado vs nuevo", round(t, 3), round(p, 5)))
    pd.DataFrame(tests, columns=["test", "estadistico", "p_valor"]).to_csv(cfg.TABLES / "tests.csv", index=False)

    # Anomalias: km anormalmente alto/bajo para la edad y precio extremo por grupo
    d["km_anormal"] = (d["km_per_year"] > 40000) | (d["km_per_year"] < 500)
    q1, q3 = d["price_usd"].quantile([0.01, 0.99])
    d["precio_atipico"] = (d["price_usd"] < q1) | (d["price_usd"] > q3)
    anomalias = d[d["km_anormal"] | d["precio_atipico"]][
        ["url", "title", "price_usd", "year", "mileage_km", "km_per_year", "km_anormal", "precio_atipico"]
    ]
    anomalias.to_csv(cfg.TABLES / "anomalias.csv", index=False)

    print(f"STATS: {len(d)} observaciones | modelo={len(modelo)} terminos | anomalias={len(anomalias)}")


if __name__ == "__main__":
    main()
