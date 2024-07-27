from itertools import product
import math

# Define the cities coordinates
cities_coordinates = {
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

# Define groups of cities
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all permutations of city groups
all_permutations = list(product(*city_groups))

# Function to calculate total tour cost
def calculate_tour_cost(tour):
    total_cost = 0
    # Start at depot
    current_city = 0
    # Add return to depot
    tour = [0] + list(tour) + [0]
    # Calculate the distance
    for next_city in tour:
        total_cost += distance(current_city, next_city)
        current_city = next_city
    return total_cost

# Find the minimum tour cost and the corresponding permutation
min_cost = float('inf')
optimal_tour = None

for permutation in all_permutations:
    cost = calculate_tour_cost(permutation)
    if cost < min_cost:
        min_cost = cost
        optimal_tour = permutation

# Output results
tour_output = f'Tour: {[0] + list(optimal_tour) + [0]}'
cost_output = f'Total travel cost: {min_cost}'

print(tour_output)
print(cost_output)