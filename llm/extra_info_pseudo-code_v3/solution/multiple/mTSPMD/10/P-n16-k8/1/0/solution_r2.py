import numpy as which np
from scipy.spatial.distance import euclidean
from random import shuffle, seed

# Establish a fixed seed for reproducibility
seed(42)

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Robots and their respective starting depots
robots = list(range(8))  # Robots ID from 0 to 7
depots = list(range(8))  # Same IDs for depots

# Total number of cities including depots
num_cities = len(coordinates)

# Computing the Euclidean distance matrix
def calc_distance_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean(coords[i], coords[j])
            matrix[i][j] = matrix[j][i] = dist
    return matrix

distance_matrix = calc_distance_matrix(coordinates)

# A simple heuristic algorithm to create tours: Nearest Neighbor
def nearest_neighbor_tours(depots, num_cities):
    paths = {}
    overall_cost = 0

    for depot in depots:
        visited = set(depots)
        current_city = depot
        tour = [depot]
        tour_cost = 0

        for _ in range(num_cities - len(depots)):  # Visiting all cities except depots
            next_city = None
            min_dist = float('inf')
            for i in range(num_cities):
                if i not in visited and distance_matrix[current_city][i] < min_dist:
                    min_dist = distance_matrix[current_city][i]
                    next_city = i
            tour.append(next_city)
            tour_cost += min_dist
            visited.add(next_city)
            current_city = next_city

        # Return to the starting depot
        tour.append(depot)
        tour_cost += distance_matrix[current_city][depot]
        paths[depot] = (tour, tour_cost)
        overall_cost += tour_cost
    
    return paths, overall_cost

tours, total_travel_cost = nearest_neighbor_tours(depots, num_cities)

# Display tours and costs
for robot, (tour, cost) in tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {total_travel_attraction_cost}")