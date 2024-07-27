import math
from itertools import product, permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

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

# Groups of cities
groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Generate all possible selections of cities, one from each group
def generate_possible_combinations(groups):
    group_lists = [groups[key] for key in sorted(groups.keys())]  
    return product(*group_lists)

# Calculate total travel cost for a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_function(cities[tour[i]], cities[tour[i+1]])
    return cost

# Find the shortest tour
def find_shortest_tour(groups):
    best_tour = None
    min_cost = float('inf')
    
    for combination in generate_possible_combinations(groups):
        tour = [0] + list(combination) + [0]
        cost = calculate_total_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
            
    return best_tour, min_cost

# Main execution to find the optimal tour and its cost
shortest_tour, total_cost = find_shortest_tour(groups)

# Output results
print(f"Tour: {shortest_tour}")
print(f"Total travel cost: {total_cost:.2f}")