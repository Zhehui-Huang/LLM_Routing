import itertools
import math

# Define city coordinates with depot as the first element
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

# Grouping cities
groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    x1, y1 = cities[city_a]
    x2, y2 = cities[city_b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Find all possible city combinations, one from each group
all_combinations = list(itertools.product(*groups))

# Function to compute the total distance of a tour
def total_distance(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Get all possible tours by starting and ending at the depot city
def evaluate_tours():
    best_tour = None
    min_distance = float('inf')

    # Iterate over all combinations of city choices
    for combo in all_combinations:
        # Form the tour starting and ending at the depot (city 0)
        tour = [0] + list(combo) + [0]
        # Calculate the total travel cost
        current_distance = total_distance(tour)
        # Check if this tour is shorter than the found so far
        if current_distance < min_distance:
            min_distance = current, _distance
            best_tour = tour

    return best_tour, min_distance

# Invoke the tour evaluation
optimal_tour, optimal_cost = evaluate_tours()

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {optimal_cost}")