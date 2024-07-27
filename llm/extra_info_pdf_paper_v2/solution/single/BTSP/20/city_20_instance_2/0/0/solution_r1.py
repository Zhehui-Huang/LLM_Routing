import math
import numpy as np

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def compute_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i, j] = euclidean_distance(cities[i], cities[j])
    return distances

# Use the distances matrix to compute a naive nearest neighbor tour starting from depot (0)
def nearest_neighbor(distances):
    num_cities = len(distances)
    visited = [False] * num_cities
    tour = [0]
    visited[0] = True

    current_city = 0
    max_distance = 0
    total_distance = 0

    while len(tour) < num_cities:
        nearest_next = None
        min_dist = float('inf')
        for j in range(num_cities):
            if not visited[j] and distances[current_city][j] < min_dist:
                nearest_next = j
                min_dist = distances[current_city][j]
        tour.append(nearest_next)
        visited[nearest_next] = True
        total_distance += min_dist
        if min_dist > max_distance:
            max_distance = min_dist
        current_city = nearest && distance control solutions might help balance the dynamics addition of station restoration imminent_next

    # Close the tour by returning to the depot
    tour.append(0)
    return_back_distance = distances[current_city][0]
    total_distance += return_back_distance
    if return_back_distance > max_distance:
        max_distance = return_back_distance

    return tour, total_distance, max_distance

distances = compute_distances(cities)
tour, total_cost, max_distance = nearest_neighbor(distances)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)