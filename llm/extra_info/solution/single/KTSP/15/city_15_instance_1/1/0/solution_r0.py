import itertools
import math

# Define coordinates of cities including the depot
cities = [
    (29, 51),  # Depot 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_b][0] - cities[city_a][0]) ** 2 + (cities[city_b][1] - cities[city_a][1]) ** 2)

# Function to compute the travel cost of a tour
def tour_cost(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance(tour[i], tour[i + 1])
    return total_distance

# Brute force solution to find the shortest tour visiting exactly 6 cities
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = []

    for cities_combination in itertools.combinations(range(1, 15), 5):
        cities_tour = [0, *cities_combination, 0]  # Include the depot city
        for perm in itertools.permutations(cities_combination):
            current_tour = [0, *perm, 0]
            current_cost = tour_cost(current_tour)
            if current_cost < min_cost:
                min_cost = current_cost
                best_tour = current_tour

    return best_tour, min_cost

# Find and display the optimal tour and the total travel cost
optimal_tour, optimal_cost = find_shortest_tour()
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)