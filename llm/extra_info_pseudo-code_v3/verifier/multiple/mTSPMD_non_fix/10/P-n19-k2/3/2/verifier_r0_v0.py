import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return round(total_cost, 2)

def test_solution():
    coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }
    
    robot_tours = [
        [0, 6, 18, 5, 7, 2, 9, 15, 13, 16],
        [0, 1, 10, 12, 14, 4, 11, 3, 8, 17]
    ]
    
    robot_costs = [102.66, 99.43]
    calculated_costs = [calculate_total_cost(tour, coordinates) for tour in robot_tours]
    
    # Test all cities are visited exactly once
    all_cities_visited_once = sorted(sum(robot_tours, []))
    correct_city_visit = all_cities_visited_once == sorted(coordinates.keys())
    
    # Test travel costs
    correct_costs = all(round(calculated_costs[i], 2) == robot_costs[i] for i in range(2))
    
    # Test tour starts from designated depots
    correct_starts = all(tour[0] == 0 for tour in robot_tours)  # Both start at city 0
    
    # Overall check
    if correct_city_visit and correct_costs and correct_starts:
        print("CORRECT")
    else:
        print("FAIL")

test_solution()