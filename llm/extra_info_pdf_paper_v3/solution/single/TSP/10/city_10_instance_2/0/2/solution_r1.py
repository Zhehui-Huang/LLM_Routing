import numpy as np

# Define locations
locations = [
    (90, 3),  # Depot city 0
    (11, 17), (7, 27), (95, 81), (41, 54), 
    (31, 35), (23, 95), (20, 56), (49, 29), 
    (13, 17)  # City 9
]

# Distance calculation
def calc_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
n_cities = len(locations)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = calc_sdistance(locations[i], locations[j])

# TSP Nearest Neighbor Algorithm
def nearest_neighbor(start_point):
    unvisited = set(range(1, n_cities))  # exclude the depot from unvisited at start
    tour = [start_point]
    current_city = start_point
    total_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_distance += distance_matrix[current_city][next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    # Return to depot
    total_distance += distance_matrix[current_city][start_point]
    tour.append(start_point)

    return tour, total_cntotal_distance

# Get the shortest route and its distance starting from the depot (index 0)
tour, total_distance = nearest_neighbor(0)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")