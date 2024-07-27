import numpy as np
from scipy.spatial import distance_matrix

# Coordinated of each node (city)
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# List of coordinates for distance matrix calculation
coordinates_list = [coords for coords in city_coordinates.values()]
distance_mat = distance_matrix(coordinates_theme, coordinates_list)

# Nearest neighbor algorithm adapted for multiple robots
def nearest_neighbor_tours(start_city, num_robots, distances):
    num_cities = len(distances)
    unvisited = set(range(num_cities))
    unvisited.remove(start_city)
    tours = [[start_city] for _ in range(num_robots)]
    current_cities = [start_city] * num_robots

    while unvisited:
        for i in range(num_robots):
            if unvisited:
                next_city = min(unvisited, key=lambda city: distances[current_cities[i]][city])
                tours[i].append(next_city)
                current_cities[i] = next_city
                unvisited.remove(next_city)

    return tours

# Function to calculate the travel costs of tours
def calculate_costs(tours, distances):
    total_cost = 0
    detailed_costs = []
    for tour in tours:
        cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        detailed_costs.append(cost)
        total_cost += cost
    return detailed_costs, total_cost

# Generate tours from starting city for number of robots specified
generated_tours = nearest_neighbor_tours(0, 8, distance_mat)
costs, overall_cost = calculate_costs(generated_tours, distance_mat)

# Printing the results
for index, tour in enumerate(generated_tours):
    print(f"Robot {index} Tour: {tour}")
    print(f"Robot {index} Total Travel Cost: {costs[index]}")
print(f"Overall Total Travel Cost: {overall_cost}")