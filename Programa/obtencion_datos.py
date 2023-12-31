import csv
import random
import networkx as nx
import matplotlib.pyplot as plt

def save_graph_to_txt(graph, filename):
    with open(filename, 'w') as file:
        for edge in graph.edges():
            file.write(f"{edge[0]} {edge[1]}\n")

def load_graph_from_txt(filename):
    graph = nx.Graph()
    with open(filename, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            if len(nodes) == 2:
                graph.add_edge(int(nodes[0]), int(nodes[1]))
    return graph

def generarGrafo():
    
    #Nombre del archivo
    archivo_csv = 'data_set.csv'

    # Índices de las columnas que deseamos incluir en la lista
    indices_columnas = [0, 7]
    # Lista para almacenar los datos del CSV
    datos_csv = []

    # Abrimos el archivo CSV y leemos los datos
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)

        # Iteramos sobre las filas y agregamos solo ciertas columnas a la lista
        for fila in lector_csv:
            datos_filtrados = [fila[i] for i in indices_columnas]
            datos_csv.append(datos_filtrados)

    # Mostramos los datos almacenados en la lista
    #for fila in datos_csv:
    #    print(fila)

    # Inicializamos la lista de amigos con listas vacías
    amigos = []
    rango = range(0,1500)

    for i in range(1500):
        num_elementos = int(datos_csv[i][1])
        numeros_disponibles = list(rango)  # Copia del rango original
        numeros_disponibles.remove(i)  # Elimina el número de esa fila
        numeros_aleatorios = random.sample(numeros_disponibles, num_elementos)
        amigos.append(numeros_aleatorios)
        
    #for fila in amigos:
    #    print(fila)
        
    grafo = []

    for i in range(1500):
        for j in range(len(amigos[i])):
            grafo.append((i,amigos[i][j]))
    
    
    #print(grafo)
    G=nx.Graph()
    G.add_edges_from(grafo)
    save_graph_to_txt(G, 'grafo.txt')
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=False, width=0.1, node_size=10, font_size=8)
    plt.savefig("grafo.png")
    plt.show()
    
    return grafo

#G = load_graph_from_txt("grafo.txt")
#pos = nx.kamada_kawai_layout(G)
#nx.draw(G, pos, with_labels=False, width=0.1, node_size=10, font_size=8)
#plt.savefig("grafo.png")
#plt.show()