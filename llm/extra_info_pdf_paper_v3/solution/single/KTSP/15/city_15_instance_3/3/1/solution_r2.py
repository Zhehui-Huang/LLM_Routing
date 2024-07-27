import math
import itertools

# Define cities' coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Define function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Compute and store distances between each city pair
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Function to find the k-TSP tour
def find_tour():
    best_tour = None
    best_cost = float('inf')

    # Generate combinations (excluding the depot) of 9 cities to visit
    for subset in itertools.combinations(range(1, 15), 9):
        full_tour = [0] + list(subset) + [0]  # Add depot as start and end

        # Permute the internal cities to find the optimal path
        for permutation in itertools.permutations(subset):
            permuted_tour = [0] + list(permutation) + [0]
            tour_cost = sum(distances[(permuted_tour[i], permuted_tour[i + 1])] for i in range(len(permuted_tour) - 1))
            
            # If this permutation results in a lower cost, update best tour and cost
            if tour_cost < best_cost:
                best_cost = tour_cost
                best_tour = permuted_tour

    return best_tour, best_cost

# Calculate the optimal tour and its cost
optimal_tour, optimal_cost = find_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)