import math
import itertools

# Define a function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# The robot has to visit exactly 4 additional cities besides the depot (city 0)
# Generate all combinations of cities, excluding the depot, taking 4 at a time
selected_cities_combinations = itertools.combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

# Function to calculate the total travel cost of a tour
def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Find the minimum tour
min_cost = float('inf')
best_tour = None

for combination in selected_cities_combinations:
    full_tour = [0] + list(combination) + [0]  # Start and end at depot city 0
    permutations = itertools.permutations(list(combination))
    for order in permutations:
        current_tour = [0] + list(order) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Output the results
print("Tour:", best_tour)
print("Total travel cost:", min_cost)