import numpy as np
from scipy.spatial import distance_matrix

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Calculate the distance matrix (Euclidean distances)
distances = distance_matrix(coordinates, coordinates)

# Constants
robots = 4
depot = 0

# Split all cities except depots for robots (assume robots start from the same depot here)
num_cities = len(coordinates)
cities_for_robots = list(range(1, num_eum_cities))  # Exclude the depot

# Distribute cities fairly among robots
def distribute_cities(cities, num_robots):
    avg = len(cities) / float(num_robots)
    result = []
    last = 0.0

    while last < len(cities):
        result.append(cities[int(last):int(last + avg)])
        last += avg

    return result

city_groups = distribute_cities(cities_for_robots, robots)

# Nearest neighbor tour with city group assignment
def nearest_neighbor_tour(start_point, possible_cities, distances):
    tour = [start_point]
    current_city = start_point
    remaining_cities = set(possible_cities)

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)

    return tour

# Compute all tours and costs
tours = []
total_cost = 0

for robot in range(robots):
    tour = nearest_neighbor_tour(depot, city_groups[robot], distances)
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    tours.append((tour, tour_cost))

# Output the results
for idx, (tour, tour_cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")