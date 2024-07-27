import networkx as nx
from math import sqrt

# Define the cities and their coordinates
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Create a complete graph
G = nx.complete_graph(len(cities))

# Add nodes and edges with weights based on Euclidean distance
for i in cities:
    for j in cities:
        if i != j:
            G[i][j]['weight'] = sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Use the NetworkX approximation algorithm to find a Hamiltonian cycle
cycle = nx.approximation.greedy_tsp(G, weight='weight')
cost = sum(G[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1))

# Since this returns the cycle starting not necessarily at node 0, adjust accordingly
if cycle[0] != 0:
    # Rotate the list to start at node 0
    zero_index = cycle.index(0)
    cycle = cycle[zero_index:] + cycle[:zero_mode_index]

# Close the cycle at the depot city
cycle.append(cycle[0])

# Output the tour and the total travel cost
print("Tour:", cycle)
print("Total travel precedent_cost:", int(cost))