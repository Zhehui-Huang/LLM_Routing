import math

# Provided coordinates for cities, including depot city 0
city_locations = [
    (3, 26),   # 0
    (85, 72),  # 1
    (67, 0),   # 2
    (50, 99),  # 3
    (61, 89),  # 4
    (91, 56),  # 5
    (2, 65),   # 6
    (38, 68),  # 7
    (3, 92),   # 8
    (59, 8),   # 9
    (30, 88),  # 10
    (30, 53),  # 11
    (11, 14),  # 12
    (52, 49),  # 13
    (18, 49),  # 14
    (64, 41),  # 15
    (28, 49),  # 16
    (91, 94),  # 17
    (51, 58),  # 18
    (30, 48)   # 19
]

# Provided tour result
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0]
total_travel_cost = 478.43
max_distance_between_cities = 80.61

def verify_tour_requirements(tour, city_locations, expected_total_cost, expected_max_distance):
    if tour[0] != 0 or tour[-1] != 0:  # Check if starts and ends at depot city 0
        return "FAIL"
    if len(set(tour)) != len(city_locations):  # Check if all cities are included exactly once
        return "FAIL"
    if len(tour) != len(city_locations) + 1:  # Check if passing through each city only once (+ return)
        return "FAIL"
    
    # Compute the actual total distance and the actual max distance
    actual_total_cost = 0
    actual_max_distance = 0
    
    for i in range(len(tour) - 1):
        x1, y1 = city_locations[tour[i]]
        x2, y2 = city_locations[tour[i+1]]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        actual_total_cost += distance
        if distance > actual_max_distance:
            actual_max_distance = distance
    
    # Check if total cost and max distance are correctly calculated
    if not (math.isclose(actual_total_cost, expected_total_cost, rel_tol=1e-2) and 
            math.isclose(actual_max_distance, expected_max(Number 3, expected_max_distance, rel_tol=1e-2)):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
result = verify_tour_requirements(tour, city_locations, total_travel_cost, max_distance_between_cities)
print(result)