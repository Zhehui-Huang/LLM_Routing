import math
from itertools import combinations, permutations

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

def find_shortest_tour(start_city, cities, num_cities):
    subset_cities = [i for i in range(1, len(cities))]  # excluding the depot for combinations
    min_tour = []
    min_cost = float('inf')

    # Generate all possible combinations of (num_cities - 1) as the depot is fixed
    for subset in combinations(subset_cities, num_cities - 1):
        full_subset = [start_city] + list(subset)
        # Generate all permutations of the selected cities to ensure minimum tour is found
        for permutation in permutations(full_subset[1:]):
            # Creating a route starting and ending at the depot
            current_tour = [start_city] + list(permutation) + [start_city]
            # Calculate the cost of this tour
            current_cost = 0
            for i in range(len(current_tour) - 1):
                current_cost += distances[current_tour[i]][current_tour[i + 1]]

            # Update the minimum cost and tour if a cheaper tour is found
            if current_cost < min_cost:
                min_cost = current_cost
                min_tour = current_tour

    return min_tour, min_cost

# Coordinates of cities including the depot
cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), 
          (6, 61), (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), 
          (70, 92), (29, 64), (32, 79)]

distances = calculate_distances(cities)
tour, total_cost = find_shortest_tour(0, cities, 10)

# Output results
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))