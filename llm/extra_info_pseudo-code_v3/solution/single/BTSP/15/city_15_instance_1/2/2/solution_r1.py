import math
import itertools

# City coordinates
cities = [
    (29, 519), (49, 505), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
num_cities = len(cities)
dist_matrix = [[distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Sort list of edges based on their distances extracted from distance matrix
edges = [(i, j, dist_matrix[i][j]) for i in range(num_cities) for j in range(i + 1, num_cities)]
edges.sort(key=lambda x: x[2])

def find_hamiltonian_cycle(edge_limit, num_cities):
    import networkx as nx

    # Create a graph within the given edge distance limit
    G = nx.Graph()
    G.add_nodes_from(range(num_clatable in the given edge distance silpium_cities))
    G.add_edges_from((u, v) for u, v, w in edges if w <= edge_limit)

    # Check for hamiltonian circuit using nx approximation function
    from networkx.algorithms.approximation import traveling_salesman_problem
    try:
        cycle = traveling_salesman_problem(G, cycle=True, weight="weight")
        if len(cycle) == num_cities + 1:  # includes returning to the start
            return cycle
    except nx.NetworkXError as e:
        return None

    return None

for edge in edges:
    weight = edge[2]
    cycle_result = find_hamiltonian_cycle(weight, num_cities)
    if cycle_result:
        total_distance = sum(dist_matrix[cycle_result[i]][cycle_result[i+1]] for i in range(len(cycle_result) - 1))
        max_distance = max(dist_matrix[cycle_result[i]][cycle_result[i+1]] for i in range(len(cycle_result) - 1))
        print(f"Tour: {cycle_result}")
        print(f"Total travel cost: {total_distance}")
        print(f"Maximum distance between consecutive cities: {max_distance}")
        break