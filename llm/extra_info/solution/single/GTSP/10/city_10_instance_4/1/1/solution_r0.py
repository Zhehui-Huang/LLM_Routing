import itertools
import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# City groups
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Compute distances between all pairs of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = [[0]*len(cities) for _ in range(len(cities))]
for i in range(len(cities)):
    for j in range(len(cities)):
        distances[i][j] = euclidean_distance(cities[i], cities[j])

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour):
    total_distance = 0
    for k in range(len(tour) - 1):
        total_distance += distances[tour[k]][tour[k+1]]
    return total_distance

# Explore all combinations
min_distance = float('inf')
best_tour = []

for combination in itertools.product(*groups):
    # Adding the depot to the start and end of the tour
    current_tour = [0] + list(combination) + [0]
    current_distance = calculate_tour_cost(current_tour)
    if current_distance < min_distance:
        min_distance = current_distance
        best_tour = current_tour

# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance}")