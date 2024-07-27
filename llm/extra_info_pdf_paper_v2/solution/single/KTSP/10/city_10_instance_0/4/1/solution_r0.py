from itertools import combinations, permutations
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return total_cost

def find_shortest_tour(cities_coordinates, k):
    depot = 0
    other_cities = list(range(1, len(cities_coordinates)))
    min_cost = float('inf')
    best_tour = []

    # Generate all combinations of k-1 other cities to visit
    for city_combination in combinations(other_cities, k - 1):
        # Generate all tours through these cities starting and ending at depot
        full_tour_cities = [depot] + list(city_combination)
        for perm in permutations(full_tour_cities):
            if perm[0] == depot:  # Ensure starting at the depot
                tour = list(perm) + [depot]  # Adding depot at the end to complete the loop
                cost = calculate_tour_cost(tour, cities_coordinates)
                if cost < min_cost:
                    min_cost = cost
                    best_tour = tour

    return best_tour, min_cost

# Input data
cities_coordinates = [
    (50, 42),  # City 0 - Depot
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

# Finding the shortest tour visiting exactly 4 cities including the depot
k = 4
best_tour, min_cost = find_shortest_tour(cities_coordinates, k)

# Output results
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))