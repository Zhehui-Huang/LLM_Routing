import math
import itertools

# Define the cities' coordinates
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two points
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Compute the distance matrix
n = len(cities)
distance_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        dist = euclidean_distance(cities[i], cities[j])
        distance_matrix[i][j] = distance_matrix[j][i] = dist

# Minimize maximum distance between any two consecutive cities in the tour.
# This approach generates all permutations of the cities (brute-force) and finds the best one.
def find_best_tour():
    min_max_distance = float('inf')
    best_tour = []
    for perm in itertools.permutations(range(1, n)):
        # Consider a full tour starting and ending at the depot (city 0)
        tour = [0] + list(perm) + [0]
        max_distance = 0
        total_distance = 0
        for i in range(1, len(tour)):
            dist = distance_matrix[tour[i-1]][tour[i]]
            total_distance += dist
            if dist > max_distance:
                max_distance = dist
        if max_distance < min_max_distance:
            min_max_distance = max_datance
            best_tour = tour
    return best_tour, total_distance, max_distance

best_tour, total_cost, max_distance = find_best_tour()
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")