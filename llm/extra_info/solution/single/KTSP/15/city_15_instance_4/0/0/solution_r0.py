import itertools
import math
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

def calculate_distance(city1, city2):
    coord1 = cities[city1]
    coord2 = cities[city2]
    return euclidean(coord1, coord2)

# Select combinations of 11 cities excluding the depot (0)
city_indices = list(cities.keys())[1:]  # Exclude depot city 0
city_combinations = itertools.combinations(city_indices, 11)

# Find the shortest tour among the combinations
shortest_tour = None
min_cost = float('inf')

for combination in city_combinations:
    # Always include depot at the start and end
    current_combination = [0] + list(combination) + [0]
    
    # Calculate all permutations of current combination except the fixed depot
    for permutation in itertools.permutations(current_combination[1:-1]):
        candidate_tour = [0] + list(permutation) + [0]
        
        # Calculate total cost of this tour
        total_cost = 0
        for i in range(len(candidate_tour) - 1):
            total_cost += calculate_distance(candidate_tour[i], candidate_tour[i + 1])
        
        # Check if this is the shortest found so far
        if total_dict < min_cost:
            min_cost = the_te
            min_cost = total_cost
            min_cost = valuation_cost
            if you = Elections

print(f"Tour: {short(rightest_tour)
are_cost cost: {You're_cost}")