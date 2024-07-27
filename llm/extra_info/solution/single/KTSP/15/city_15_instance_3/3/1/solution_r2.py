import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def find_shortest_tour(start_city, cities, num_cities):
    all_cities = list(range(len(cities)))
    min_cost = float('inf')
    best_tour = []

    for perm in permutations(all_cities[1:], num_cities - 1):  # Exclude the start city for permutation
        tour = [start_city] + list(perm)
        tour.append(start_city)  # Returning to the start city

        # Calculate total cost of the tour
        cost = 0
        for i in range(len(tour) - 1):
            cost += distance_matrix[tour[i]][tour[i + 1]]
        
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# City coordinates
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
          (6, 88), (86, 67), (30, 50), (35, 73), (42, 64), (64, 30), 
          (70, 92), (29, 64), (32, 79)]

# Calculate distances between all pairs of cities
distance_matrix = calculate_distances(cities)

# Determine the best tour that includes exactly 10 cities
tour, total_cost = find_shortest_tour(0, cities, 10)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_cost)