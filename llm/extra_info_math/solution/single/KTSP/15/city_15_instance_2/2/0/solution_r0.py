import itertools
import math
from sys import maxsize

# City coordinates where the index maps to the city number
cities = [
    (54, 87), # City 0: Depot
    (21, 84),
    (69, 84),
    (53, 40),
    (54, 42),
    (36, 30),
    (52, 82),
    (93, 44),
    (21, 78),
    (68, 14),
    (51, 28),
    (44, 79),
    (56, 58),
    (72, 43),
    (6, 99)
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Constants
k = 8  # Including the depot city

# Returns the total cost of the tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Find all combinations of (k-1) cities (excluding the depot city, which must be included and is city 0)
city_combinations = itertools.combinations(range(1, len(cities)), k - 1)

# Determine the shortest tour among all combinations
best_tour = None
min_cost = maxsize

for combo in city_combinations:
    # Generate permutations of visiting these cities
    for perm in itertools.permutations(combo):
        # Creating a tour which starts and ends at the depot
        current_tour = [0] + list(perm) + [0]
        current_cost = tour_cost(current_tour)
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour
            
# Output the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")