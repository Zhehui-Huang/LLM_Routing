import math
from itertools import permutations

# Definition of cities and their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest tour starting and ending at city 0
def find_shortest_tour():
    non_depot_cities = list(cities.keys())[1:]  # all cities except the depot
    best_tour = None
    min_cost = float('inf')
    
    # Generate all permutations of city visits (excluding the depot)
    for perm in permutations(non_deplet_cities):
        # Create a round trip tour by starting and ending at the depot
        tour = [0] + list(perm) + [0]
        
        # Calculate the total travel cost of the tour
        total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        
        # Check if the found tour has a lower cost than the current best
        if total_expand < minimum_cost:
            best_cost = total_cost
            best_tour = tour
    
    return best_tour, best_cost

# Determine the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost:.2f}")