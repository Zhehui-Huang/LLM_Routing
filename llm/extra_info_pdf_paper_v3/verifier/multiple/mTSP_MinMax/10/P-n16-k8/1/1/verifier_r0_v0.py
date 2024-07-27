import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 49),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 48),
        14: (58, 27),
        15: (37, 69)
    }
    
    tours = [
        [0, 1, 9, 0],
        [0, 2, 10, 0],
        [0, 3, 11, 0],
        [0, 4, 12, 0],
        [0, 5, 13, 0],
        [0, 6, 14, 0],
        [0, 7, 15, 0],
        [0, 8, 0]
    ]
    
    reported_costs = [72.88070710888512, 52.4625939010481, 86.03587467520119, 64.98936367308863, 
                      68.36272673975597, 64.17258428512785, 83.62034367443502, 64.89992295835181]
    max_reported_cost = 86.03587467520119
    
    # Check all cities visited exactly once
    all_visited = set()
    for tour in tours:
        all_visited.update(tour[1:-1])  # exclude the depot city from start and end
    if sorted(all_visited) != list(range(1, 16)):
        return "FAIL"

    # Calculate travel costs and check against reported costs
    for tour, reported_cost in zip(tours, reported_costs):
        total_cost = 0
        for i in range(len(tour) - 1):
            total_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        if not math.isclose(total_cost, reported_cost, abs_tol=1e-5):
            return "FAIL"
    
    # Check if the max cost is correctly reported
    if not math.isclose(max_reported_cost, max(reported_costs), abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())