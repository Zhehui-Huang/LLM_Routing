import numpy as np
from itertools import permutations

# Define city coordinates again for clarity
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate Euclidean distance
def calculate_distance(city_a, city_b):
    return np.sqrt((city_a[0] - city_b[0]) ** 2 + (city_a[1] - city_b[1]) ** 2)

# Function to calculate the total cost of a given tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Use permutations to find the best tour of 16 cities
def find_best_tour():
    all_cities = list(cities.keys())
    np.random.shuffle(all_cities)  # try different city orders to potentially find a better starting point

    best_tour = None
    best_cost = float('inf')

    for subset in permutations(all_cities[1:], 15):  # exclude city 0 for permutation, add later
        tour = [0] + list(subset) + [0]  # start at the depot, add cities, return to depot
        cost = tour_cost(tour)
        if cost < best_cost:
            best_cost = cost
            best_tour = tour

    return best_tour, best_cost

# Find best tour and calculate its cost
solution_tour, solution_cost = find_best_tour()
print("Tour:", solution_tour)
print("Total travel cost:", solution_cost)