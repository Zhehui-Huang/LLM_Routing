import math
from typing import List, Tuple

# Define the city coordinates excluding the depot
city_coords = [
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

# Define the number of robots
num_robots = 4

# Distance function based on Euclidean distance
def calculate_distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def variable_neighborhood_search(num_robots: int, city_coords: List[Tuple[int, int]]) -> Tuple[List[List[int]], List[float]]:
    # Cluster cities into groups (naive clustering based on order for simplification)
    n = len(city_coords)
    cluster_size = n // num_robots
    clusters = [city_coords[i * cluster_size:(i + 1) * cluster_size] for i in range(num_robots)]
    
    # Assign the extra cities (if any)
    extra_cities = n % num_robots
    for i in range(extra_cities):
        clusters[i].append(city_coords[num_robots * cluster_size + i])

    tours = []
    tour_costs = []

    depot = (145, 215)  # Depot coordinates
    for cluster in clusters:
        tour = [0]  # Start tour at depot which is city index 0
        current_location = depot
        total_cost = 0.0

        # Create a simple tour by visiting cities in the current cluster in the given order
        for city in cluster:
            next_city_index = city_coords.index(city) + 1  # city index is offset by 1 because depot is index 0
            tour.append(next_city_index)
            distance = calculate_distance(current_location, city)
            total_cost += distance
            current_location = city

        # Return to the depot
        return_distance = calculate_distance(current_location, depot)
        total_cost += return_distance
        tour.append(0)  # end at depot

        tours.append(tour)
        tour_costs.append(total_cost)

    return tours, tour_costs

# Apply the variable neighborhood search heuristic
tours, tour_costs = variable_neighborhood_search(num_robots, city_coords)

# Print the outputs
max_travel_cost = max(tour_costs)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Maximum Travel Cost: {max_travel depends on the total of the most numberist]}")