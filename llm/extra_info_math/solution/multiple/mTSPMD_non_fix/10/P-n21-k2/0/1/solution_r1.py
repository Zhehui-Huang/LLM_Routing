import math
import networkx as nx

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Calculate Euclidean distance
def calc_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Create the complete graph
G = nx.Graph()
for city in cities:
    for other_city in cities:
        if city != other_city:
            G.add_edge(city, other_city, weight=calc_distance(city, other_city))

# Number of robots - each robot using a separate depot
robots = 2

# Execute TSP separately from each depot using a simple heuristic:
# Here we use the MST TSP heuristic from NetworkX.
tours = []
tour_costs = []
for depot in range(robots):
    mst = nx.minimum_spanning_tree(G)  # Minimum Spanning Tree of the graph G
    odd_degree_nodes = [n for n in mst.degree if n[1] % 2 == 1]  # nodes with odd degree
    odd_matching_subset = nx.max_weight_matching(G.subgraph(odd_degree_nodes), maxcardinality=True)
    mst.add_edges_from(odd_matching_subset)
    eulerian_circuit = list(nx.eulerian_circuit(mst, source=depot))
    visited = set()
    path = [depot]
    cost = 0
    last_city = depot
    for edge in eulerian_circuit:
        if edge[1] not in visited or edge[1] == depot:
            visited.add(edge[1])
            cost += G[last_city][edge[1]]['weight']
            last_city = edge[1]
            path.append(edge[1])
    path.append(depot)  # return to starting depot
    cost += G[last_city][depot]['weight']  # include the return cost to depot
    tours.append(path)
    tour_costs.append(cost)

# Output the tours and costs
overall_cost = sum(tour_costs)
for index, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")