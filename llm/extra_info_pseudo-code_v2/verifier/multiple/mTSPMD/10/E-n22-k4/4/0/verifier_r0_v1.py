import math

# Test function to verify if the solution meets the specified requirements
def test_solution(robot_tours, city_coordinates):
    total_cost_calculated = 0
    # Set to track all visited cities by all robots
    all_visited = set()
    
    # Check each robot tour
    for robot_id, tour in robot_tours.items():
        depot = robot_id  # Assuming depot is the index of the robot, which must start and end there.
        start_city = tour[0]
        end_city = tour[-1]
        
        # Check that each tour starts and ends at its assigned depot
        if start_city != depot or end_city != depot:
            print(f"Robot {robot_id} does not start or end at its depot.")
            return "FAIL"
        
        # Calculate total travel distance for each robot and check city visiting rules
        tour_cost = 0
        previous_city = tour[0]
        visited_cities = set(tour)
        
        # Calculate the travel cost for the tour
        for city in tour[1:]:
            tour_cost += calculate_distance(city_coordinates[previous_city], city_coordinates[city])
            previous_city = city
        
        # Update tracking of visited cities
        all_visited.update(visited_cities)
        
        # Accumulate total calculated cost
        total_cost_calculated += tour_cost
    
    # Check if all cities are visited exactly once by any robot
    if len(all_visited) != len(city_coordinates) or any(tour.count(city) > 1 for cities in robot_tours.values() for city in cities):
        print("Not all cities are visited exactly once by the robots.")
        return "FAIL"
    
    # Optionally check total travel cost matches reported approximation closely
    if not math.isclose(total_cost_calculated, 1128.890866261554, rel_tol=1e-5):
        print(f"Total calculated cost {total_cost_calculated} does not match the reported cost closely.")
        return "FAIL"
    
    return "CORRECT"

# Calculate Euclidean distance between two points
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates which need to be provided for the function to work
city_coordinates = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Test with given tours
robot_tours = {
    0: [0, 14, 16, 13, 11, 4, 7, 5, 9, 10, 8, 6, 12, 15, 18, 20, 17, 21, 19, 0],
    1: [1, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 5, 7, 9, 1],
    2: [2, 5, 7, 9, 10, 8, 6, 4, 11, 13, 16, 14, 17, 21, 19, 20, 18, 15, 12, 2],
    3: [3, 4, 8, 6, 7, 5, 9, 10, 12, 15, 18, 20, 17, 21, 19, 13, 16, 14, 11, 3]
}

# Run the test
output = test_solution(robot_tours, city_coordinates)
print(output)