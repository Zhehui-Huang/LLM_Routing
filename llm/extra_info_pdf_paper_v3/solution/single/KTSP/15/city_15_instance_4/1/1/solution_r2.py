import itertools
import math
from sys import maxsize

# Coordinates of each city, including the starting city
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate the total distance of a tour
def total_distance(tour):
    return sum(distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# Generate the best tour using permutations of selected city indexes
def find_best_tour():
    min_cost = maxsize
    best_tour = []
    
    # Generate combinations of 11 cities (excluding the start city index 0)
    for city_combination in itertools.combinations(range(1, 15), 11):
        city_subset = [0] + list(city_combination) + [0]  # Add depot to start and end

        # Generate permutations of the city subset
        for perm in itertools.permutations(city_subset[1:-1]):
            current_tour = [0] + list(perm) + [0]
            cost = total_distance(current_tour)
            if cost < min_cost:
                min_cost = cost
                best_tour = current_tour

    return best_tour, min_cost

# Compute the best tour and its cost
best_tour, min_cost = find_best_tour()

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")