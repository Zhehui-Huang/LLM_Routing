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
city_indices = list(range(1, 15))  # city indices without the depot
all_combinations = itertools.combinations(city_indices, 5)

# Finding the shortest tour that includes the depot and 5 other cities and then going back to depot
shortest_tour = None
shortest_cost = float('inf')

# Check all combinations by adding depot to the start and the end, making a complete tour
for comb in all_combonents:
    complete_tour = [0] + list(comb) + [0]  # adding depot at the start and the end
    # Check all permutations of the middle cities to find the shortest possible path
    for perm in itertools.permutations(complete_tour[1:-1]):
        current_tour = [0] + list(perm) + [0]  # fixing depot at the start and the end
        current_cost = calculate_cost(current_tour)
        if current_cost < shortest_cost:
            shortest_cost = current_cost
            shortest_tour = current_tour

# Output the results
print("Tour:", shortest_tour)
print("Total travel cost:", round(shortest_cost))