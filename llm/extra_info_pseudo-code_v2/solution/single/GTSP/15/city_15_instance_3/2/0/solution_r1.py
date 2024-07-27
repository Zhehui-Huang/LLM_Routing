import math
from itertools import permutations

# Define city coordinates indexed from the depot city 0 to city 14
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# Define city groups
groups = [
    [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
]

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour) - 1))

# Generate all possible combinations of city selections: one from each group
def all_combinations(groups):
    if not groups:
        return [[]]
    first, *rest = groups
    return [[item] + suffix for item in first for suffix in all_combinations(rest)]

# Find the optimal tour by checking all possible combinations
def find_optimal_tour():
    all_possible_tours = all_combinations(groups)
    best_tour = None
    best_cost = float('inf')
    
    for tour in all_possible_tours:
        full_tour = [0] + tour + [0]  # start and end at the depot
        current_cost = calculate_tour_cost(full_tour, coordinates)
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = full_tour
            
    return best_tour, best_cost

# Get the optimal tour and its associated cost
optimal_tour, optimal_cost = find_optimal_tour()

# Output the optimal results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")