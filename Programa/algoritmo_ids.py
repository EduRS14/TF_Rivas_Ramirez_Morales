import networkx as nx
import matplotlib.pyplot as plt

def iterative_ids(graph, start, goal, initial_depth, max_depth):
    for depth in range(initial_depth, max_depth + 1):
        result = dls(graph, start, goal, depth)
        if result is not None:
            return result
    return None

def dls(graph, current, goal, depth, path=[]):
    path = path + [current]
    
    if current == goal:
        return path
    
    if depth == 0:
        return None
    
    for neighbor in graph.neighbors(current):
        if neighbor not in path:
            new_path = dls(graph, neighbor, goal, depth - 1, path)
            if new_path is not None:
                return new_path
    
    return None

def draw_graph(graph, path):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=False, font_weight='bold', width = 0.1, node_size=10, font_size=8)
    
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    edge_labels = {(path[i], path[i + 1]): i + 1 for i in range(len(path) - 1)}
    
    nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='r', width=2)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    
    plt.show()

def draw_subgraph(graph, path):
    subgraph = graph.subgraph(path)
    pos = nx.spring_layout(subgraph)
    nx.draw(subgraph, pos, with_labels=True, font_weight='bold', node_size=20, node_color='skyblue', font_color='black', font_size=8, width = 0.5)
    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(subgraph, pos, edgelist=edges, edge_color='r', width=2)
    plt.show()