import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def solution_test():
    cities_coords = {
        0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
        5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
        10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
        15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
        20: (155, 185), 21: (139, 182)
    }
    
    demands = {
        0: 0, 1: 1100, 2: 700, 3: 800, 4: 1400, 5: 2100, 6: 400, 7: 800, 8: 100,
        9: 500, 10: 600, 11: 1200, 12: 1300, 13: 1300, 14: 300, 15: 900, 16: 2100,
        17: 1000, 18: 900, 19: 2500, 20: 1800, 21: 700
    }
    
    robot_capacity = 6000
    robots_tours = [
        [0, 14, 17, 20, 10, 5, 0],
        [0, 16, 19, 21, 9, 0],
        [0, 12, 15, 18, 7, 2, 1, 0],
        [0, 13, 11, 8, 6, 3, 4, 0]
    ]
    
    # Check if all cities except depot are visited exactly once
    all_visited_cities = sum((tour[1:-1] for tour in robots_tours), [])  # Concatenate lists ignoring the depot (first and last)
    if len(set(all_visited_cities)) != 21 or any(all_visited_cities.count(city) != 1 for city in range(1, 22)):
        return "FAIL"

    # Check if every tour starts and ends at the depot
    if not all(tour[0] == 0 and tour[-1] == 0 for tour in robots_tours):
        return "FAIL"
    
    # Check if the total demand on each robot's tour does not exceed the robot's capacity
    for tour in robots_tours:
        total_demand = sum(demands[city] for city in tour)
        if total_demand > robot_capacity:
            return "FAIL"

    # Calculate the total travel cost and compare
    original_total_cost = 551.4921974050563
    calculated_total_cost = 0
    
    for tour in robots_tours:
        tour_cost = sum(calculate_distance(cities_coords[tour[i]], cities_coords[tour[i + 1]]) for i in range(len(tour) - 1))
        calculated_total_cost += tour_cost
    
    if not math.isclose(calculated_total_cost, original_total_cost, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

print(solution_test())