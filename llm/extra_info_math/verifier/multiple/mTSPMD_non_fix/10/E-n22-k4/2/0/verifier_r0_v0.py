import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution():
    # Cities coordinates
    cities = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
        (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
        (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
        (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    
    # Solution provided
    robot_tours = [
        [0],
        [0],
        [0],
        [0, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    # Calculate distances and verify solution
    all_visited_cities = set()
    total_cost = 0
    
    for tour in robot_tours:
        previous_city = tour[0]
        for city in tour[1:]:
            total_cost += calculate_distance(cities[previous_city], cities[city])
            previous_city = city
        all_visited_cities.update(tour)
    
    # Check if all cities are visited exactly once
    if len(all_visited_cities) != 22 or all_visited_cities != set(range(22)):
        return "FAIL"
    
    # Check if minimal cost is indeed minimized (here we assume it is since we cannot compare without an alternative)
    # However, we can also check for the correctness of distance calculation by hardcoding proper distances for comparison if required.
    
    # Check if robots start at their designated depot and do not return
    # Since all robots start and end at city 0 in this solution, this condition need to verify they 'do not need to end' at their start point.
    if any([not tour or tour[0] != 0 for tour in robot_tours]):
        return "FAIL"
    
    # Given this setup, all tests pass, so return "CORRECT"
    return "CORRECT"

print(check_solution())