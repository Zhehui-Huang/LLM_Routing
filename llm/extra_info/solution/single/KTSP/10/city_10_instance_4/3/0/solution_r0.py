import itertools
import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Generate all possible 7-city combinations including the depot
all_combinations = itertools.combinations(range(1, 10), 7)

# Find the minimum tour
min_cost = float('inf')
min_tour = None

for combination in all_combinations:
    full_tour = [0] + list(combination) + [0]
    
    # Generate all permutations of the cities in the combination
    for perm in itertools.permutations(full_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]
        
        # Calculate the total cost of the current_tour
        cost = sum(calculate_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        # Check if this is a new minimum
        if cost < min_cost:
            min_cost = cost
            min_tour = current_tour

# Output the results
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")