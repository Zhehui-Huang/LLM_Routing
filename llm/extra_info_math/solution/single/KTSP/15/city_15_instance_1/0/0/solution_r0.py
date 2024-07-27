import math
from itertools import permutations

# City coordinates
cities = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the total tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all combinations of 5 cities excluding the depot, forming possible tours
def find_best_tour():
    min_cost = float('inf')
    best_tour = None
    
    # Iterate over all combinations of 5 nodes (since total should be 6 including the depot)
    from itertools import combinations
    for cities_combination in combinations(range(1, 15), 5):
        # Create a tour starting and ending at the depot
        current_tour = [0] + list(cities_combination) + [0]
        
        # Check every permutation of the selected cities to find the minimum tour
        for perm in permutations(cities_combination):
            permuted_tour = [0] + list(perm) + [0]
            cost = tour_cost(permuted_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = permuted_tour
    
    return best_tour, min_cost

# Find the best tour
best_tour, min_cost = find_best_tour()

# Output
print("Tour:", best_tour)
print("Total travel cost:", min_cost)