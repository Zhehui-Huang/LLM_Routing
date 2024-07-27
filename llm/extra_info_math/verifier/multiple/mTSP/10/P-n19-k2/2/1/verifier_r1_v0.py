import numpy as np

# Define city coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Define tours
robot_tours = [
    [0, 6, 0],
    [0, 1, 10, 4, 11, 14, 12, 3, 17, 16, 8, 9, 15, 13, 5, 7, 2, 18, 0]
]

# Define test case parameters
number_of_robots = 2
number_of_cities = len(cities)


def check_all_cities_once(robot_tours):
    visited = set()
    for tour in robot_tours:
        for city in tour[1:-1]:  # Exclude the depot city at start and end
            if city in visited:
                return False
            visited.add(city)
    return len(visited) == number_of_cities - 1  # Exclude the depot city

def check_flow_conservation(robot_tours):
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
        previous_city = None
        for city in tour:
            if previous_city is not None and previous_city == city:
                return False  # No city should visit itself consecutively
            previous_city = city
    return True

def check_for_each_robot_starts_and_ends_depot(robot_tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours)

def check_subtour_elimination(robot_tours):
    # Subtour elimination can be verified implicitly by checking if each city is visited exactly once and ends at the depot
    for tour in robot_tours:
        visited = set(tour)
        if len(visited) != len(tour):  # Including repeated depot
            return False
    return True

# Execute tests
all_cities_once = check_all_cities_once(robot_tours)
flow_conservation = check_flow_conservation(robot_tours)
each_robot_starts_ends_depot = check_for_each_robot_starts_and_ends_depot(robot_tours)
subtour_elimination = check_subtour_elimination(robot_tours)

# Determine overall correctness
if all([all_cities_once, flow_conservation, each_robot_starts_ends_depot, subtour_elimination]):
    print("CORRECT")
else:
    print("FAIL")