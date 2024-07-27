import itertools
import math

# City coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Find all possible city combinations of size 3
comb = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

# Variables to hold the minimum cost and best tour path found
min_cost = float('inf')
best_tour = None

# Explore all combinations
for cities_subset in comb:
    # Create template tour starting and ending at the depot with three selected cities
    potential_tours = itertools.permutation(cities_subset)
    
    for tour in potential_tours:
        # Create a path starting and ending at the depot
        current_tour = [0] + list(tour) + [0]
        
        # Calculate the total travel cost for this tour
        cost = 0
        for i in range(len(current_tour) - 1):
            cost += distance(current_tour[i], current_tour[i + 1])
        
        # Update minimum cost and tour path if this tour has a lower cost
        if cost < min_cost:
            min_cost = cost
            best_tour = current_tour

# Output the best tour and the minimal cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")