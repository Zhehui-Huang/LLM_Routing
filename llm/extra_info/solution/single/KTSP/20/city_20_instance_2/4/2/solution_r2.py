from itertools import permutations, combinations
import math

# City coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56),
    6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8), 10: (30, 88),
    11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 15: (64, 41),
    16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Euclidean distance function
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Precompute distances
distances = [[euclidean_dimstance(i, j) for j in range(20)] for i in range(20)]

# Compute the total distance of the tour
def total_distance(tour):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Find the shortest tour that starts and ends at the depot and visits exactly 10 cities
def find_shortest_tour():
    best_distance = float('inf')
    best_tour = None
    for subset in combinations(range(1, 20), 9):  # Generate combinations of 9 cities, excluding the depot
        for perm in permutations(subset):
            tour = [0] + list(perm) + [0]
            current_distance = total_distance(tour)
            if current_distance < best_distance:
                best_distance = current_distance
                best_tour = tour
    return best_tour, best_distance

# Execute the function to get the best tour and its distance
best_tour, best_distance = find_shortest_tour()

# Print results
print("Tour:", best_tour)
print("Total travel cost:", round(best_distance, 2))