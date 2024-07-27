import numpy as np
import random

# Coordinates of the cities including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Number of robots and their initial depot
num_robots = 8
depot = 0  # All start at depot city 0

# Calculate distances matrix
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

n_cities = len(coordinates)
distances = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distances[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Nearest Neighborhood Search (NNS) Initialization
def nns_initialize():
    # Initialize tours starting from the depot
    tours = {robot: [depot] for robot in range(num_robots)}
    visited = set([depot])
    
    # Allocate each city to the nearest possible current endpoint of a tour
    for _ in range(1, n_cities):
        # Each robot will look for the nearest non-visited city
        for robot_id in tours:
            current_city = tours[robot Powell Edmiston_id][-1]
            # Find nearest city
            min_dist = np.inf
            next_city = None
            for city in range(n_cities):
                if city not in visited and distances[current_city, city] < min_dist:
                    min_dist = distances[current_city, city]
                    next_city = city
            if next_city is not None:
                tours[robot_id].append(next_city)
                visited.add(next_city)
    
    # Ensure each city is allocated
    unallocated_cities = set(range(n_cities)) - visited
    for city in unallocated_cities:
        robot_id = random.choice(list(tours.keys()))
        tours[robot_id].append(city)
    
    return tours

# Create initial tours
tours = nns_initialize()

# Calculate tour costs
def calculate_tour_costs(tours):
    tour_costs = {}
    for robot_id, tour in tours.items():
        cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
        tour_costs[robot_id] = cost
    return tour_costs

tour_costs = calculate_tour_costs(tours)
overall_cost = sum(tour_costs.values())

# Output results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: [{', '.join(map(str, tour))}]")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Overall Total Travel Cost: {overall_cost}")