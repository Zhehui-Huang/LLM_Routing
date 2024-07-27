import math
from itertools import combinations, permutations

# Define the cities with their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate all 3-city combinations from cities excluding the depot
city_combinations = combinations([i for i in cities if i != 0], 3)

min_cost = float('inf')
optimal_tour = []

# Check each combination of cities
for combination in city_combinations:
    # Create the full tour by re-adding the depot city
    full_tour = [0] + list(combination) + [0]
    
    # Generate all permutations of the selected cities
    for tour in permutations(combination):
        # Create tour starting and ending at depot
        trial_tour = [0] + list(tour) + [0]
        
        # Calculate total cost of this tour
        tour_cost = sum(calculate_distance(trial_tour[i], trial_tour[i+1]) for i in range(len(trial_tour) - 1))
        
        # Update the minimal cost and optimal tour
        if tour_cost < min_cost:
            min_cost = tour_cost
            optimal_tour = trial_tour

# Output the optimal tour and its cost
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_cost:.2f}")