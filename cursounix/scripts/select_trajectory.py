#!/usr/bin/env python3
"""
select_trajectory.py
Genera una lista de nombres de archivo (face_XXXXX.png) que siguen una trayectoria en espacio (alpha, beta)
Uso ejemplo:
  python3 select_trajectory.py circle cx cy r n > traj_list.txt
  python3 select_trajectory.py line ax ay bx by n > traj_list.txt
Devuelve filenames una por línea, en orden.
"""
import sys
import math

def k_from_ab(alpha, beta):
    # alpha range 0..270 -> j
    # beta range 0..79 -> i
    a = int(round(alpha)) % 271
    b = int(round(beta))
    if b < 0: b = 0
    if b > 79: b = 79
    k = b * 271 + a
    return "fres2_%05d.png" % k

def circle(cx, cy, r, n):
    out = []
    for t in range(n):
        theta = 2*math.pi * t / max(1,n-1)
        a = cx + r*math.cos(theta)
        b = cy + r*math.sin(theta)
        out.append(k_from_ab(a,b))
    # remove duplicates while preserving order
    seen = set(); uniq=[]
    for x in out:
        if x not in seen:
            seen.add(x); uniq.append(x)
    return uniq

def line(ax, ay, bx, by, n):
    out=[]
    for t in range(n):
        s = t / max(1,n-1)
        a = ax + (bx-ax)*s
        b = ay + (by-ay)*s
        out.append(k_from_ab(a,b))
    seen=set(); uniq=[]
    for x in out:
        if x not in seen:
            seen.add(x); uniq.append(x)
    return uniq

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: select_trajectory.py circle cx cy r n  OR line ax ay bx by n", file=sys.stderr)
        sys.exit(1)
    typ = sys.argv[1]
    if typ == "circle":
        _,_, cx, cy, r, n = sys.argv
        out = circle(float(cx), float(cy), float(r), int(n))
    elif typ == "line":
        _,_, ax, ay, bx, by, n = sys.argv
        out = line(float(ax), float(ay), float(bx), float(by), int(n))
    else:
        print("Tipo no reconocido", file=sys.stderr); sys.exit(1)
    for name in out:
        print(name)
