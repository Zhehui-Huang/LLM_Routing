import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def is_valid_tour(tour, total_distance):
    # Coordinates of each city by index
    coordinates = [
        (8, 11),  # 0 - Depot
        (40, 6),   # 1
        (95, 33),  # 2
        (80, 60),  # 3
        (25, 18),  # 4
        (67, 23),  # 5
        (97, 32),  # 6
        (25, 71),  # 7
        (61, 16),  # 8
        (27, 91),  # 9
        (91, 46),  # 10
        (40, 87),  # 11
        (20, 97),  # 12
        (61, 25),  # 13
        (5, 59),   # 14
        (62, 88),  # 15
        (13, 43),  # 16
        (61, 28),  # 17
        (60, 63),  # 18
        (93, 15)   # 19
    ]

    # Check if the tour starts and ends at the depot (index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if all cities are visited exactly once (excluding depot, visited exactly twice)
    visited = set(tour)
    if len(visited) != len(coordinates) or sorted(tour[1:-1]) != list(range(1, len(coordinates))):
        return False
    
    # Check if the calculated total distance matches the provided distance
    calculated_total_distance = 0
    for i in range(len(tour) - 1):
        city_a = coordinates[tour[i]]
        city_b = coordinates[tour[i+1]]
        calculated_total_distance += calculate_euclidean_distance(city_a[0], city_a[1], city_b[0], city_b[1])
    
    if not math.isclose(calculated_total_distance, total_distance, rel_tol=1e-9):
        return False

    return True

# Test the provided solution
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
total_travel_cost = 349.1974047195548

if is_valid_tour(tour, total_travel_cost):
    print("CORRECT")
else:
    print("FAIL")