import itertools
import math

# Coordinates of the depot and cities
cities = [
    (29, 51),  # Depot city 0
    (49, 20),  # City 1
    (79, 69),  # City 2
    (17, 20),  # City 3
    (18, 61),  # City 4
    (40, 57),  # City 5
    (57, 30),  # City 6
    (36, 12),  # City 7
    (93, 43),  # City 8
    (17, 36),  # City 9
    (4, 60),   # City 10
    (78, 82),  # City 11
    (83, 96),  # City 12
    (60, 50),  # City 13
    (98, 1)    # City 14
]

# Distance calculating function
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Tour cost calculation function
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

# Generate combinations of 5 cities (total 6 including depot)
city_indices = range(1, 15)  # Indices of the cities excluding the depot
combinations = itertools.combinations(city_indices, 5)  # Selecting 5 cities

best_tour = None
min_cost = float('inf')

# Evaluate each combination
for combo in combinations:
    # Permutate the selected cities' indices
    permutations = itertools.permutations(combo)
    for permutation in permutations:
        # Create a tour by including the depot at the start and the end
        tour = [0] + list(permutation) + [0]
        cost = calculate_tour_cost(tour)
        
        # Keep track of the minimum cost tour
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Display the best tour and the corresponding travel cost
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))