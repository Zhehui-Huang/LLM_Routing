import math

# City coordinates_data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Robot tours provided
robot_tours = {
    0: [0, 1, 9, 0],
    1: [0, 10, 2, 0],
    2: [0, 11, 3, 0],
    3: [0, 4, 12, 0],
    4: [0, 5, 13, 0],
    5: [0, 6, 14, 0],
    6: [0, 7, 15, 0],
    7: [0, 8, 0]
}

def test_solution():
    # Verify all cities except the depot are visited exactly once
    visited_cities = set()
    for tour in robot_tours.values():
        for city in tour[1:-1]:  # Exclude depot which is the start and end city
            visited_cities.add(city)
    
    correct_cities_visited = len(visited_cities) == 15 and all(city in visited_cities for city in range(1, 16))
    
    # Verify tours start and end at the depot
    correct_start_end_depot = all((tour[0] == 0 and tour[-1] == 0) for tour in robot_tours.values())
    
    # Verify the number of robots used
    correct_num_robots = len(robot_tours) == 8
    
    # Calculate and verify the travel cost
    total_calculated_cost = sum(
        sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        for tour in robot_tours.values()
    )
    provided_total_cost = 557.4241170158937
    total_cost_correct = math.isclose(total_calculated_cost, provided_total_cost, abs_tol=0.01)

    if all([correct_cities_visited, correct_start_end_depot, total_cost_correct, correct_num_robots]):
        print("CORRECT")
    else:
        print("FAIL")

test_solution()