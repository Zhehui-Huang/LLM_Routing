from math import sqrt
from itertools import permutations

# Cities coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    xa, ya = cities[city_a]
    xb, yb = cities[city_b]
    return sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

# Brute-force approach to find the optimal tour using permutations
def find_optimal_tour():
    city_indices = list(cities.keys())
    min_cost = float('inf')
    best_tour = []
    
    # Generate all permutations of the city indices (excluding the depot city)
    for perm in permutations(city_indices[1:]):
        # Adding depot city at the start and end of the tour
        tour = [0] + list(perm) + [0]
        
        # Calculate the total cost of this tour
        cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update the minimum cost and best tour if this tour has a lower cost
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Find the shortest tour and its cost
optimal_tour, total_cost = find_optimal_tour()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_cost}")