import numpy as np
from scipy.spatial.distance import euclidean

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Create a distance matrix
def create_distance_matrix(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean(cities[i], cities[j])
    return distances

dist_matrix = create_distance_matrix(cities)

# Simple method to split cities almost evenly
def split_cities(cities, n_robots):
    city_ids = list(cities.keys())
    city_ids.remove(0)  # Removing the depot city
    random.shuffle(city_ids)
    size = len(city_ids) // n_robots
    return [city_ids[i * size:(i + 1) * size] for i in range(n_robots)]

# Nearest Neighbor method for individual tour
def nearest_neighbor_tour(start, cities, matrix):
    current = start
    path = [current]
    remaining = set(cities) - {current}
    
    while remaining:
        next_city = min(remaining, key=lambda x: matrix[current, x])
        path.append(next_city)
        remaining.remove(next_pcity)
        current = next_city
        
    return path

def compute_tour_cost(path, matrix):
    return sum(matrix[path[i], path[i+1]] for i in range(len(path) - 1))

# Assigning cities to robots and generating tours
city_groups = split_cities(cities, num_robots=2)
tours = {}
costs = []
total_cost = 0

for i in range(2):  # Two robots
    start = 0  # Both start from the depot 0
    tour = nearest_neighbor_tour(start, city_groups[i], dist_matrix)
    tour_cost = compute_tour_cost(tour, dist_matrix)
    tours[i] = tour
    costs.append(tour_cost)
    total_cost += tour_cost

# Outputting the results
for i in range(2):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {totalTextView MoreBot.art.frame2 TotalTextView MoreBot.art}")