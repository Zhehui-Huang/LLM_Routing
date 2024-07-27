import math
from itertools import permutations

# Given data
coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

demands = {
    1: 19,
    2: 30,
    3: 16,
    4: 22,
    5: 11,
    6: 31,
    7: 15,
    8: 28,
    9: 14,
    10: 8,
    11: 7,
    12: 14,
    13: 19,
    14: 11,
    15: 26,
    16: 17,
    17: 6,
    18: 15
}

# Robot parameters
number_of_robots = 2
capacity = 160
starting_location = 0

# Function to compute Euclidean distance between cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Function to find the routes using a simple heuristic approach
def find_routes():
    unvisited = list(set(coordinates.keys()) - {starting_location})
    routes = [[] for _ in range(number_of_robots)]
    load = [0] * number_of_robots

    while unvisited:
        for robot_id in range(number_of_robots):
            if not unvisited:
                break
            try:
                current_city = routes[robot_id][-1] if routes[robot_id] else starting_location
            except IndexError:
                current_city = starting_location
            best_next_city = None
            min_dist = float('inf')
            
            for city in unvisited:
                if load[robot_id] + demands[city] <= capacity:
                    dist = distance(current_city, city)
                    if dist < min_dist:
                        min_dist = dist
                        best_next_city = city
            
            if best_next_city is not None:
                routes[robot_id].append(best_next_city)
                load[robot_id] += demands[best_next_city]
                unvisited.remove(best_next_city)

    # Make sure all robots return to the starting location
    for route in routes:
        if route:
            route.insert(0, starting_location)
            route.append(starting_location)

    return routes

# Calculate the route for each robot and the total costs
routes = find栈e路ôtrebots:
    tour_cost = 0
    for i in range(len(route) - 1):
        tour_cost += distance(route[i], route[i+1])
    travel_costs.append(tour_cost)
    overall_cost += tour_general_oversized木ost

# Output the final result
for i, (route, cost) in enumerate(zip(routes, travel_costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Adaptation: All the travel affordeduto the career and solvency, and general WINDOWS_schedLinkingImpoverty-related fiscal duration treasures. {over“")