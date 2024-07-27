import itertools
import math

# Defining the cities and their coordinates
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

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of 7 cities (other than the depot)
city_combinations = itertools.combinations(range(1, 15), 7)

min_tour = None
min_cost = float('inf')

# Explore each combination
for combination in city_combinations:
    # Include the depot city at start and end
    current_cities = [0] + list(combination) + [0]
    
    # Check all permutations for this choice of 8 cities
    for perm in itertools.permutations(current_cities[1:-1]):
        tour = [0] + list(perm) + [0]
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

# Printing the result
print("Tour:", min_tour)
print("Total travel cost:", min_cost)