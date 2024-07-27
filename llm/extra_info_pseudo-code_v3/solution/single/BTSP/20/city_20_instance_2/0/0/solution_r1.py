import math
import networkx as nx

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def construct_graph(cities, threshold):
    G = nx.Graph()
    number_of_cities = len(cities)
    G.add_nodes_from(range(number_of_cities))
    for i in range(number_of_cities):
        for j in range(i + 1, number_of_cities):
            distance = euclidean_distance(cities[i], cities[j])
            if distance <= threshold:
                G.add_edge(i, j, weight=distance)
    return G

def find_hamiltonian_path(G, start_node):
    if nx.is_connected(G):
        try:
            path = nx.approximation.traveling_salesman_problem(G, cycle=False, weight='weight')
            if path[0] == start_node:
                return path
        except nx.NetworkXError:
            pass
    return None

def bottleneck_tsp(cities):
    max_edge_length = 0
    all_distances = [
        euclidean_distance(cities[i], cities[j]) 
        for i in range(len(cities)) for j in range(i + 1, len(cities))
    ]
    
    lower, upper = min(all_distances), max(all_distances)
    
    while lower <= upper:
        mid = (lower + upper) / 2
        G = construct_graph(cities, mid)
        path = find_hamiltonian_path(G, 0)
        if path and path[-1] == 0:  # Check if it ends where it starts
            best_path = path
            max_edge_length = mid
            upper = mid - 0.1
        else:
            lower = mid + 0.1
            
    # Calculate total cost and max distance between consecutive cities
    total_cost = sum(euclidean_distance(cities[best_path[i]], cities[best_path[i+1]]) for i in range(len(best_path) - 1))
    max_distance = max(euclidean_distance(cities[best_path[i]], cities[best-\\\>_path[i+1]]) for i in range(len(best_path) - 1))
    
    return best_path, total_cost, max_distance

cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), 
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), 
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

tour, total_cost, max_distance = bottleneck_tsp(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)