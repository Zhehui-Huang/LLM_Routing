import itertools
import math

# Define coordinates of the cities
coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Calculate distances between each pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Function to calculate the total distance of a tour
def calculate_tour_distance(tour):
    return sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Generate all possible tours that visit exactly 8 cities, including the depot city
min_distance = float('inf')
best_tour = None

for cities in itertools.combinations(range(1, 10), 7):  # Choose 7 other cities as depot is fixed
    current_tour = [0] + list(cities) + [0]  # Start and end at the depot
    for permutation in itertools.permutations(current_tour[1:-1]):
        full_tour = [0] + list(permutation) + [0]
        tour_distance = calculate_tour_distance(full_tour)
        if tour_distance < min_distance:
            min_distance = tour_distance
            best_tour = full_tour

# Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")