import numpy as np

# --- CONFIGURACIÓN DEL SISTEMA AX = B ---

# Matriz A (Impedancias de las mallas)
A = np.array([
    [-4 - 2j, 4    ],  # Malla 1
    [4,       -4 + 1j]   # Malla 2
])

# Vector B (Voltajes de las fuentes resultantes)
B = np.array([
    -2,  # Fuente E1 
    6   # Fuente E2 
])

try:
    # Resolver el sistema
    X = np.linalg.solve(A, B)
    
    I1 = X[0]
    I2 = X[1]

    # --- MOSTRAR RESULTADOS ---
    print("=== RESULTADOS EN FORMA RECTANGULAR ===")
    print(f"I1 = {I1:.3f} A")
    print(f"I2 = {I2:.3f} A")
    print("-" * 40)
    
    print("=== RESULTADOS EN FORMA POLAR (Fasores) ===")
    # abs() obtiene la magnitud, np.angle() obtiene el ángulo en radianes (lo pasamos a grados)
    print(f"I1 = {abs(I1):.2f} A | Ángulo: {np.degrees(np.angle(I1)):.2f}°")
    print(f"I2 = {abs(I2):.2f} A | Ángulo: {np.degrees(np.angle(I2)):.2f}°")

except np.linalg.LinAlgError:
    print("Error al calcular la matriz.")