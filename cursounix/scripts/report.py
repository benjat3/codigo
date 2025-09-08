#!/usr/bin/env python3
# Genera un archivo de reporte.
import csv, sys, statistics

if len(sys.argv) != 2:
    print("Uso: report.py <metadata.csv>")
    sys.exit(1)

meta = sys.argv[1]
alphas=[]; betas=[]; sizes=[]
with open(meta,newline='') as f:
    r = csv.DictReader(f, fieldnames=["filename","index","i","j","alpha","beta","size"])
    for row in r:
        try:
            alphas.append(float(row["alpha"]))
            betas.append(float(row["beta"]))
            sizes.append(int(row["size"]))
        except:
            pass
print("count:", len(alphas))
print("alpha mean:", statistics.mean(alphas) if alphas else 0)
print("beta mean:", statistics.mean(betas) if betas else 0)
print("size mean (bytes):", int(statistics.mean(sizes)) if sizes else 0)
