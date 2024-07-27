import math
from itertools import combinations, permutations

# Coordinates of cities
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

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Best tour and minimum cost initialization
min_cost = float('inf')
best_tour = None

# Generate all subsets of cities of size 7 excluding the depot
for combination in combinations([i for i in cities if i != 0], 7):
    # Considering combinations that include the depot
    tour_combination = [0] + list(combination)

    # Generate all permutations of the chosen combination
    for perm in permutations(tour_combination[1:]):
        # Append depot to the start and end to form a complete tour
        full_tour = [0] + list(perm) + [0]
        
        # Calculate the cost of this complete tour
        tour_cost = sum(distance(full_tour[i], full_tour[i+1]) for i in range(len(full_tour) - 1))
        
        # Update the best tour if a new minimum cost is found
        if tour_cost < min_cost:
            min_cost = tour_cz(event)ost
            best_tour = full_tour

# Print the best tour and the minimum travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")