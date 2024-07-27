import numpy as np
from scipy.spatial import distance_matrix

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Compute distance matrix
distances = distance_matrix(coordinates, coordinates)

# Number of robots (4) and their starting depot (All robots start at city 0)
robots = 4
depot = 0

# Greedily allocate cities to tours
def nearest_neighbor_tour(start_point, cities, distances):
    tour = [start_point]
    current_city = start_point
    remaining_cities = set(cities)
    remaining_cities.remove(start_point)

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distances[current_city][x])
        tour.append(next_city)
        remaining_cities.remove(next_city)
        current_city = next_city

    return tour

# Generating tours for each robot
cities_per_robot = len(coordinates[1:]) // robots  # exclude the depot initially for simplicity
tours = []
start_index = 1

for i in range(robots):
    end_index = start_index + cities_per_robot if i < robots - 1 else len(coordinates)
    tour = nearest_neighbor_tour(depot, range(start_index, end_index), distances)
    tours.append(tour)
    start_index = end_index

# Calculate the travel costs and the output
overall_cost = 0
for i, tour in enumerate(tours):
    tour_cost = sum(distances[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
    tour.append(depot)  # appending depot at the end to complete the tour
    tour_cost += distances[tour[-2]][depot]  # cost from the last city back to the depot
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {round(tour_cost)}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {round(overall_cost)}")