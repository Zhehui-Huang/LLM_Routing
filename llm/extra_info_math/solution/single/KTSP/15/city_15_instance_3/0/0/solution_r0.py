from itertools import permutations
import math

# Given cities with coordinates including depot (city 0)
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), 
    (54, 93), (34, 73), (6, 61), (86, 69), 
    (30, 50), (35, 73), (42, 64), (64, 30), 
    (70, 95), (29, 64), (32, 79)
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Calculate the distance matrix
n = len(coordinates)
distance_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Subset includes depot city 0 and any 9 other cities
def find_shortest_tour():
    min_tour_length = float('inf')
    best_tour = []

    # Iterate over all subsets of size 10 including the depot city
    from itertools import combinations
    city_indices = range(1, n)  # excluding depot city in combinations, always include depot later.
    subsets = combinations(city_indices, 9)  # Choose 9 because depot is always in

    for subset in subsets:
        # We include the depot city '0' in the tour
        current_subset = [0] + list(subset)

        # Permute the subset to find the minimum tour within the subset that starts and end on the depot
        for permuted_subset in permutations(current_subset[1:]):
            tour = [0] + list(permuted_subset) + [0]
            tour_length = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            
            if tour_length < min_tour_length:
                min_tour_length = tour_length
                best_tour = tour

    return best_tour, min_tour_length

# Get the best tour and its cost
tour, total_cost = find_shortest_tour()

print("Tour:", tour)
print("Total travel cost:", total_cost)