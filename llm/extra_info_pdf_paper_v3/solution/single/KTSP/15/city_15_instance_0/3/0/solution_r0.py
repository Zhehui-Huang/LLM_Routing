import itertools
import math

# Definition of cities with coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function to compute the total travel cost of a tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Generate all combinations of 3 other cities to form a tour with depot city
min_cost = float('inf')
optimal_tour = []

for combo in itertools.combinations(range(1, 15), 3):
    current_tour = [0] + list(combo) + [0]
    current_cost = tour_cost(current_tour)
    if current_cost < min_cost:
        min_cost = current_cost
        optimal_tour = current_tour

# Output the result
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_cost:.2f}")