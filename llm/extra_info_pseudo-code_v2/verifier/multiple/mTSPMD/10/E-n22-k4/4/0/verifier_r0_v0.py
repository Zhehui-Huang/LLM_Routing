import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(robot_tours, cities):
    # Unpacking city coordinates
    city_coordinates = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
        4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
        8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
        12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
        16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }
    
    total_cost_calculated = 0
    all_visited = set()
    
    # Check each robot tour
    for robot_id, tour in robot_tours.items():
        depot = robot_id
        start_city = tour[0]
        end_city = tour[-1]
        
        # Check start and end at depot
        if start_city != depot or end_city != depot:
            print(f"Robot {robot_id} does not start or end at its depot.")
            return "FAIL"
        
        # Check for valid tour and calculate total distance
        tour_cost = 0
        previous_city = tour[0]
        visited_cities = set(tour)
        
        for city in tour[1:]:
            if city != previous_city:  # Valid move, not staying in the same city
                tour_cost += calculate_distance(city_coordinates[previous_city], city_coordinates[city])
                previous_city = city
        
        all_visited.update(visited_cities)
        
        total_cost_calculated += tour_cost
    
    # Check if all cities are visited exactly once
    if len(all_visited) != len(city_coordinates) or any(tour.count(city) > 1 for cities in robot_tours.values() for city in cities):
        print("Not all cities are visited exactly once by the robots.")
        return "FAIL"
    
    # Check if total cost amtches report
    if not math.isclose(total_cost_calculated, 1128.890866261554, rel_tol=1e-5):
        print(f"Total calculated cost {total_login_cost} does not match the reported cost.")
        return "FAIL"
    
    return "CORRECT"

# Given robot tours from the solution
robot_tours = {
    0: [0, 14, 16, 13, 11, 4, 7, 5, 9, 10, 8, 6, 12, 15, 18, 20, 17, 21, 19, 0],
    1: [1, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 5, 7, 9, 1],
    2: [2, 5, 7, 9, 10, 8, 6, 4, 11, 13, 16, 14, 17, 21, 19, 20, 18, 15, 12, 2],
    3: [3, 4, 8, 6, 7, 5, 9, 10, 12, 15, 18, 20, 17, 21, 19, 13, 16, 14, 11, 3]
}

# Check the correctness of the solution
output = test_solution(robot_tours, city_coordinates)
print(output)