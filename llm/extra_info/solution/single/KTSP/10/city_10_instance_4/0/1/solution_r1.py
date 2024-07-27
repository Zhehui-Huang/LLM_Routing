import math
import itertools

# City coordinates indexed from 0 to 9
coordinates = [
    (79, 15),   # City 0 - Depot
    (79, 55),   # City 1
    (4, 80),    # City 2
    (65, 26),   # City 3
    (92, 9),    # City 4
    (83, 61),   # City 5
    (22, 21),   # City 6
    (97, 70),   # City 7
    (20, 99),   # City 8
    (66, 62)    # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Precompute distances between every pair of cities
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(10)] for i in range(10)]

# Function to calculate total travel cost of a tour
def tour_cost(tour):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Generate all 7-city combinations involving the depot city
combinations = itertools.combinations(range(1, 10), 7)  # 9 cities (excluding depot), choose 7

best_tour = None
min_cost = float('inf')

# Search for the shortest tour
for cities in combinations:
    cities = (0,) + cities  # Include the depot city
    # Generate permutations of the seven cities and add depot at the start/end for complete tour
    for perm in itertools.permutations(cities[1:]):
        tour = (0,) + perm + (0,)
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the best tour found and the minimal cost
print(f"Tour: {list(best_tour)}")
print(f"Total travel cost: {min_cost:.2f}")