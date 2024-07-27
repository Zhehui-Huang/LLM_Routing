import math
from itertools import permutations

# Positions of cities (index corresponds to city number)
cities = [
    (54, 87), # Depot city 0
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# This function calculates the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Find the shortest path visiting exactly k=8 cities including the depot
def find_min_k_tsp(cities, k):
    def tour_cost(tour):
        return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    
    min_cost = float('inf')
    min_tour = None

    # Permute all combinations of 7 cities from the total list excluding the depot city
    for city_comb in permutations(range(1, len(cities)), k-1):
        # Consider only combinations of exactly 7 cities, making total 8 including the depot
        if len(set(city_comb)) == k - 1:
            city_tour = [0] + list(city_comb) + [0]
            cost = tour_cost(city_tour)
            if cost < min_cost:
                min_cost = cost
                min_tour = city_tour
    return min_tour, min_cost

# Number of cities to include in the tour including the depot (8 in this case)
k = 8
best_tour, best_cost = find_min_k_tsp(cities, k)

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")