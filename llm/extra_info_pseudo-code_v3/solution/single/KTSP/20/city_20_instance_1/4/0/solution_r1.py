import numpy as np
from itertools import permutations, combinations

# Given city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 
    14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45), 
    18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all combinations of cities excluding the start city and calculate tour cost
def find_best_tour(k=7):
    best_tour = None
    min_cost = float('inf')
    for combination in combinations(cities.keys() - {0}, k-1):  # Exclude depot, get combinations of k-1
        # Test each permutation of the cities in combination
        for perm in permutations(combination):
            tour = [0] + list(perm) + [0]  # Forming a tour back to the depot
            cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            if cost < min_cost:
                min_cost = cost
                best_tour = tour
    return best_tour, min_cost

# Finding the optimal tour with the given constraint of cities
optimal_tour, optimal_cost = find_best_tour()

# Print the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")