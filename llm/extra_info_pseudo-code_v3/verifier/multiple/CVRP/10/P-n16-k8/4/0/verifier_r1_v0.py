import math

# City Coordinates (city_index, x, y)
city_coords = [
    (0, 30, 40), (1, 37, 52), (2, 49, 49), (3, 52, 64), (4, 31, 62),
    (5, 52, 33), (6, 42, 41), (7, 52, 41), (8, 57, 58), (9, 62, 42),
    (10, 42, 57), (11, 27, 68), (12, 43, 67), (13, 58, 48), (14, 58, 27), (15, 37, 69)
]

# Demand of each city
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Robot Tours
tours = [
    [0, 13, 12, 5, 0],
    [0, 4, 10, 0],
    [0, 7, 15, 9, 0],
    [0, 14, 3, 0],
    [0, 1, 11, 0],
    [0, 6, 0],
    [0, 2, 0],
    [0, 8, 0]
]

# Robot Capacity
capacities = [35] * 8

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(tours, capacities, city_demands):
    all_visited = set()
    for i, tour in enumerate(tours):
        remaining_capacity = capacities[i]
        previous_city = tour[0]
        for city in tour[1:]:
            demand = city_demands[city]
            if remaining_capacity - demand < 0:
                return False, "Capacity exceeded"
            remaining_capacity -= demand
            all_visited.add(city)
            previous_city = city
        if previous_city != 0:
            return False, "Tour does not end at depot"

    if all_visited.difference({0}) != set(range(1, 16)):
        return False, "Not all cities are visited"

    return True, "All constraints satisfied"

def calculate_total_cost(tours):
    overall_cost = 0
    for tour in tours:
        tour_cost = 0
        last_city = tour[0]
        for next_city in tour[1:]:
            last_x, last_y = city_coords[last_city][1], city_coords[last_city][2]
            next_x, next_y = city_coords[next_city][1], city_coords[next_city][2]
            tour_cost += calculate_euclidean_distance(last_x, last_y, next_x, next_y)
            last_city = next_city
        overall_cost += tour_cost
    return overall_cost

# Test function
def test_solution():
    valid, reason = validate_solution(tours, capacities, city_demands)
    if not valid:
        return "FAIL"
    
    calculated_total_cost = calculate_total_cost(tours)
    expected_total_cost = 582.01
    if abs(calculated_total_cost - expected_total_cost) < 1e-2:
        return "CORRECT"
    else:
        return "FAIL"

# Run test
test_result = test_solution()
print(test_result)