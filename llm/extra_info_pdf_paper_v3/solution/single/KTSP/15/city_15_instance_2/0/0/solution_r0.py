import math
import itertools

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Coordinates of the cities indexed by their identifiers
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Creating a heuristic to determine a good combination of 7 additional cities to form a tour with the depot city
def compute_tours():
    best_tour = None
    min_cost = float('inf')
    
    for cities_subset in itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 7):
        complete_tour = [0] + list(cities_subset) + [0]
        permutations = itertools.permutations(complete_tour[1:-1])
        
        for permutation in permutations:
            tour = [0] + list(permutation) + [0]
            total_cost = 0
            
            for i in range(len(tour) - 1):
                total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
            
            if total_cost < min_cost:
                min_cost = total_cost
                best_tour = tour

    return best_tour, min_cost

# Find the optimal tour and the minimum travel cost
tour, total_cost = compute_tours()

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")