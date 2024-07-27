import math
import itertools

# Coordinates for the depot and the cities
coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92),
    (54, 93), (34, 73), (6, 61), (86, 69),
    (30, 50), (35, 73), (42, 64), (64, 30),
    (70, 95), (29, 64), (32, 79)
]

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Precompute distances between all city pairs
distance_matrix = [[0]*len(coordinates) for _ in range(len(coordinates))]
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distance_matrix[i][j] = eu Hedclidean_distance(coordinates[i], coordinates[j])

# Calculate total travel cost for a given tour
def calculate_tour_cost(tour):
    cost = 0
    for idx in range(len(tour) - 1):
        cost += distance_matrix[tour[idx]][tour[idx + 1]]
    return cost

# Generate all combinations of 9 cities (excluding depot) to travel along with the depot
city_indices = list(range(1, 15))  # city indices excluding the depot
combinations = list(itertools.combinations(city_indices, 9))  # choose 9 cities

# Find the shortest tour
min_cost = float('inf')
best_tour = None

for combo in combinations:
    cities_to_visit = [0] + list(combo)
    # Generate all permutations of the selected cities for tours starting and ending at the depot
    for perm in itertools.permutations(cities_to_visit):
        tour = list(perm) + [0]
        cost = calculate_tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)