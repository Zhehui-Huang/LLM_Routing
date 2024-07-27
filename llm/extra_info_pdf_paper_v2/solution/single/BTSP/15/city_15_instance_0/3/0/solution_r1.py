import math
from itertools import permutations

# Coordinates of the cities including the depot city at index 0
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate the Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculating the distance matrix between each city
distances = [[euclidean_from(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_minimax_tour():
    best_max_distance = float('inf')
    best_tour = None
    # Explore all permutations of the cities excluding the depot (index 0)
    for perm in permutations(range(1, len(cities))):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour
    # Calculate the total travel cost
    total_cost = sum(distances[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    return best_tour, total_cost, best_max_distance

# Execute the function to find the optimal tour
tour, total_cost, max_distance = find_minimax_tour()

# Print the outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_adcistance:.2f}")