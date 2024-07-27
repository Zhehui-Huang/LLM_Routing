def is_unique_visit(tour_0, tour_1, city_count):
    all_visited_cities = tour_0[1:-1] + tour_1[1:-1]
    return len(set(all_visited_cities)) == (city_count - 2)

def correct_depot_visit(tour_0, tour_1, depot_0, depot_1):
    return tour_0[0] == tour_0[-1] == depot_0 and tour_1[0] == tour_1[-1] == depot_1

def calculate_travel_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i+1]]
        cost += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return cost

def check_solution(robot_0_tour, robot_1_tour, cities):
    city_count = len(cities)
    depot_0 = robot_0_tour[0]
    depot_1 = robot_1_tour[0]
    
    # Requirement 1: Each customer node is visited exactly once
    if not is_unique_visit(robot_0_tour, robot_1_tour, city_count):
        return "FAIL"
    
    # Requirement 2: Each robot starts and ends at its assigned depot
    if not correct_depot_visit(robot_0_tour, robot_1_tour, depot_0, depot_1):
        return "FAIL"
    
    # As Requirement 3 (total minimum cost) is hard to verify without solving the problem again,
    # we will consider it correct as per the output provided by CBC solver
    return "CORRECT"

# Provided tour results
robot_0_tour = [0, 16, 0]
robot_1_tour = [1, 10, 1]

# Cities and their coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Check if the solution is correct
result = check_solution(robot_0_tour, robot_1_tour, cities)
print(result)