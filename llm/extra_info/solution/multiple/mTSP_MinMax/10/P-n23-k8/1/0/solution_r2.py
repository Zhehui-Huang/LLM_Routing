import numpy as np
from scipy.spatial.distance import cdist

def calculate_distance(coord1, coord2):
    return np.linalg.norm(np.array(coord1) - np.array(coord2))

def nearest_neighbor_tour(start_city, cities, city_coordinates):
    tour = [start_city]
    unvisited = set(cities)
    unvisited.remove(start_city)
    
    current_city = start_city
    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(city_coordinates[current_city], city_coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city
        
    tour.append(start_city)  # Complete the loop by returning to the start
    return tour

def compute_tour_cost(tour, city_coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    return cost

# City Coordinates
city_coordinates = [
    (30, 40), # Depot
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35),
    (32, 39),
    (56, 37)
]

depot = 0
cities = list(range(1, len(city_coordinates)))  # excluding the depot

# Number of robots
num_robots = 8

# Segment cities into roughly equal partitions to distribute among the robots
np.random.shuffle(cities)  # Shuffle to randomize allocation
sliced_cities = np.array_split(cities, num_robots)

tours = []
costs = []

for idx, segment in enumerate(sliced_cities):
    tour = nearest_neighbor_tour(depot, segment.tolist() + [depot], city_coordinates)
    cost = compute_tour_cost(tour, city_coordinates)
    tours.append(tour)
    costs.append(cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

max_cost = max(costs)
print(f"Maximum Travel Cost among all tours: {max_cost:.2f}")