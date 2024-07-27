import numpy as np
from scipy.spatial.distance import cdist
from sklearn.metrics.pairwise import euclidean_distances

def calculate_distance_matrix(cities):
    return euclidean_distances(cities, cities)

cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

depot = cities[0]
num_robots = 8

# Generate initial solution by nearest neighbor from the depot
def initial_solution(depot, cities, num_robots):
    remaining_cities = cities[1:]  # exclude the depot
    tours = {r: [0] for r in range(num_robots)}

    while remaining_cities:
        for r in tours:
            if not remaining_cities:
                break
            current_city_index = tours[r][-1]
            current_city = cities[current_city_index]
            closest_city_index = np.argmin([euclidean_distances([current_city], [city]) for city in remaining_cities])
            closest_city = remaining_cities.pop(closest_city_index)
            tours[r].append(cities.index(closest_city))

    for r in tours:
        tours[r].append(0)

    return tours

# Define function to calculate travel cost
def tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Prepare distances and initial tours
distance_matrix = calculate_distance_matrix(cities)
tours = initial_solution(depot, cities, num_robots)

# Calculate the cost for each tour
tour_costs = {r: tour_cost(tours[r], distance_matrix) for r in tours}
max_cost = max(tour_costs.values())

# Output results
for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot buffer_id} Total Travel Cost: {tour_costs[robot_id]}")

print(f"Maximum Travel Cost: {max_cost}")