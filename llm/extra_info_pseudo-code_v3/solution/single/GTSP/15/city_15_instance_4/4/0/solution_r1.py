import itertools
import math

# Define city coordinates
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Define groups of cities
groups = [
    [3, 8],
    [4, 13],
    [1, 2],
    [6, 14],
    [5, 9],
    [7, 12],
    [10, 11]
]

# Calculates Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Generate all possible selections of one city from each group
def generate_possible_tours():
    return itertools.product(*groups)

# Calculate total distance of a given tour
def calculate_total_distance(tour):
    total_dist = distance(0, tour[0])  # From depot to first city
    for i in range(len(tour) - 1):
        total_dist += distance(tour[i], tour[i+1])
    total_after_return = total_dist + distance(tour[-1], 0)  # Return to the depot
    return total_after_return

# Find the shortest tour
def find_shortest_tour():
    min_distance = float('inf')
    best_tour = None
    for perm in generate_possible_tours():
        total_dist = calculate_total_distance(perm)
        if total_dist < min_distance:
            min_distance = total_dist
            best_tour = perm
    return best_tour, min_distance

# Running the function to find the optimal tour and its cost
optimal_tour, optimal_cost = find_shortest_tour()

# Output format:
print(f"Tour: [0, {', '.join(map(str, optimal_tour))}, 0]")
print(f"Total travel cost: {optimal_cost:.2f}")