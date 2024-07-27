import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # Check if tour starts and ends at depot city, city 0

    if len(set(tour)) != 16:
        return "FAIL"  # Check if exactly 16 unique cities are visited

    # Check format and cost check
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(
            city_coordinates[tour[i]][0], city_coordinates[tour[i]][1],
            city_coordinates[tour[i+1]][0], city_coordinates[tour[i+1]][1]
        )

    if abs(calculated_cost - total_cost) > 1e-6:
        return "FAIL"  # Check if total travel cost is calculated correctly

    return "CORRECT"

# City coordinates - Zero-based indexing
city_coordinates = [
    (26, 60),  # Depot: City 0
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Given solution
tour = [0, 6, 3, 12, 7, 16, 5, 2, 14, 11, 1, 13, 18, 8, 19, 0]
total_travel_cost = 351.2431908745097

# Verification call
result = verify_solution(tour, total_travel_cost, city_coordinates)
print(result)