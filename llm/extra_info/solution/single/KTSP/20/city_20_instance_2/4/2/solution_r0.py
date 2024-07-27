from itertools import combinations
import math

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88),
    11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41),
    16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Precompute distances
distances = {}
for i in cities:
    distances[i] = {}
    for j in cities:
        distances[i][j] = euclidean_distance(i, j)

# Helper function to calculate total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i + 1]]
    return cost

# Implementing a branch and bound approach to find minimum distance
def find_min_tour():
    min_cost = float('inf')
    best_tour = []
    
    # Combining the cities excluding the depot
    non_depot_cities = list(range(1, 20))
    for cities_subset in combinations(non_depot_cities, 9):  # We pick 9 as the depot city is always included
        # Form the tour beginning and ending at the depot
        current_tour = [0] + list(cities_subset) + [0]
        # Calculate the permutation of the chosen cities to find the minimal tour
        cities_permutations = it.permutations(cities_subset)
        for perm in cities_permutations:
            permuted_tour = [0] + list(perm) + [0]
            cost = tour_cost(permuted_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = permuted_tour
                
    return best_tour, min_cost

# Finding the tour and its cost
final_tour, final_cost = find_min_tour()

# Output the results
print("Tour:", final_tour)
print("Total travel cost:", final_cost)