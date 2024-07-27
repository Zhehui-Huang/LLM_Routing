import math
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to compute the total travel cost of a tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Generate all possible tours that start and end at the depot and include exactly 7 cities
def generate_tours():
    best_tour = None
    best_cost = float('inf')
    for cities_subset in permutations(range(1, 20), 6):  # Choose 6 other cities as depot is fixed
        current_tour = [0] + list(cities_subset) + [0]
        current_cost = total_cost(current_tour)
        if current_cost < best_cost:
            best_tour, best_cost = current_tour, current_cost
    return best_tour, best_cost

# Find the minimum tour with the heuristic
result_tour, result_cost = generate_tours()

# Output the results
print("Tour:", result_tour)
print("Total travel cost:", result_cost)