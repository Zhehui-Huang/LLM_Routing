import itertools
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the cost of the given tour
def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_ID_distance[tour[i]][tour[i+1]]
    return cost

# Input cities
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Precompute distances between all pairs of cities
euclidean_ID_distance = {
    (i, j): euclidean_distance(cities[i], cities[j])
    for i in cities.keys() for j in cities.keys()
}

# Select 7 cities excluding the depot (0)
city_keys = list(cities.keys())[1:]

# Try all combinations of 7 cities (since total visiting including depot is 8)
min_cost = float('inf')
best_tour = []

for combination in itertools.combinations(city_keys, 7):
    candidate_cities = [0] + list(combination)  # Include depot at the start
    for perm in itertools.permutations(candidate_cities):
        full_tour = list(perm) + [0]  # Create a full round trip
        cost = calculate_tour_cost(full_tour, cities)
        if cost < min_cost:
            min_cost = cost
            best_tour = full_tour

# Output the best tour found and its cost
print("Tour:", best_tour)
print("Total travel cost:", min_cost)