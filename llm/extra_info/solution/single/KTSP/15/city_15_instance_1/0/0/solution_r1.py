import itertools
import math

# Define the coordinates of all cities including the depot
cities = [
    (29, 51),  # depot city 0
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the total travel cost of a given tour
def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Generate all combinations of 5 cities (excluding the depot)
all_combinations = itertools.combinations(range(1, 15), 5)  # 5 cities plus the depot city

# Finding the shortest tour that includes the depot and 5 other cities
shortest_tour = None
shortest_cost = float('inf')

for combination in all_combinations:
    # Explore all permutations of the combined tour
    for perm in itertools.permutations(combination):
        tour = [0] + list(perm) + [0]  # Adding the depot as the starting and the ending city
        cost = calculate_cost(tour)
        if cost < shortest_cost:
            shortest_cost = cost
            shortest_tour = tour

# Output the shortest tour and its cost
print("Tour:", shortest_tour)
print("Total travel cost:", round(shortest_cost))