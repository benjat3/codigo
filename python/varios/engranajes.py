import networkx as nx
import matplotlib.pyplot as plt

def diagrama_caja_velocidades():
    # 1. Configuración Inicial
    rpm_entrada = 1000  # Velocidad inicial del motor
    
    # Relaciones de transmisión por etapa (Ej: 2 engranajes y luego 3 engranajes)
    etapas = [
        [0.5, 1.2],         # Etapa 1: del Motor al Eje 1 (2 opciones)
        [0.8, 1.0, 6]     # Etapa 2: del Eje 1 al Eje 2 (3 opciones)
    ]

    G = nx.DiGraph()

    # Nodo inicial
    nodo_motor = "Motor"
    G.add_node(nodo_motor, capa=0, rpm=rpm_entrada)
    capa_actual = [(nodo_motor, rpm_entrada)]

    # 2. Calcular todas las combinaciones y ramificaciones
    for i, relaciones in enumerate(etapas):
        siguiente_capa = []
        for nombre_origen, rpm_origen in capa_actual:
            for j, rel in enumerate(relaciones):
                # Calcular nueva velocidad
                rpm_destino = rpm_origen * rel
                
                # Crear un nombre único para el nodo basado en la ruta
                nombre_destino = f"{nombre_origen}_R{j}"
                
                # Agregar nodo y conexión a la red
                G.add_node(nombre_destino, capa=i+1, rpm=rpm_destino)
                G.add_edge(nombre_origen, nombre_destino, relacion=rel)
                
                siguiente_capa.append((nombre_destino, rpm_destino))
        
        capa_actual = siguiente_capa

    # 3. Definir la posición en el gráfico (X = Eje, Y = Velocidad RPM)
    posiciones = {}
    for nodo, datos in G.nodes(data=True):
        posiciones[nodo] = (datos['capa'], datos['rpm'])

    # 4. Obtener y ordenar las velocidades finales
    velocidades_finales = [datos['rpm'] for nodo, datos in G.nodes(data=True) if datos['capa'] == len(etapas)]
    velocidades_finales.sort()

    # Imprimir en consola el resultado ordenado
    print(f"--- Se generaron {len(velocidades_finales)} combinaciones de velocidad ---")
    for i, v in enumerate(velocidades_finales):
        print(f"Velocidad {i+1}: {v:.1f} RPM")

    # 5. Dibujar el diagrama
    plt.figure(figsize=(10, 7))
    plt.title(f"Diagrama de Árbol de Velocidades ({len(velocidades_finales)} combinaciones finales)", fontsize=14, fontweight='bold')

    # Dibujar red
    nx.draw(G, posiciones, with_labels=False, node_size=300, node_color='#ff9999', edge_color='gray', width=1.5)

    # Etiquetas de las aristas (muestran la relación de transmisión elegida)
    etiquetas_aristas = {(u, v): f"x{d['relacion']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, posiciones, edge_labels=etiquetas_aristas, font_size=9, label_pos=0.6)

    # Etiquetas de los nodos (muestran las RPM en cada punto)
    margen_y = max(velocidades_finales) * 0.03
    for nodo, (x, y) in posiciones.items():
        plt.text(x, y + margen_y, f"{y:.1f}", ha='center', va='bottom', fontsize=10, fontweight='bold', color='darkblue')

    # Configurar los ejes del gráfico
    nombres_ejes = ['Motor'] + [f'Eje {i+1}' for i in range(len(etapas))]
    plt.xticks(range(len(etapas) + 1), nombres_ejes, fontsize=12)
    plt.ylabel("Velocidad Resultante (RPM)", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Habilitar ejes cartesianos para ver la escala
    plt.axis('on')
    # Ajustar límites del eje X para que los textos no se corten
    plt.xlim(-0.5, len(etapas) + 0.5) 
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    diagrama_caja_velocidades()