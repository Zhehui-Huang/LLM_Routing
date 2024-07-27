import math
import random

# Coordinates dictionary where key is city index and value is tuple (x, y)
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Creating initial solution by dividing cities almost equally
def initial_solution():
    cities = list(range(1, 21))
    random.shuffle(cities)
    mid = len(cities) // 2
    return cities[:mid], cities[mid:]

# 2-opt optimization algorithm
def two_opt(route):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(calculate_distance(new_route[k], new_route[k + 1]) for k in range(len(new_route) - 1)) < \
                   sum(calculate_distance(route[k], route[k + 1]) for k in range(len(route) - 1)):
                    route = new_route
                    improved = True
    return route

# Calculate total distance of route
def calculate_total_cost(route):
    return sum(calculate_distance(route[i], route[i + 1]) for i in range(len(route) - 1))

# Generate initial soltuions
tour1, tour2 = initial_solution()
tour1 = [0] + tour1 + [0]
tour2 = [0] + tour2 + [0]

# Optimize tours
optimized_tour1 = two_opt(tour1)
optimized_tour2 = two_opt(tour2)

# Calculate tour costs
cost1 = calculate_total_cost(optimized_tour1)
cost2 = calculate_total_cost(optimized_tour2)
total_cost = cost1 + cost2

# Printing output in the required format
print("Results:")
print(f"Robot 0 Tour: {optimized_tour1}")
print(f"Robot 0 Total Travel Cost: {cost1}\n")
print(f"Robot 1 Tour: {optimized_tour2}")
print(f"Robot 1 Total Travel Cost: {cost2}\n")
print(f"Overall Total Travel Cost: {total_cost}")