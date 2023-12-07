# Semestral - Nitsy Balabarca e Ivys Sánchez

# Importar las bibliotecas necesarias
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Función para calcular y mostrar la ruta más corta
def calcular_ruta():
    # Obtener los nombres de inicio y destino desde las entradas de la interfaz gráfica
    inicio = entrada_inicio.get()
    destino = entrada_destino.get()
     # Calcular la ruta más corta y su tiempo
    camino_corto = nx.shortest_path(Grafo, inicio, destino, weight='weight')
    tiempo = nx.shortest_path_length(Grafo, inicio, destino, weight='weight')
    leyenda = f"El Camino Corto es: {camino_corto} y toma {tiempo} Kilómetros"
    label_resultado.config(text=leyenda)

    # Especificar posiciones de nodos manualmente
    pos = {
        "Aguadulce": (0.002, 0.004),
        "Penonomé": (1.151, 0.959),
        "Antón": (1.987, 0.560),
        "Natá": (0.687,0.0361),
        "La Pintada": (0.199,0.944),
        "Olá": (0.251, 0.555)
    }

    # Crear y mostrar el gráfico con la ruta más corta
    nx.draw(Grafo, pos, node_size=1300, node_color='pink', font_size=8, font_weight='bold', with_labels=True)
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=nx.get_edge_attributes(Grafo, "weight"))
    
    # Resaltar la ruta más corta en color morado
    edge_list = [(camino_corto[i], camino_corto[i + 1]) for i in range(len(camino_corto) - 1)]
    nx.draw_networkx_edges(Grafo, pos, edgelist=edge_list, edge_color='purple', width=2)
    
    # Configurar título y guardar la visualización como una imagen PNG
    plt.title("Grafo con Ruta Más Corta Entre Los Distritos de la Provincia de Coclé")
    plt.savefig("Graph.png", format="PNG")
    plt.show()

# Crear el grafo
Grafo = nx.Graph()
Grafo.add_node("Aguadulce")
Grafo.add_node("Penonomé")
Grafo.add_node("Antón")
Grafo.add_node("Natá")
Grafo.add_node("La Pintada")
Grafo.add_node("Olá")

# Agregar nodos y aristas al grafo
Grafo.add_edge("Antón", "Penonomé", weight=34.9)
Grafo.add_edge("Penonomé", "La Pintada", weight=15.3)
Grafo.add_edge("La Pintada", "Olá", weight=55.5)
Grafo.add_edge("Natá", "Olá", weight=37.6)
Grafo.add_edge("Natá", "Aguadulce", weight=19.3)
Grafo.add_edge("Natá", "Penonomé", weight=27.1)
Grafo.add_edge("Natá","La Pintada", weight=61.0)
Grafo.add_edge("Antón", "Natá", weight=63.2)

# Crear la interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Calculadora de Ruta Más Corta")

# Crear etiquetas y entradas para ingresar los distritos de inicio y destino
etiqueta_inicio = ttk.Label(ventana, text="Distrito de Inicio:")
etiqueta_inicio.grid(column=0, row=0, padx=10, pady=10)

entrada_inicio = ttk.Entry(ventana)
entrada_inicio.grid(column=1, row=0, padx=10, pady=10)

etiqueta_destino = ttk.Label(ventana, text="Distrito de Destino:")
etiqueta_destino.grid(column=0, row=1, padx=10, pady=10)

entrada_destino = ttk.Entry(ventana)
entrada_destino.grid(column=1, row=1, padx=10, pady=10)

# Crear botón para calcular la ruta
boton_calcular = ttk.Button(ventana, text="Calcular Ruta", command=calcular_ruta)
boton_calcular.grid(column=0, row=2, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(ventana, text="")
label_resultado.grid(column=0, row=3, columnspan=2, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
