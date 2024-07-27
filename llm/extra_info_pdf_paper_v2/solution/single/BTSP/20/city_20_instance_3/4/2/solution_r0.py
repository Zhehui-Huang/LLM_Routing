import math
import itertools

# Define the cities based on the given coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to evaluate a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(cities[tour[i]], cities[tour[i + 1]])
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

# Heuristic: Nearest neighbour algorithm
def nearest_neighbour_tour(start):
    unvisited = set(cities.keys())
    unvisited.remove(start)
    tour = [start]
    current_city = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(start)  # Return to the start
    return tour

# Construct a tour using the given heuristic
tour = nearest_neighbour_tour(0)
total_cost, max_distance = evaluate_tour(tour)

# Outputs
print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_distance, 2)}")