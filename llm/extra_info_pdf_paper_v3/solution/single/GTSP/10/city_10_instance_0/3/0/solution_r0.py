import itertools
import math

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates for each city indexed by city number
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Generate all combinations of tours
def optimal_tour(cities, groups):
    # Generate all possible combinations, each taking one city from each group
    all_group_combinations = itertools.product(groups[0], groups[1], groups[2])

    min_cost = float('inf')
    best_tour = []
    
    # Check each combination
    for comb in all_group_combinations:
        # Tour starts and ends at depot: city 0
        tour = [0] + list(comb) + [0]
        cost = 0
        
        # Calculate tour cost
        for i in range(len(tour) - 1):
            cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Update the best tour if current is better
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    
    return best_tour, min_cost

# Find the best tour and its cost
best_tour, min_cost = optimal_tour(cities, groups)

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")