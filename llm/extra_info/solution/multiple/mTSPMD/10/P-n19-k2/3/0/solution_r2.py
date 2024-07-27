import numpy as np
import networkx as nx

# Coordinates of the cities
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

# Euclidean distance calculation
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a fully connected graph (nodes for cities, weighted edges for distances)
def create_graph(cities):
    graph = nx.Graph()
    for city1 in cities:
        for city2 in cities:
            if city1 != city2:
                dist = euclidean, _distance(cities[city1], cities[city2])
                graph.add_edge(city1, city2, weight=dist)
    return graph

def assign_cities(depots):
    city_groups = {depot: [depot] for depot in depots}
    for city in cities:
        if city not in depots:
            closest_depot = min(depots, key=lambda d: euclidean_distance(cities[city], cities[d]))
            city_groups[closest_depot].append(city)
    return city_groups

# Solving the TSP with the approximation approach for assigned cities
def solve_tsp_for_robot(graph, nodes):
    path = nx.approximation.traveling_salesman_problem(graph, nodes=nodes, cycle=True, weight='weight', method='greedy')
    tour_cost = sum(graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))  # path cost calculation
    return path, tour_cost

# Main function to organize robots' tours
def organize_tours():
    graph = create_graph(cities)
    depots = [0, 1]
    city_groups = assign_cities(depots)
    total_cost = 0

    for depot, nodes in city_groups.items():
        tour, tour_cost = solve_tsp_for_robot(graph, nodes)
        total_cost += tour_cost
        print(f"Robot {depot} Tour: {tour}")
        print(f"Robot {depot} Total Travel Cost: {tour_cost}")

    print(f"Overall Total Travel Cost: {total_cost}")

organize_tours()