import networkx as nx
import matplotlib.pyplot as plt
import math
import base64
import io
from weasyprint import HTML

def generar_datos_y_grafico(n_min=100, phi=1.25, grupos=[2, 3]):
    Z = math.prod(grupos)
    caracteristicas_x = [1]
    for p in grupos[:-1]:
        caracteristicas_x.append(caracteristicas_x[-1] * p)

    etapas_relaciones = []
    for p, x in zip(grupos, caracteristicas_x):
        relaciones = [phi**(i * x) for i in range(p)]
        etapas_relaciones.append(relaciones)

    G = nx.DiGraph()
    nodo_inicial = "Entrada"
    G.add_node(nodo_inicial, capa=0, rpm=n_min)
    capa_actual = [(nodo_inicial, n_min)]

    for i, relaciones in enumerate(etapas_relaciones):
        siguiente_capa = []
        for nombre_origen, rpm_origen in capa_actual:
            for j, rel in enumerate(relaciones):
                rpm_destino = rpm_origen * rel
                nombre_destino = f"{nombre_origen}_R{j}"
                G.add_node(nombre_destino, capa=i+1, rpm=rpm_destino)
                G.add_edge(nombre_origen, nombre_destino, relacion=rel)
                siguiente_capa.append((nombre_destino, rpm_destino))
        capa_actual = siguiente_capa

    # Posicionamiento para el gráfico
    posiciones = {}
    escalones_y = set()
    for nodo, datos in G.nodes(data=True):
        x = datos['capa']
        escalon_y = int(round(math.log(datos['rpm'] / n_min) / math.log(phi)))
        posiciones[nodo] = (x, escalon_y)
        escalones_y.add(escalon_y)

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    plt.title(f"Diagrama de Rayos (Progresion Geometrica phi={phi})", fontsize=14, fontweight='bold')
    nx.draw(G, posiciones, with_labels=False, node_size=100, node_color='#2c3e50', edge_color='#7f8c8d', width=1)
    
    etiquetas_aristas = {}
    for u, v, d in G.edges(data=True):
        rel = d['relacion']
        potencia = int(round(math.log(rel) / math.log(phi))) if rel > 1 else 0
        etiquetas_aristas[(u, v)] = f"phi^{potencia}"
    nx.draw_networkx_edge_labels(G, posiciones, edge_labels=etiquetas_aristas, font_size=8)

    escalones_ordenados = sorted(list(escalones_y))
    etiquetas_rpm = [f"{n_min * (phi**e):.1f}" for e in escalones_ordenados]
    plt.yticks(escalones_ordenados, etiquetas_rpm)
    plt.ylabel("Velocidades (RPM)")
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    
    # Guardar gráfico a base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
    plt.close()
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Datos para el informe
    velocidades_finales = sorted([datos['rpm'] for nodo, datos in G.nodes(data=True) if datos['capa'] == len(grupos)])
    
    return img_base64, velocidades_finales, etapas_relaciones, Z

def crear_pdf_informe(n_min, phi, grupos, img_b64, v_finales, etapas, Z):
    # Generar tabla de relaciones
    relaciones_html = ""
    for i, etapa in enumerate(etapas):
        rels_text = ", ".join([f"{r:.3f}" for r in etapa])
        relaciones_html += f"<tr><td>Etapa {i+1}</td><td>{grupos[i]}</td><td>{rels_text}</td></tr>"

    # Generar tabla de velocidades finales
    v_html = ""
    for i, v in enumerate(v_finales):
        v_html += f"<tr><td>Z<sub>{i+1}</sub></td><td>{v:.2f} RPM</td></tr>"

    html_content = f"""
    <html>
    <head>
        <style>
            @page {{ size: A4; margin: 20mm; background-color: #ffffff; }}
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; line-height: 1.6; margin: 0; padding: 0; }}
            .header {{ background-color: #2c3e50; color: white; padding: 30px; margin: -20mm -20mm 20px -20mm; text-align: center; }}
            h1 {{ margin: 0; font-size: 24pt; }}
            h2 {{ color: #2c3e50; border-bottom: 2px solid #34495e; padding-bottom: 5px; margin-top: 30px; }}
            .summary-box {{ background-color: #f8f9fa; border-left: 5px solid #2c3e50; padding: 15px; margin: 20px 0; }}
            table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
            th {{ background-color: #ecf0f1; font-weight: bold; }}
            .diagram-container {{ text-align: center; margin-top: 30px; }}
            .diagram-container img {{ max-width: 100%; border: 1px solid #ccc; }}
            .footer {{ text-align: center; font-size: 9pt; color: #7f8c8d; margin-top: 50px; border-top: 1px solid #eee; padding-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Informe Técnico de Regulación de Velocidades</h1>
            <p>Diseño de Caja de Engranajes en Progresión Geométrica</p>
        </div>

        <h2>1. Parámetros de Diseño</h2>
        <div class="summary-box">
            <p><strong>Fórmula Estructural:</strong> Z = {" x ".join(map(str, grupos))} = {Z} velocidades.</p>
            <p><strong>Velocidad Mínima (n<sub>min</sub>):</strong> {n_min} RPM</p>
            <p><strong>Razón Geométrica (&phi;):</strong> {phi}</p>
        </div>

        <h2>2. Relaciones de Transmisión por Etapa</h2>
        <table>
            <thead>
                <tr>
                    <th>Etapa</th>
                    <th>Nº Engranajes</th>
                    <th>Relaciones (&phi;<sup>x</sup>)</th>
                </tr>
            </thead>
            <tbody>
                {relaciones_html}
            </tbody>
        </table>

        <h2>3. Diagrama de Rayos (Kinemático)</h2>
        <div class="diagram-container">
            <img src="data:image/png;base64,{img_b64}" />
        </div>

        <div style="page-break-before: always;"></div>

        <h2>4. Velocidades de Salida Resultantes</h2>
        <p>A continuación se detallan las velocidades obtenidas en el último eje, ordenadas de forma ascendente:</p>
        <table style="width: 50%; margin: 0 auto;">
            <thead>
                <tr>
                    <th>Designación</th>
                    <th>Velocidad (RPM)</th>
                </tr>
            </thead>
            <tbody>
                {v_html}
            </tbody>
        </table>

        <div class="footer">
            Generado por Sistema de Diseño Mecánico Automatizado - 2024
        </div>
    </body>
    </html>
    """
    HTML(string=html_content).write_pdf("Informe_Tecnico_Velocidades.pdf")

# Ejecución
n_min = 100
phi = 1.25
grupos = [2, 3] # Caja de 2x3=6 velocidades

img_b64, v_finales, etapas, Z = generar_datos_y_grafico(n_min, phi, grupos)
crear_pdf_informe(n_min, phi, grupos, img_b64, v_finales, etapas, Z)
print("PDF generado con éxito.")