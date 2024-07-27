import itertools
import math

# Define city coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Calculate Euclidean distance between two city coordinates
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create a distance matrix for all pairs of cities
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Finds the shortest path using the permutations of subsets
def find_best_tour(cities_to_visit, num_cities=12):
    subset_best_tour = None
    subset_best_cost = float('inf')

    # Iterate over all city permutations generated from the 12 selected cities
    for subset in itertools.combinations(cities_to_visit, num_cities):
        # Ensure the depot city is in the subset
        if 0 not in subset:
            continue
        for perm in itertools.permutations(subset):
            if perm[0] != 0:  # Must start at the depot city
                continue
            # Calculate the total cost for this permutation
            cost = sum(distance_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
            cost += distance_matrix[perm[-1]][perm[0]]  # Return to the depot
            # Track the minimum cost tour
            if cost < subset_best_cost:
                subset_best_cost = cost
                subset_best_tour = list(perm) + [perm[0]]
    return subset_best_tour, subset_best_cost

best_tour, best_cost = find_best_tour(range(len(cities)))

# Printing results
print("Tour:", best_tour)
print("Total travel cost:", best_cost)