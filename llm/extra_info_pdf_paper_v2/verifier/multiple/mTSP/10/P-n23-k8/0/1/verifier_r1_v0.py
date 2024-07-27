import math

# Coordinates of the cities
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Provided robot tours
robot_tours = [
    [0, 1, 17, 0],
    [0, 8, 16, 0],
    [0, 9, 10, 0],
    [0, 21, 19, 0],
    [0, 2, 3, 0],
    [0, 4, 7, 0],
    [0, 14, 13, 0],
    [0, 20, 5, 12, 11, 6, 18, 22, 15, 0]
]

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0])**2 + (city_coordinates[city1][1] - city_coordinates[city2][1])**2)

# Verify Requirement 1: Each city is visited exactly once (excluding the depot)
def test_visit_each_city_once_exactly(tours, num_cities):
    city_visited = [False] * num_cities
    for tour in tours:
        for city in tour[1:-1]:  # skipping the depot at the start and end
            if city_visited[city]:
                return False
            city_visited[city] = True

    return all(city_visited[1:])  # ignore the depot city

# Verify Requirement 2: Each robot starts and ends at the depot
def test_start_end_depot(tours):
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

# Check the solutions
def verify_solution(tours):
    requirement_1 = test_visit_each, city_once_exactly(tours, len(city_coordinates))
    requirement_2 = test_start_end_depot(tours)

    if requirement_1 and requirement_2:
        print("CORRECT")
    else:
        print("FAIL")

verify_solution(robot_tours)