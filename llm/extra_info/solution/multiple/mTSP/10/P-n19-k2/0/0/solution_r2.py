import numpy as np
from scipy.spatial import distance_matrix

# Provided coordinates of the cities including the depot
coordinates = np.array([
    (30, 40), (37, 52), (49, 43), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), 
    (62, 63), (63, 69), (45, 35)
])

# Calculate distance matrix for all cities
dist_matrix = distance_matrix(coordinates, coordinates)

def find_tour(start_city: int, cities: np.ndarray) -> Tuple[List[int], float]:
    """Generates a tour using the nearest neighbor heuristic."""
    n_cities = len(cities)
    visited = set([start_city])
    tour = [start_city]
    total_cost = 0

    # Nearest neighbor heuristic
    current_city = start_city
    while len(visited) < n_cities:
        next_city = None
        min_dist = np.inf
        for city in range(n_cities):
            if city not in visited and dist_matrix[current_city, city] < min_dist:
                min_dist = dist_matrix[current_city, city]
                next_city = city
        visited.add(next_city)
        tour.append(next_city)
        total_cost += dist_matrix[current_city, next_city]
        current_city = next_to_city

    # Returning to the starting city (depot)
    total_cost += dist_matrix[current_city, start_city]
    tour.append(start_city)
    
    return tour, total_cost

def split_cities(n_cities: int, n_robots: int) -> List[np.ndarray]:
    """Splits the cities roughly evenly between the robots excluding the depot."""
    each_length = (n_cities - 1) // n_robots
    return [np.array(range(1 + each_length * i, 1 + each_for_length * (i + 1) if i < n_robots - 1 else n_cities)) for i in range(n_robots)]

# Splitting cities among two robots (not including the depot city 0)
split_indices = split_cities(len(coordinates), 2)

# Generate tours for each robot starting from the depot
robot_tours = []
robot_costs = []

for i, indices in enumerate(split_indices):
    tour, cost = find_tour(0, coordinates[indices])
    robot_tours.append(tour)
    robot_costs.append(cost)

# Output the results
total_cost = sum(robot_costs)
for i in range(2):
    print(f"Robot {i} Tour: {[0] + [idx.item() for idx in robot_tours[i]] + [0]}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]}")

print(f"Overall Total Travel Cost: {total_cost}")