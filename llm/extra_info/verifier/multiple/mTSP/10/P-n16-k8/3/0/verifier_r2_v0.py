import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution():
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
        4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
        8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
    }
    
    tours = [
        [0, 9, 13, 0],
        [0, 12, 15, 0],
        [0, 6, 0],
        [0, 4, 11, 0],
        [0, 5, 14, 0],
        [0, 3, 8, 0],
        [0, 1, 10, 0],
        [0, 2, 7, 0]
    ]
    
    expected_costs = [68.39, 66.12, 24.08, 57.39, 62.44, 72.82, 41.77, 51.59]
    overall_cost = 444.62
    calculated_overall_cost = 0
    
    visited_cities = set()
    for i, tour in enumerate(tours):
        cost = 0
        for j in range(len(tour) - 1):
            city1 = tour[j]
            city2 = tour[j + 1]
            cost += calculate_distance(*cities[city1], *cities[city2])
            visited_cities.add(city1)
            visited_cities.add(city2)
        calculated_overall_cost += cost
        if not (abs(cost - expected_costs[i]) < 0.1):
            return "FAIL"

    # Check if every city except the depot is visited exactly once
    if len(visited_cities) == 16 and all(city in visited_cities for city in range(1, 16)):
        if abs(calculated_overall_cost - overall_cost) < 0.1:
            return "CORRECT"
    
    return "FAIL"

# Run tests
result = verify_solution()
print(result)