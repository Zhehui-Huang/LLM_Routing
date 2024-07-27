import math

# City coordinates with city number as the key
city_coordinates = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

# Solution provided
tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
calculated_cost = 349.1974047195548

def calculate_euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, calculated_cost):
    # Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each city is visited exactly once except the depot
    visited = set(tour)
    if len(visited) != 21 or any(tour.count(city) != 1 for city in range(1, 20)):
        return "FAIL"
    
    # Calculate the total travel cost and compare
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean distance(tour[i], tour[i+1])
        
    if abs(total_cost - calculated_cost) > 1e-3:  # considering floating point error margin
        return "FAIL"
    
    return "CORRECT"

# Validate the provided solution
test_result = validate_tour(tour, calculated_cost)
print(test_result)