import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35)
    }
    
    tours = {
        0: [0, 16, 6, 20, 2, 10, 12, 4, 8, 18, 14, 0],
        1: [1, 15, 11, 3, 19, 13, 9, 17, 5, 7, 1]
    }
    
    provided_costs = {
        0: 171.820768703562,
        1: 137.90549546878637
    }
    
    calculated_costs = {}
    for robot_id, tour in tours.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_costs[robot_id] = tour_cost
    
    # Check calculated costs against provided cost within a reasonable precision
    cost_comparison = all(abs(provided_costs[i] - calculated_costs[i]) < 1e-4 for i in provided_costs)
    
    # Check that all cities are visited exactly once
    all_cities_visited_once = len(set(tours[0] + tours[1])) == 21 and all(tours[0].count(city) == 1 for city in set(tours[0])) and all(tours[1].count(city) == 1 for city in set(tours[1]))
    
    # Output result based on the evaluation
    if cost_comparison and all_cities_visited_once:
        print("CORRECT")
    else:
        print("FAIL")

test_solution()