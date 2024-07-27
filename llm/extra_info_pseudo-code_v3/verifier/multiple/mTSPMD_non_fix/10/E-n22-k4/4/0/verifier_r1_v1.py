import math

# Define the cities coordinates (Depots included)
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Given tours
robots_tours = [
    [0, 14, 17, 20, 10, 5, 4],
    [0, 16, 19, 21, 9, 2],
    [0, 12, 15, 18, 7, 1],
    [0, 13, 11, 8, 6, 3]
]

# Given costs
given_costs = [137.50503266621382, 127.27519007733558, 111.4797772480147, 75.13592297270176]

def calculate_distance(city1, city2):
    x1, y1 = cities_coordinates[city1]
    x2, y2 = cities_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def test_solution(robots_tours, cities_coordinates):
    all_visited = set()
    cities_count = len(cities_coordinates)
    total_calculated_cost = 0

    for robot_index, tour in enumerate(robots_tours):
        tour_cost = 0
        previous_city = tour[0] 
        for city in tour[1:]:
            all_visited.add(previous_city)
            tour_cost += calculate_distance(previous_city, city)
            previous_city = city
            
        # Account for the initial city in visited
        all_visited.add(previous_city)
        
        if not math.isclose(tour_cost, given_costs[robot_index], rel_tol=1e-5):
            print(f"Cost mismatch for robot {robot_ialgo_index}: {tour_cost} vs given {given_costs[robot_index]}")
            return "FAIL"

        total_calculated_cost += tour_cost
    
    if len(all_visited) != cities_count:
        print("Not all cities visited or some cities visited more than once. Total cities visited: ", len(all_city_visited))
        return "FAIL"
    
    if not math.isclose(total_calculated_cost, sum(given_costs), rel_tol=1e-5):
        print(f"Overall cost mismatch: {total_calculated_cost} vs given {sum(given_costs)}")
        return "FAIL"
    
    return "CORRECT"

# Print the result of the unit tests
print(test_solution(robots_tours, cities_coordinates))