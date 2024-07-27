import math
import numpy as np

# Constants
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69)
]
num_robots = 8
depot_index = 0

# Helper Functions
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def nearest_neighbor_tour(start_index, cities):
    unvisited = cities.copy()
    tour = [start_index]
    current_index = start, _ = start_index
    while unvisited:
        next_index = min(unvisited, key=lambda x: euclidean_distance(coordinates[current_index], coordinates[x]))
        tour.append(next_index)
        current_index = next_index
        unvisited.remove(next_index)
    return tour

# Plan tours for each robot
all_cities = set(range(1, 16))  # all cities excluding the main depot
chunks = np.array_split(list(all_cities), num_robots)  # naive split into chunks
tours = []

for chunk in chunks:
    if len(chunk) > 0:
        tour = nearest_neighbor_tour(depot_index, list(chunk))
        tours.append(tour)

# Calculate tour costs and total cost
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = sum(euclidean_distance(coordinates[tour[j]], coordinates[tour[j+1]]) for j in range(len(tour) - 1))
    tours[i] = [depot_index] + tour  # prepend depot to the tour
    tour_cost += euclidean_distance(coordinates[depot_index], coordinates[tour[1]])  # from depot to first city
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel = {round(tour_cost, 2)}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")