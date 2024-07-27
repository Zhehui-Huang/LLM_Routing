import itertools
import math

# Coordinates of cities indexed from 0 to 9
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

# City groups containing indices from above
city_groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Generate all possible tours by visiting one city from each group
all_combinations = list(itertools.product(*city_groups))

# Calculate the total cost for a given sequence of cities starting and ending at depot city 0
def tour_cost(tour):
    total_cost = 0
    # Start at depot
    current_city = 0
    for city in tour:
        total_cost += distance(current_city, city)
        current_city = city
    # Return to depot
    total_cost += distance(current_city, 0)
    return total_cost

# Find the minimum cost tour
min_cost = float('inf')
best_tour = None

for combination in all_combinations:
    current_tour = [0] + list(combination) + [0]
    current_cost = tour_cost(combination)
    if current_cost < min_cost:
        min_cost = current_cost
        best_tour = current_tour

# Outputs the tour and total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")