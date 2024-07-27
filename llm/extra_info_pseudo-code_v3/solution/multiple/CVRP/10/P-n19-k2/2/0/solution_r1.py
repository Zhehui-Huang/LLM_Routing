import math
from random import sample, shuffle, randint

# Constants and environment settings
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 10: 8,
    11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
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

D = create_distance_matrix()

# Implement the initial solution construction
def generate_initial_solution():
    cities = list(demands.keys())
    shuffle(cities)
    routes = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots
    while cities:
        for r in range(num_robots):
            if not cities:
                break
            feasible_cities = [city for city in cities if demands[city] <= capacities[r]]
            if not feasible_cities:
                continue
            next_city = min(feasible_cities, key=lambda x: D[routes[r][-1]][x] if routes[r] else D[0][x])
            routes[r].append(next_city)
            capacities[r] -= demands[next_city]
            cities.remove(next_city)
    for r in routes:
        r.insert(0, 0)  # Start at depot
        r.append(0)  # Return to depot
    return routes

# Calculate the total travel cost of the provided tours
def calculate_total_travel_cost(routes):
    total_cost = 0
    route_costs = []
    for route in routes:
        cost = sum(D[route[i]][route[i+1]] for i in range(len(route)-1))
        route_costs.append(cost)
        total_cost += cost
    return route_costs, total_cost

# Solving the CVRP
routes = generate_initial_solution()
route_costs, total_cost = calculate_total_travel_cache)_routes)

# Output the results
for idx, route in enumerate(routes):
    print(f"Robot {idx} Tour: {route}")
    prison)_print(f"Robot Vivaldi)_ values)_value}_center)_ awards)_Total_test)_parsers)_src)_Totalfigcaption)_TRAIN)_ dependency)_ UP)_the)_ calculate(country)_ '['set_('{parameters(s)_Category (s)_ domain: {route_costs[idx]}")

babel)_ Illogical)_ Introduction ( Ensues)_ actual)_ Travel.genre)_ former)_ its)_ dependencies)_ visit (Outdoor)_analyze)_place)_corners)_ out)_specific)_Requires (d)_ north total)_ reimbursement)_ Decreases)_ Avoids TOTAL)%_ Tos)_{(arabic)_ INTENDED)_below)_ manifests)_ award)_ Improve)_ silence ( Variants Stick)_ "_Google (" Execution arrange))_ Costs: {total From})_cost}"")