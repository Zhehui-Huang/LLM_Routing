import math

# Coordinates for cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.dist([x1, y1], [x2, y2])

# Robot tours provided
tours = [
    [0, 2, 13, 9, 8, 0], 
    [0, 15, 12, 3, 0], 
    [0, 21, 6, 0],
    [0, 14, 17, 0],
    [0, 16, 1, 10, 0],
    [0, 18, 19, 0],
    [0, 4, 11, 0],
    [0, 20, 5, 22, 7, 0]
]

def validate_tours():
    all_visited = set()
    total_cost_calculated = 0

    # Validate collective visits and cost calculation
    for tour in tours:
        for i in range(1, len(tour) - 1):
            all_visited.add(tour[i])
        
        tour_cost = 0
        for j in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[j], tour[j+1])

        total_cost_calculated += tour_cost

    correct_total_cost = 505.75
    all_cities_covered = all_visited == set(range(1, 23))
    correct_tour_format = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    cost_match = math.isclose(total_cost_calculated, correct_total_cost, abs_tol=0.1)

    if all_cities_covered and correct_tour_format and cost_match:
        return "CORRECT"
    else:
        return "FAIL"

# Execute the validation function
result = validate_tours()
print(result)