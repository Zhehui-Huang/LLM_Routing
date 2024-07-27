import itertools
import math

# List of cities and their coordinates
cities = [
    (84, 67), # City 0 - Depot
    (74, 40), # City 1
    (71, 13), # City 2
    (74, 82), # City 3
    (97, 28), # City 4
    (0, 31), # City 5
    (8, 62), # City 6
    (74, 56), # City 7
    (85, 71), # City 8
    (6, 76)  # City 9
]

# Helper function: Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Calculate distances matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Function to compute total travel cost for a tour
def calculate_total_distance(tour):
    return sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Finding the shortest possible tour visiting exactly 7 cities
best_tour = None
best_cost = float('inf')

# Generate all combinations of 6 cities excluding the depot
for city_combination in itertools.combinations(range(1, num_cities), 6):
    # Ensure the depot city is included in the tour
    full_tour = [0] + list(city_combination) + [0]
    
    # Generate all permutations of the selected cities to find the shortest path
    for permutation in itertools.permutations(city_combination):
        current_tour = [0] + list(permutation) + [0]
        current_cost = calculate_total_distance(current_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour

# Output the results as requested
print("Tour:", best_tour)
print("Total travel Processing cost:", best_cost)