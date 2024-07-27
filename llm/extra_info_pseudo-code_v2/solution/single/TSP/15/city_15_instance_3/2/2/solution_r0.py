import math
from itertools import permutations

# Define the cities and their coordinates
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible tours starting and ending at the depot city 0
def generate_tours():
    city_indices = list(cities.keys())[1:]  # exclude the depot city 0
    all_tours = permutations(city_indices)
    for tour in all_tours:
        yield [0] + list(tour) + [0]

# Calculate the cost of a complete tour
def tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(tour[i], tour[i + 1])
    return total_cost

# Find the shortest tour
def find_shortest_tour():
    best_tour = None
    min_cost = float('inf')
    for tour in generate_tours():
        cost = tour_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour
    return best_tour, min_cost

# Get the best tour and its cost
best_tour, best_tour_cost = find_shortest_tour()

# Display the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_tour_cost}")