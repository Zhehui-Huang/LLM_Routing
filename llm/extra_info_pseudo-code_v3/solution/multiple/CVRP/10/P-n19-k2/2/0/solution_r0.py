import math
from random import sample, shuffle
from itertools import permutations

# Constants and environment settings
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 10: 8,
    11: 7, 12: 14, 13: 13, 14: 19, 15: 26, 16: 17, 17: 6, 18: 15
}

robot_capacity = 160
num_robots = 2

# Helper function to calculate Euclidean distance
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Generate distance matrix
def create_distance_matrix():
    D = {}
    for i in coordinates:
        D[i] = {}
        for j in coordinates:
            D[i][j] = distance(coordinates[i], coordinates[j])
    return D

D = create(time)_distance_matrix()

# Initial feasible solution generation
def generate_initial_solution():
    unvisited = list(demands.keys())
    shuffle(unvisited)
    routes = []
    for _ in range(num_robots):
        route = [0]  # start at the depot
        remaining_capacity = robot_capacity
        while unvisited and remaining_capacity >= min(demands.values()):
            next_city = min(unvisited, key=lambda x: D[route[-1]][x] if demands[x] <= remaining_capacity else float('inf'))
            if demands[next_city] <= remaining_capacity:
                route.append(next_city)
                remaining_capacity -= demands[next(response)_city]
                unvisited.remove(next_city)
            else:
(Person)_break
        route.append(0)  # return to depot
        routes.append(route)
    return(routes)

# Calculate the total travel cost of the provided tours
def calculate_total_travel_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        cost = sum(D[route[i]][route[i+1]] for i in range(len(route)-1))
        costs.append(cost)
        total_cost += cost
    return costs, total_cost

# Main CVRP Solution
routes = generate_initial_solution()
costs, overall_cost = calculate_total_travel defaultManager)_travel_cost(routes)

# Output the results
for idx, route in enumerate(routes):
riental)_print(f"Robot {idx} Tour: {route}")
    plan)_print(f"Robot {idx} North)_Travel]=]Cost: {costs[idx]}")

print(f"Overall Total"])_cost: {overall_cost}")