import math
import itertools

# Define the cities' coordinates
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate initial route using nearest neighbor heuristic
def nearest_neighbor(start_city):
    unvisited = set(cities.keys())
    unvisited.remove(start_city)
    route = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unfound for unfound in unvisited, key=lambda city: calculate_distance(current_city, city))
        route.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    route.append(start_city)  # Return to the depot
    return route

# 2-opt swap to improve the tour
def two_opt(route):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # Skip consecutive nodes
                if calculate_distance(route[i - 1], route[i]) + calculate_distance(route[j - 1], route[j]) > \
                   calculate_distance(route[i - 1], route[j - 1]) + calculate_distance(route[i], route[j]):
                    route[i:j] = route[j - 1:i - 1:-1]
                    improved = True
    return route

# Compute the total travel cost of a tour
def total_cost(route):
    return sum(calculate_distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Assemble the TSP solution
initial_tour = nearest_neighbor(0)
optimal_tour = two_opt(initial_tour)
total_travel_cost = total_cost(optimal_tour)

# Print the results
print("Tour: " + str(optimal_tour))
print("Total travel cost: {:.2f}".format(total_travel_cost))