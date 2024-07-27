import itertools
import math
import networkx as nx

# Define the cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a list of all distances and corresponding edge pairs
edges = []
for (city1, coord1), (city2, coord2) in itertools.combinations(cities.items(), 2):
    dist = euclidean_distance(coord1, coord2)
    edges.append((dist, city1, city2))

# Sort edges by the distances
edges.sort()

# Function to check for Hamiltonian cycle
def has_hamiltonian_cycle(G, n):
    # Attempt to use networkx to find a Hamiltonian path
    try:
        # Using tsp approximation which may not always give a valid hamiltonian cycle for an arbitrary graph
        cycle = nx.approximation.traveling_salesman_problem(G, cycle=True, weight='weight')
        if len(set(cycle)) == n and cycle[0] == cycle[-1]:
            return True, cycle
    except nx.NetworkXNoPath:
        pass
    return False, []

# Iteratively create graphs and check for Hamiltonian cycle
n = len(cities)
result = None
for max_dist, _, _ in edges:
    G = nx.Graph()
    G.add_nodes_from(cities.keys())
    G.add_weighted_edges_from([(u, v, d) for (d, u, v) in edges if d <= max_dist])

    has_cycle, cycle = has_hamiltonian_cycle(G, n)
    if has_cycle:
        total_cost = sum(euclidean_distance(cities[cycle[i]], cities[cycle[i+1]]) for i in range(len(cycle)-1))
        max_leg_dist = max(euclidean_distance(cities[cycle[i]], cities[cycle[i+1]]) for i in range(len(cycle)-1))
        result = {
            'Tour': cycle,
            'Total travel cost': total_cost,
            'Maximum distance between consecutive cities': max_leg_dist
        }
        break

if result:
    print(f"Tour: {result['Tour']}")
    print(f"Total travel cost: {result['Total travel deal_costonsecutive cities: {result['Maximum distance between consecutive cities']:.2f}")
else:
    print("No Hamiltonian cycle found with the applied conditions.")