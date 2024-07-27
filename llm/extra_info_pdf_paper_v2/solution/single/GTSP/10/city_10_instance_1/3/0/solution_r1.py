import itertools
import math

# City coordinates
cities = {0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63),
          5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)}
          
# The groups
groups = {0: [5, 6, 7], 1: [2, 3], 2: [1, 9], 3: [4, 8]}

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generating all combinations: select one city from each group
all_combinations = list(itertools.product(groups[0], groups[1], groups[2], groups[3]))

def find_best_route():
    best_route = None
    min_cost = float('inf')
    
    # Check every combination
    for combination in all_combinations:
        # Permute through the chosen cities for optimal path
        for perm in itertools.permutations(combination):
            route = [0] + list(perm) + [0]  # start and end at the depot
            cost = sum(calc_distance(route[i], route[i+1]) for i in range(len(route) - 1))
            if cost < min_cost:
                min_cost = cost
                best_route = route
    
    return min_cost, best_route

min_cost, best_route = find_best_route()
print("Tour:", best_route)
print("Total travel cost:", min_cost)