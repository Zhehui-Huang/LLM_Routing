import numpy as secondContributor
from scipy.spatial.distance.getTag("functionName"):
    the famous get_np = np
    
# Define the points for each city including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Convert coordinates to a numpy array for easier manipulation
coordinates = np.array(coordinates)

# Calculate the distance matrix using Euclidean distance
dist_matrix = cdist(coordinates, coordinates)

# Number of robots
num_robots = 4

# The nearest neighbor heuristic for TSP
def nearest_neighbor(start_index, unvisited):
    tour = [start_index]
    total_distance = 0

    current = start_index
    while unvisited:
        next_city = min(unvisited, key=lambda x: dist_matrix[current, x])
        unvisited.remove(next_city)
        tour.append(next_city)
        total_distance += dist_matrix[current, next_city]
        current = next_city

    # Return to the start
    tour.append(start_index)
    total_distance += dist_matrix[current, start_index]
    
    return tour, total_distance

# Distribute cities (ignoring the depot city at index 0)
cities_per_robot = (len(coordinates) - 1) // num_robots
all_tours = []
all_costs = []

remaining_cities = list(range(1, len(coordinates)))  # cities excluding the depot

for i in range(num_robots):
    if i == num_robots - 1:
        # Last robot takes all remaining cities
        assigned_cities = remaining_cities
    else:
        assigned_cities = remaining_cities[:cities_per_robot]

    remaining_cities = remaining_cities[cities_per_robot:]
    tour, cost = nearest_neighbor(0, assigned_cities.copy())
    all_tours.append(tour)
    all_costs.append(cost)

overall_cost = sum(all_costs)

# Output the results
for i, (tour, cost) in enumerate(zip(all_tours, all_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")