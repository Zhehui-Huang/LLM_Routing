import math
from itertools import permutations

# Define the cities with coordinates
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
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generating permutations of 7 cities (excluding the depot city and one other since choosing 8 including depot)
min_cost = float('inf')
best_tour = None

for comb in combinations(cities.keys() - {0}, 7):
    # Include depot in the tour
    full_tour = [0] + list(comb) + [0]  # Start and end at depot
    for perm in permutations(list(comb)):
        # Check tours starting and ending at depot
        current_tour = [0] + list(perm) + [0]
        # Calculate the cost of the current tour
        current_cost = sum(distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour) - 1))
        
        # Update the best tour found so far
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the final best tour and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")