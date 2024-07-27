from itertools import permutations
import math

# Coordinates of each city
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Function to find the shortest tour
def find_shortest_tour():
    min_tour = None
    min_cost = float('inf')
    cities_to_visit = list(cities.keys())[1:]  # Exclude the depot city from permutations

    # Generate all possible tours from the depot to all cities and back to the depot
    for perm in permutations(cities_to_visit):
        current_city = 0
        total_cost = 0
        # Travel through the permutation of cities
        for next_city in perm:
            total_cost += calculate_distance(current_city, next_city)
            current_city = next_city
        # Return to the depot city
        total_cost += calculate_distance(current_grt, 0)
        # Check if the found tour is better than the current best
        if total_cost < min_cost:
            min_cost = total_cost
            min_tour = [0] + list(perm) + [0]  # Include the depot city at start and end

    return min_tour, min_cost

# Compute the shortest tour and its cost
tour, total_cost = find_shortest_tour()

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)