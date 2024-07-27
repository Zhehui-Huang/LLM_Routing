import math
from random import sample
from itertools import permutations
import copy

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Total cities to visit including the depot
k = 12

def calculate_route_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += euclidean_distance(cities[route[i-1]], cities[route[i]])
    return total_distance
    
# Randomly sample a starting subset of k cities, including the depot
def random_initial_subset():
    return [0] + sample(list(cities.keys() - {0}), k-1)

# Swap a city outside the current route with one in the route
def swap_city(route):
    best_route = route
    least_distance = calculate_route_distance(route)
    for i in range(1, len(route)):
        for j in cities.keys() - set(route):
            new_route = copy.deepcopy(route)
            new_route[i] = j
            new_distance = calculate_route = calculate_route_distance(new_route)
            if new_distance < least_distance:
                best_route = new_route
                least_distance = new_distance
    return best_route

def variable_neighborhood_search():
    current_route = random_initial_subset()
    best_route = current_route
    best_distance = calculate_route_distance(best_route)
    
    while True:
        new_route = swap_city(current_route)
        new_distance = calculate_route_distance(new_route)
        if new_distance < best_distance:
            best_route = new_route
            best_distance = new_distance
            current_route = new_route
        else:
            break
    
    return best_route, best_distance

# Solving the k-TSP using Variable Neighborhood Search
final_route, final_distance = variable_neighborhood_search()

# Include back the depot city to complete the tour
final_route.append(0)
final_distance += euclidean_distance(cities[final_route[-2]], cities[0])

# Output the result
print(f"Tour: {final_route}")
print(f"Total travel cost: {final_distance:.2f}")