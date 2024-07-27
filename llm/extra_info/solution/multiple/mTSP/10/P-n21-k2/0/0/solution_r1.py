import math
import random

# Coordinates (City Index: (x, y))
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Helper function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 +
                     (coordinates[city1][1] - coordinates[city2][1])**2)

# 2-opt optimization routine
def two_opt(route):
    best_route = route[:]
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if j-i == 1: continue  # consecutive cities, skip
                new_route = route[:]
                new_route[i:j+1] = route[j:i-1:-1]  # reverse segment
                if sum(calculate_distance(new_route[k], new_route[k+1]) for k in range(len(new_route) - 1)) < \
                   sum(calculate_distance(best_route[k], best_route[k+1]) for k in range(len(best_route) - 1)):
                    best_route = new_route
                    improved = True
        route = best_route
    return best_route

# Function to generate initial solution
def initial_solution():
    cities = list(range(1, 21))
    random.shuffle(cities)
    mid_point = len(cities) // 2
    return cities[:mid_point], cities[mid_point:]

# Create initial paths
path1, path2 = initial_solution()

# Include the starting and ending depot
tour1 = [0] + path1 + [0]
tour2 = [0] + path2 + [0]

# Perform 2-opt optimization on tours
optimized_tour1 = two_opt(tour1)
optimized_tour2 = two_opt(tour2)

# Calculate costs
def calculate_total_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

cost1 = calculate_total_cost(optimized_tour1)
cost2 = calculate_total_cost(optimized_tour2)
total_cost = cost1 + cost2

# Output the results
print("Results:")
print(f"Robot 0 Tour: {optimized_tour1}")
print(f"Robot 0 Total Travel Cost: {cost1}\n")
print(f"Robot 1 Tour: {optimized_tour2}")
print(f"Robot 1 Total Travel Cost: {cost2}\n")
print(f"Overall Total Travel Cost: {total_/3")