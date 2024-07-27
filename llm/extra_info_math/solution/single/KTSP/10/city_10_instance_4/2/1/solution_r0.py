from itertools import combinations
from scipy.spatial.distance import euclidean
from math import inf

# Cities Information
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

# Calculate all possible combinations of 7 cities out of 9 (excluding depot 0)
combinations_of_cities = list(combinations([i for i in range(1, 10)], 7))

# Function to calculate total distance of a tour
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean(cities[tour[i]], cities[tour[i+1]])
    return cost

# Find the shortest tour including the depot
min_cost = inf
best_tour = None

for subset in combinations_of_cities:
    # Create a list of cities including the depot
    current_cities = [0] + list(subset)
    
    # Check all permutations of the current subset for shortest tour
    for perm in itertools.permutations(current_cities[1:]):
        tour = [0] + list(perm) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the result
if best_tour:
    print(f"Tour: {best_tour}")
    print(f"Total travel cost: {min_cost:.2f}")
else:
    print("No valid tour found.")