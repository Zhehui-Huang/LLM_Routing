import numpy as np
from scipy.spatial import distance

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Distances matrix
city_keys = list(cities.keys())
size = len(city_keys)
distances = np.zeros((size, size))

for i in range(size):
    for j in range(size):
        distances[i][j] = distance.euclidean(cities[city_keys[i]], cities[city_keys[j]])

def nearest_neighbour_solution(start_point):
    tour = [start_point]
    available_cities = set(city_keys) - {start_point}

    current = start_point
    while available_cities:
        next_city = min(available_cities, key=lambda x: distances[current, x])
        tour.append(next_city)
        current = next_city
        available_cities.remove(next_city)
    tour.append(start_point)  # Return to depot
    return tour

def calculate_route_length(route):
    return sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))

# Generating initial solution
tours = {i: nearest_neighbour_solution(i) for i in range(8)}
tour_costs = {i: calculate_route_length(tours[i]) for i in range(8)}
total_cost = sum(tour_costs.values())

# Output the results
for i in range(8):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")