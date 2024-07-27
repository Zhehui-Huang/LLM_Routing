import numpy as np
import networkx as nx

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

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create a graph from city coordinates
def create_graph(cities):
    G = nx.Graph()
    for i in cities:
        for j in cities:
            if i != j:
                dist = euclidean_distance(cities[i], cities[j])
                G.add_edge(i, j, weight=dist)
    return G

# Function to perform TSP solving
def solve_tsp(G, depot):
    tour = nx.approximation.traveling_salesman_problem(G, weight='weight', cycle=True, method='greedy', source=depot)
    return tour

# Assign and solve for each robot
def assign_and_solve(cities, depots):
    graph = create_graph(cities)
    results = {}
    overall_cost = 0

    for depot in depots:
        tour = solve_tsp(graph, depot)
        tour_cost = sum(graph[u][v]['weight'] for u, v in zip(tour[:-1], tour[1:]))  # Calculate tour cost
        tour.append(depot)  # Complete the cycle
        results[depot] = (tour, tour_cost)
        overall_cost += tour_cost

        # Output the result for each robot
        print(f"Robot {depot} Tour: {results[depot][0]}")
        print(f"Robot {depot} Total Travel Cost: {results[depot][1]}")
    
    return overall_cost, results

# Run the function with specified depots
depots = [0, 1]
total_cost, details = assign_and_solve(cities, depots)

# Print the overall cost
print(f"Overall Total Travel Cost: {total_cost}")