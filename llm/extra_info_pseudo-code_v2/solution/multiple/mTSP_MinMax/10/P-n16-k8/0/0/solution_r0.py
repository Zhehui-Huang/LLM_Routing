import numpy as np

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
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
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Calculation of distances
def euclidean_dist(a, b):
    return np.hypot(b[0] - a[0], b[1] - a[1])

# Create distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_dist(cities[i], cities[j])

# Initialization procedure
def initialize(num_robots, distance_matrix):
    nodes = list(range(1, num_cities))  # exclude the depot city from initialization
    nodes.sort(key=lambda x: distance_matrix[0][x])  # sort by distance to the depot

    tours = [[] for _ in range(num_robots)]
    for i in range(num_robots):
        if nodes:
            tours[i].append(nodes.pop(0))  # assign the closest node to each robot initially

    # Assign remaining nodes to the closest tour base on the cost function
    while nodes:
        min_cost = float('inf')
        min_tour_idx = -1
        node_to_assign = nodes[0]

        for idx, tour in enumerate(tours):
            current_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour)-1))
            proposed_cost = current_cost + distance_matrix[tour[-1]][node_to_assign] + distance_matrix[node_to_assign][0]

            if proposed_cost < min_cost:
                min_cost = proposed_cost
                min_tour_idx = idx

        tours[min_tour_idx].append(node_to_assign)
        nodes.pop(0)

    # Complete tours by returning to the depot
    for tour in tours:
        tour.insert(0, 0) # start at depot
        tour.append(0) # end at depot

    return tours

# Calculate tours
num_robots = 8
tours = initialize(num_robots, distance_matrix)

# Calculation of travel cost for each tour
def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

costs = [calculate_tour_cost(tour, distance_matrix) for tour in tours]
max_cost = max(costs)

# Output results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Maximum Travel Change Cost: {max_cost}")