import numpy as np
from scipy.spatial import distance_matrix

# Define city coordinates including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance matrix
dist_matrix = distance_matrix(coordinates, coordinates)

# Assign cities to robots based on a simplistic strategy; more sophisticated algorithms could be used
assigned_cities = {i: [] for i in range(8)}
for city_id in range(8, len(coordinates)):
    assigned_cities[city_id % 8].append(city_id)

# Include depot start and end points for each robot
for robot_id in range(8):
    assigned_cities[robot_id].insert(0, robot

def compute_tsp_tour(cities):
    """ Solve TSP for the given cities using a nearest neighbour heuristic. """
    start_city = cities[0]
    path = [start_city]
    cost = 0
    unvisited = set(cities[1:-1])  # Exclude returning to depot (will be done manually later)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
        cost += dist_matrix[current_city, next_city]
        path.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    # Return to starting depot
    path.append(start_city)
    cost += dist_matrix[current_city, start_city]
    return path, cost

all_tours = {}
total_cost = 0

# Execute TSP for each robot and collect results
for robot_id in range(8):
    tour, tour_cost = compute_tsp_tour(assigned_cities[robot_id])
    all_tours[robot_id] = (tour, tour_cost)
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}\n")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")