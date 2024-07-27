import math
import itertools

# Coordinates for each city, including the depot at index 0
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    (x1, y1), (x2, y2) = coordinates[city1], coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of cities
n = len(coordinates)

# Generate initial greedy tour to use as baseline
def generate_greedy_tour(start=0):
    unvisited = set(range(1, n))
    tour = [start]
    while unvisited:
        current = tour[-1]
        next_city = min(unvisited, key=lambda city: distance(current, city))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)
    return tour

# Evaluate total cost and max distance in a tour
def evaluate_tour(tour):
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    max_distance = max(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    return total_cost, max_distance

# Greedy Tour
greedy_tour = generate_greedy_tour()
total_cost, max_distance = evaluate_tour(greedy_tour)

# Output
print("Tour: ", greedy_tour)
print("Total travel cost: ", total_cost)
print("Maximum distance between consecutive cities: ", max_distance)