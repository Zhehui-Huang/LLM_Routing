import math
import itertools

# Coordinates of the cities
cities = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Calculate Euclidean distance
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create distance matrix
distance_matrix = [[calc_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Number of cities to visit including the depot
k = 10

best_tour = None
min_cost = float('inf')

# Generate all combinations of 9 cities plus the depot city (at index 0)
for cities_combination in itertools.combinations(range(1, len(cities)), k - 1):
    current_combination = [0] + list(cities_combination)
    
    # Generate all permutations of the selected cities starting from the depot
    for perm in itertools.permutations(current_combination[1:]):
        tour = [0] + list(perm) + [0]
        
        # Calculate the cost of this tour
        cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        
        # Check if this tour has a lower cost than the current best
        if cost < min_cost:
            best_tour = tour
            min_cost = cost

# Display results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)