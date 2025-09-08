#!/usr/bin/env python3
"""
analyze_images.py
Uso:
  python3 analyze_images.py dataset/raw > metadata.csv
o
  python3 analyze_images.py dataset/raw/face_00012.png
Salida (CSV):
filename,index,i,j,alpha,beta,size_bytes
"""
import os
import re
import sys

def analyze_file(path):
    # Extract filename and index
    fname = os.path.basename(path)
    m = re.match(r'fres2_(\d{5})\.png$', fname)
    if not m:
        return None
    idx = int(m.group(1))
    # mapping to i,j (beta,i) and alpha (j)
    j = idx % 271
    i = idx // 271
    alpha = j
    beta = i
    size = os.path.getsize(path)
    return (fname, idx, i, j, alpha, beta, size)

def process_path(p):
    if os.path.isdir(p):
        for entry in sorted(os.listdir(p)):
            full = os.path.join(p, entry)
            if os.path.isfile(full):
                out = analyze_file(full)
                if out:
                    print(','.join(map(str,out)))
    else:
        out = analyze_file(p)
        if out:
            print(','.join(map(str,out)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 analyze_images.py <archivo|dir>", file=sys.stderr)
        sys.exit(1)
    for arg in sys.argv[1:]:
        process_path(arg)
