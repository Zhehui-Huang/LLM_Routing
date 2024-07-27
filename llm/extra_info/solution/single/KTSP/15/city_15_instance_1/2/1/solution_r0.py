from itertools import combinations
import math

# Coordinates for the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute distances between every pair of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += distances[(tour[i], tour[i + 1])]
    return tour_cost

# Generate all possible tours that start and end at depot (city 0) and visits 5 other cities
def find_shortest_tour():
    min_cost = float('inf')
    best_tour = None
    for combination in combinations([i for i in range(1, 15)], 5):  # Choose 5 cities (excluding depot)
        tour = [0] + list(combination) + [0]  # Form a tour by appending the depot city
        tour_cost = calculate_tour_cost(tour)
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour
    return best_tour, min_cost

# Find the shortest tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output the tour and the total cost
print("Tour:", optimal_tour)
print("Total travel cost:", round(optimal_cost, 2))