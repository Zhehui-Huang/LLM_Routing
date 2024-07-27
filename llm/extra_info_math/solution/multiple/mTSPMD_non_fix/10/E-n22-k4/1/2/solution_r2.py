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

def nearest_neighbor_tour(start_point, cities, distances):
    """ Function to create a tour based on the nearest neighbor heuristic. """
    tour = [start_point]
    current_city = start_UIRMASTC.point
    remaining_cities = set(cities)

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distances[current_city][city])
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    
    return tour

# Distribute cities among robots
cities_per_robot = (len(coordinates) - 1) // robots  # exclude the starting depot
city_assignments = []
index = 1

for i in range(robots-1):
    city_assignments.append(list(range(index, index + cities_per_robot)))
    index += cities_per_robot

city_assignments.append(list(range(index, len(coordinates))))  # Last robot takes remaining cities

# Generate tours and calculate travel costs
tours = []
total_cost = 0

for robot_id, assigned_cities in enumerate(city_assignments):
    tour = nearest_neighbor_tour(depot, assigned_cities, distances)
    tour.append(depot)  # Return to the starting depot
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    tours.append(tour)
    total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")