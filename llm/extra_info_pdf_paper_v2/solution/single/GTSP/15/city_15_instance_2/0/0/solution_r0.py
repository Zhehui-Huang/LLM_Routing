import math
from itertools import permutations

# Define coordinates of cities
cities = {0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 5: (36, 30),
          6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 10: (51, 28), 11: (44, 79),
          12: (56, 58), 13: (72, 43), 14: (6, 99)}

# Define city groups
groups = {0: [8, 12, 14], 1: [7, 10, 11], 2: [4, 6, 9], 3: [1, 3, 13], 4: [2, 5]}

# Calculate the Euclidean distance between two cities
def city_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all possible combinations of cities to visit (one from each group)
def possible_combinations(groups):
    return list(permutations([group[0] for group in groups.values()]))

# Calculate the total distance of a specific tour configuration
def calculate_tour_cost(tour):
    total_cost = city_distance(0, tour[0])  # initial travel from depot to first city
    for i in range(len(tour) - 1):
        total to the next city
        total_cost += city_distance(tour[i], tour[i + 1])
    total_cost += city_distance(tour[-1], 0)  # return to depot
    return total_cost

# FIollowing code is to attempt to find an optimal route
def find_optimal_route(groups):
    best_tour = None
    min_cost = float('inf')
    for combo in possible_combinations(groups):
        # Calculate cost for each possible tour
        cost = calculate_tour_cost(combo)
        if cost < min_cost:
            min_cost = cost
            best_tour = combo
    
    return best_tour, min_cost

# Get the optimal route and its cost
optimal_tour, optimal_cost = find_optimal_route(groups)
final_tour = [0] + list(optimal_tour) + [0]  # add depot at start and end

# Print the results
print("Tour:", final_tour)
print("Total travel cost:", optimal_cost)