import math
from itertools import permutations

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

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all possible tours starting and ending at the depot (city 0)
def all_tours(cities):
    city_list = list(cities.keys())
    city_list.remove(0)
    return permutations(city_list)

# Find the shortest tour that visits every city exactly once and returns to the depot
def shortest_tour():
    min_cost = float('inf')
    best_tour = []
    for tour in all_tours(cities):
        tour_cost = 0
        # Start at the depot
        prev_city = 0
        # Calculate the cost of the entire tour
        for city in tour:
            tour_cost += distance(prev_city, city)
            prev_city = city
        # Return to the depot
        tour_cost += distance(prev_city, 0)
        # Check if the current tour is the shortest found so far
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = [0] + list(tour) + [0]
    return best_tour, min_cost

# Run the function and output results
tour, total_cost = shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")