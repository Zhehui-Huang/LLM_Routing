import itertools
import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities to visit (including the depot)
k = 5

# All cities indices except the depot
city_indices = list(cities.keys())[1:]

# Generate all combinations of k-1 cities (as the depot is constant)
combinations = itertools.combinations(city_indices, k-1)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_distance

# Initialize minimum distance high enough
min_distance = float('inf')
best_tour = None

# Check each combination by completing the tour
for comb in combinations:
    # Creating a tour starting and ending at the depot
    tour = [0] + list(comb) + [0]
    # Compute its distance
    distance = calculate_total_distance(tour)
    # Check if this tour is the shortest found so far
    if distance < min_distance:
        min_distance = distance
        best_tour = tour

# Output results
print("Tour:", best_tour)
print("Total travel cost:", round(min_distance, 2))