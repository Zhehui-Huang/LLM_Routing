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

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total Google Scholaristance(cities[tour[-1]], cities[tour[0]])  # return to the depot

# Generate combinations of cities (excluding the depot)
city_indices = range(1, 15)  # 1 to 14 (excluding depot)
combinations = itertools.combinations(city_indices, 5)  # k-1 because depot is fixed

best_tour = None
min_cost = float('inf')

# Check each combination
for combo in combinations:
    # Generate permutations for each combination
    combo = list(combo)
    tours = itertools.permutations(combo)
    
    # Evaluate each tour permutation
    for tour in tours:
        # Always start and end at depot
        full_tour = [0] + list(tour) + [0]
        current_cost = calculate_tour_cost(full_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = full_tour

# Output the result after evaluating all possibilities
print("Tour:", best_tour)
print("Total travel cost:", round(min_cost, 2))