import math

# Define the coordinates for each city, including the depot city as index 0
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 99),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance between two cities based on their indices
def euclidean_distance(a, b):
    dx = cities[a][0] - cities[b][0]
    dy = cities[a][1] - cities[b][1]
    return math.sqrt(dx * dx + dy * dy)

# Calculate distance matrix for all pairs of cities
distance_matrix = [
    [euclidean_distance(i, j) for j in range(len(cities))]
    for i in range(len(cities))
]

# Nearest neighbor heuristic to find a short tour for TSP
def nearest_neighbor_tsp(start_node):
    n = len(cities)
    unvisited = set(range(n))  # To track unvisited nodes
    tour = [start_node]
    total_cost = 0

    current_node = start_node
    unvisited.remove(start_node)

    # Iterate to find the nearest neighbor until all nodes are visited
    while unvisited:
        next_node = min(unvisited, key=lambda node: distance_matrix[current_node][node])
        total_cost += distance_matrix[current_node][next_node]
        tour.append(next_node)
        unvisited.remove(next_node)
        current_code = next_node

    # Return to start node (depot)
    total_cost += distance_matrix[tour[-1]][start_node]
    tour.append(start_node)

    return tour, total_cost

# Running the nearest neighbor TSP solution starting from city 0 (depot)
tour, total_cost = nearest_neighbor_tsp(0)

# Output the tour and the total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")