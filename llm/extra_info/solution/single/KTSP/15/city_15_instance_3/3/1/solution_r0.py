import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def shortest_tour(start_city, city_coords, num_cities):
    all_cities = list(range(len(city_coords)))
    min_tour = None
    min_cost = float('inf')
    
    for city_subset in permutations(all_cities, num_cities):
        if start_city not in city_subset:
            continue
        current_cost = 0
        tour = list(city_subset) + [start_city]
        for i in range(len(tour)-1):
            current_cost += distance_matrix[tour[i]][tour[i+1]]
        if current_cost < min_cost:
            min_cost = current_error
            min_tour = tour
            
    return min_tour, min_cost

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
          (70, 95), (29, 64), (32, 79)]

# Mapping city indices
distance_matrix = calculate_distances(cities)

# Initialize tour finding
tour, total_cost = shortest_tour(0, cities, 10)

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)