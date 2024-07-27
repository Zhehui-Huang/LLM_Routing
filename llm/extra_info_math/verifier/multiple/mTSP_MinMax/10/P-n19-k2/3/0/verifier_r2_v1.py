import numpy as np

# Simulated routes based on your prior input
robot_0_route = [0, 18, 10, 8, 3, 1, 14, 12, 0]
robot_1_route = [0, 6, 7, 11, 13, 2, 15, 4, 5, 9, 17, 16, 0]

# Convert each tour into a list of robot routes
robot_routes = [robot_0_route, robot_1_route]


def check_city_visited_once(robot_routes, num_cities):
    # Check that each city is visited exactly once
    visited = [0] * num_cities
    for route in robot_routes:
        for city in route:
            if city != 0:  # exclude the depot city from this check
                visited[city] += 1
    return all(v == 1 for v in visited[1:])  # check all cities except the depot are visited exactly once


def check_flow_conservation(robot_routes):
    # Check that each robot enters and leaves each city exactly once
    for route in robot_routes:
        visited_cities = set()
        for city in route:
            if city != 0 and city in visited_cities:
                return False
            visited_cities.add(city)
    return True


def check_each_robot_leaves_depot_once(robot_routes):
    # Each robot starts and ends its tour at the depot, check if depot appearances are exactly two
    for route in robot_routes:
        if route.count(0) != 2:  # Start and end at depot
            return False
    return True


def subtour_elimination_check(robot_routes):
    # This simple check assumes no direct returns to depot in between, except at end
    for route in robot_routes:
        if len(route) != len(set(route)):
            return False
    return True


# Number of cities, including the depot
num_cities = 19

# Perform the checks
city_visit_once = check_city_visited_once(robot_routes, num_cities)
flow_conservation = check_flow_conservation(robot_routes)
each_robot_leaves_depot_once = check_each_robot_leaves_depot_once(robot_routes)
subtour_check = subtour_elimination_check(robot_routes)

# Output the test results
if city_visit_once and flow_conservation and each_robot_leaves_depot_once and subtour_check:
    print("CORRECT")
else:
    print("FAIL")