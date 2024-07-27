import math
import itertools

# Coordinates of the cities (index corresponds to city number)
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

# Grouping of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute all-pairs distances
dist_matrix = [[distance(i, j) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Function to calculate the total distance of a tour
def tour_distance(tour):
    return sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Find the optimal cities to represent the groups
group_representative = []

# Select the best city in each group
for group in groups:
    # Add the depot and measure the circuit for choosing the city
    potential_tours = [[0] + list(permutation) + [0] for permutation in itertools.permutations(group)]
    best_tour = min(potential_tours, key=tour_distance)
    # Choose the optimal city from this group
    best_city = best_tour[1]
    group_representative.append(best_city)

# Now include depot and find the smallest tour
complete_tour = [0] + group_representative + [0]

# Evaluate all permutations of the representative cities to find the minimum tour
min_tour = None
min_cost = float('inf')

for perm in itertools.permutations(group_representative):
    current_tour = [0] + list(perm) + [0]
    current_cost = tour_distance(current_tour)
    if current_cost < min_cost:
        min_cost = current_cost
        min_tour = current_tour

# Print the best tour and the total cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost:.2f}")