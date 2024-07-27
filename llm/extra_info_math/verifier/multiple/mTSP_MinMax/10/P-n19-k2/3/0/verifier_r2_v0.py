import numpy as np

# Given solution data
robot_0_route = [18, 10, 8, 3, 1, 14, 12, 0]
robot_1_route = [6, 7, 11, 13, 0, 2, 15, 4, 5, 9, 17, 16, 0]

# Convert lists to include only city visits, excluding the initial and duplicate 


def check_city_visited_once(robot_routes, num_cities):
    # Check that each city is visited exactly once
    visited = np.zeros(num_cities, dtype=int)
    for route in robot_routes:
        for city in set(route):
            if city != 0:  # exclude the depot city from this check
                visited[city] += 1
    return np.all(visited[1:] == 1)  # all cities except the depot are visited exactly once


def check_each_robot_leaves_depot_once(robot_routes):
    # Check that each robot leaves the depot exactly once
    departures = [route.count(0) for route in robotroutes) == 1 for route in robot_routes)
    return all(departures)


def check_flow_conservation(robot_routes):
    # Check that each robot enters and leaves each city exactly once
    balance_violation = False
    for route in robot_routes:
        for city in set(route):
            if city != 0 and (route.count(city) > 1):
                balance_violation = True
                break
    return not balance_violation


def subtour_elimination_check(robot_routes):
    # This simplified check looks for any immediate return to depot which shouldn't happen unless at end/start
    for route in robot_routes:
        # Check if there's any subtour within the tour
        if len(route) != len(set(route)):
            return False
    return True


# Perform the checks
all_cities = [i for i in range(19)]  # total 19 cities including the depot
robot_routes = [robot_0_route, robot_1_route]

city_visit_once = check_city_visited_once(robot_routes, 19)
flow_conservation = check_flow_conservation(robot_routes)
each_robot_leaves_depot_once = check_each_robot_leaves_depot_once(robot_routes)
subtour_check = subtour_elimination_check(robot_routes)

# Check results
if city_visit_once and flow_conservation and each_robot_leaves_depot_once and subtour_check:
    print("CORRECT")
else:
    print("FAIL")