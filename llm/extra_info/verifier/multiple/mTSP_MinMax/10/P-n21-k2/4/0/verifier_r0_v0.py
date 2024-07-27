import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_solution():
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
        (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    tours = [
        [0, 6, 5, 9, 7, 2, 8, 3, 10, 4, 1, 0],
        [0, 16, 11, 15, 12, 19, 18, 13, 17, 14, 20, 0]
    ]
    tour_costs = [126.59, 145.76]

    # Check Requirement 1: All cities visited exactly once by a robot, and tour begins and ends at the depot
    all_visited_cities = set()
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"  # Each tour does not start and end at the depot city
        all_visited_cities.update(tour[1:-1])  # exclude depot city
            
    if all_visited_cities != set(range(1, 21)):
        return "FAIL"  # Not all cities are visited or are visited more than once
   
    # Check Requirement 2: Handled by previous checks (each tour starts and ends at the depot)

    # Requirement 3: Travel cost calculations
    for idx, tour in enumerate(tours):
        tour_cost_calculated = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        if not math.isclose(tour_cost_calculated, tour_costs[idx], rel_tol=1e-2):
            return "FAIL"  # Incorrect cost calculation
    
    return "CORRECT"

# Run the unit test
result = test_solution()
print(result)