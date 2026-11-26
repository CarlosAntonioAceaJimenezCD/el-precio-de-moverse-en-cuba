-- Consultas analiticas del esqueleto (inspiradas en Egyptian-Used-Cars).
-- Ejecutar con: sqlite3 Data/analisis_rentabilidad/data/analisis.sqlite < sql/analysis.sql
-- o adaptar a Pandas/DuckDB cuando el volumen crezca.

-- 1. KPIs basicos por fuente
SELECT source, COUNT(*) AS anuncios, ROUND(AVG(price_usd),2) AS precio_medio
FROM listings GROUP BY source ORDER BY anuncios DESC;

-- 2. Curva de depreciacion por anno (mediana)
SELECT year,
       COUNT(*) AS n,
       ROUND(MEDIAN(price_usd),2) AS mediana,
       ROUND(AVG(car_age),1) AS edad_media
FROM listings
WHERE source_type='usado' AND year BETWEEN 1990 AND 2026
GROUP BY year ORDER BY year;

-- 3. Evolucion mensual con window functions
SELECT date, price_usd,
       LAG(price_usd) OVER (PARTITION BY brand, model ORDER BY date) AS precio_anterior,
       ROUND(100.0*(price_usd - LAG(price_usd) OVER (PARTITION BY brand, model ORDER BY date))
             / NULLIF(LAG(price_usd) OVER (PARTITION BY brand, model ORDER BY date),0),2) AS variacion_pct
FROM listings
WHERE brand IS NOT NULL AND model IS NOT NULL;

-- 4. Benchmark por marca/modelo/ano
SELECT brand, model, year, COUNT(*) AS n,
       ROUND(MEDIAN(price_usd),2) AS mediana,
       ROUND(MIN(price_usd),2) AS minimo,
       ROUND(MAX(price_usd),2) AS maximo
FROM listings
GROUP BY brand, model, year HAVING n>=2;

-- 5. Infravalorados respecto a su grupo
WITH bench AS (
  SELECT brand, model, year, MEDIAN(price_usd) AS mediana
  FROM listings GROUP BY brand, model, year HAVING COUNT(*)>=2
)
SELECT l.url, l.title, l.brand, l.model, l.year, l.price_usd, b.mediana,
       ROUND(100.0*(b.mediana-l.price_usd)/b.mediana,1) AS descuento_pct
FROM listings l JOIN bench b USING (brand, model, year)
WHERE l.price_usd < b.mediana*0.8
ORDER BY descuento_pct ASC LIMIT 30;

-- 6. Anomalias de kilometraje
SELECT url, title, year, mileage_km, km_per_year
FROM listings
WHERE km_per_year > 40000 OR (km_per_year < 500 AND year < 2020);
