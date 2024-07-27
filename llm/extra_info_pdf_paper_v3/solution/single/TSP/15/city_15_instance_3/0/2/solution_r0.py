import math
from sympy.utilities.iterables import multiset_permutations

# Cities coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Calculate distances for all city pairs
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[frozenset([i, j])] = euclidean_distance(i, j)

# Simple TSP brute force solution, feasible due to small number of cities (15)
def find_best_tour():
    best_tour = None
    min_cost = float('inf')
    # All cities excluding the depot
    cities_to_visit = list(cities.keys())[1:]
    # Generate all permutations of city visits
    for permutation in multiset_permutations(cities_to_visit):
        cost = 0
        # Start at depot
        current_city = 0
        # Calculate the cost of the tour
        for city in permutation:
            cost += euclidean_distance(current_city, city)
            current_city = city
        # Return to depot
        cost += euclidean_distance(current_city, 0)
        if cost < min_cost:
            min_cost = cost
            best_tour = [0] + list(permutation) + [0]

    return best_tour, min_cost

# Find the best tour using the brute force approach
tour, total_cost = find_best_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")