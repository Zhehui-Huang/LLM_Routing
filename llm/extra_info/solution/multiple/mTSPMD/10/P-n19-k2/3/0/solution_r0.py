import numpy as np
import networkx as nx

# Define the locations of each city, including depots.
cities = {
    0: (30, 40),  # Depot for robot 0
    1: (37, 52),  # Depot for robot 1
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Compute distances between all pairs of cities
def euclidean_distance(p1, p2):
    return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

# Create a full graph of cities
def create_graph(cities):
    G = nx.Graph()
    for u in cities:
        for v in cities:
            if u != v:
                dist = euclidean_distance(cities[u], cities[v])
                G.add_edge(u, v, weight=dist)
    return G

# Solve TSP for a given set of cities
def solve_tsp(G, nodes):
    subG = G.subgraph(nodes)
    # Approximate TSP solution using the greedy approach
    cycle = nx.approximation.greedy_tsp(subG, source=nodes[0])
    return cycle

# Assign cities to nearest depot
def assign_cities_to_depots(cities, depots):
    assignments = {depot: [depot] for depot in depots}
    for city in cities:
        if city not in depots:
            nearest_depot = min(depots, key=lambda depot: euclidean_distance(cities[city], cities[depot]))
            assignments[nearest_depot].append(city)
    return assignments

# Main computation starts here
depots = [0, 1]
city_assignments = assign_cities_to_depots(cities, depots)

# Initialize the graph
G = create_graph(cities)

# Solve TSP separately for each depot and robot
overall_cost = 0
robot_tours = {}

for depot in depots:
    assigned_cities = city_assignments[depot]
    if len(assigned_cities) > 1:
        tsp_tour = solve_tsp(G, assigned_cities + [depot])
        tour_cost = sum(G[u][v]['weight'] for u, v in zip(tsp_tour[:-1], tsp_tour[1:])) + G[tsp_tour[-1]][tsp_tour[0]]['weight']
        robot_tours[depot] = (tsp_tour, tour_cost)
        overall_cost += tour_costs
    
    # Output the results for each robot
    print(f"Robot {depot} Tour: {robot_tours[depot][0]}")
    print(f"Robot {depot} Total Travel Cost: {robot_tours[depot][1]}")

# Output the overall total travel cost
print(f"Overall Total Travel Cost: {overall_cost}")