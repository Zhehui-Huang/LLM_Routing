import itertools
import math

# Define city coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Define city groups
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Calculate distances between all pairs of cities
def calculate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

# Generate all permutations of city visits, one from each group
def all_possible_tours(groups):
    group_permutations = [list(itertools.product(*groups))]
    return itertools.product(*group_permutations)

# Calculate the tour cost
def calculate_tour_cost(tour, distance_matrix):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i]][tour[i + 1]]
    return total_cost

distance_matrix = calculate_distance_matrix(cities)

# Adding depot city to each group permutation
groups_with_depot = [[0] + group for group in groups]

min_cost = float('inf')
best_tour = None

# Find the best tour
for tour_perm in itertools.product(*groups_with_depot):
    complete_tour = [0] + list(tour_perm) + [0]  # start and end at the depot
    
    cost = calculate_tour_cost(complete_tour, distance_matrix)
    if cost < min_cost:
        min_cost = cost
        best_tour = complete_tour

# Produce the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")