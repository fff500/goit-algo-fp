import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra_heap(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    G = nx.Graph()
    # Stores and restaurants in my town
    G.add_nodes_from(["Home", "PD", "C1", "C2", "A", "L", "IM", "BK", "TP"])

    G.add_edge("Home", "PD", weight=2)
    G.add_edge("PD", "C1", weight=8)
    G.add_edge("C1", "C2", weight=2)
    G.add_edge("C1", "TP", weight=2)
    G.add_edge("TP", "C2", weight=3)
    G.add_edge("C2", "A", weight=2)
    G.add_edge("A", "L", weight=1)
    G.add_edge("A", "BK", weight=1)
    G.add_edge("BK", "L", weight=1)
    G.add_edge("A", "IM", weight=2)
    G.add_edge("IM", "Home", weight=10)
    G.add_edge("IM", "C1", weight=6)

    print("Dijkstra with heap:")
    print(dijkstra_heap(G, 'Home'))

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

if __name__ == "__main__":
    main()
