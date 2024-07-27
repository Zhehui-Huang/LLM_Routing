import math
from itertools import permutations

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculate the distance matrix
n_cities = len(coordinates)
distance_matrix = [[0] * n_cities for _ in range(n_cities)]
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def calculate_tour_cost(tour):
    total_cost = 0
    for k in range(len(tour) - 1):
        total_cost += distance_matrix[tour[k]][tour[k+1]]
    return total_cost

def find_best_routes():
    cities = list(range(1, n_cities))  # non-depot city indices
    min_max_cost = float('inf')
    best_routes = []

    for division in permutations(cities):
        mid_point = len(division) // 2
        route1 = [0] + list(division[:mid_point]) + [0]
        route2 = [0] + list(division[mid_point:]) + [0]

        cost1 = calculate_tour_cost(route1)
        cost2 = calculate_tour_cost(route2)
        
        max_cost = max(cost1, cost2)

        if max_cost < min_max_cost:
            min_max_cost = max_cost
            best_routes = [route1, route2, max_cost]
    
    return best_routes

best_routes = find_best_routes()

# Display the results
print("Robot 0 Tour: {}".format(best_routes[0]))
print("Robot 0 Total Travel Cost: {:.2f}".format(calculate_tour_cost(best_routes[0])))
print("Robot 1 Tour: {}".format(best_routes[1]))
print("Robot 1 Total Travel Cost: {:.2f}".format(calculate_tour_cost(best_routes[1])))
print("Maximum Travel Cost: {:.2f}".format(best_routes[2]))