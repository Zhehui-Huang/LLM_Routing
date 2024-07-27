import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def verify_solution(tour, total_cost, city_positions):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Starting and Ending at depot city 0
    if len(set(tour)) != 10:
        return "FAIL"  # Visiting exactly 10 cities including the depot city
    if any(city_index >= len(city_positions) or city_index < 0 for city_index in tour):
        return "FAIL"  # Valid city indices
    calculated_cost = sum(euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]]) for i in range(len(tour)-1))
    if abs(calculated_cost - total_cost) > 1e-5:  # Allowing a tiny margin for floating-point arithmetic differences
        return "FAIL"  # Correct calculation of the total travel cost
    return "CORRECT"

# City coordinates
city_positions = [
    (3, 26),  # Depot City 0
    (85, 72),
    (67, 0),
    (50, 99),
    (61, 89),
    (91, 56),
    (2, 65),
    (38, 68),
    (3, 92),
    (59, 8),
    (30, 88),
    (30, 53),
    (11, 14),
    (52, 49),
    (18, 49),
    (64, 41),
    (28, 49),
    (91, 94),
    (51, 58),
    (30, 48)
]

# Tour from user
tour_response = [0, 12, 9, 13, 1, 17, 8, 6, 14, 19, 0]
total_cost_response = 351.95529712421035

# Verify solution
print(verify_solution(tour_response, total_cost_response, city_positions))