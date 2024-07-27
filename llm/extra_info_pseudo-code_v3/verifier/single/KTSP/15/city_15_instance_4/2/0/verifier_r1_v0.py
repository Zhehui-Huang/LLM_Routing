import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Verify if tour starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify if 12 cities are visited (11 other cities + depot city)
    if len(set(tour)) != 12:
        return "FAIL"
    
    # Calculate the traveling cost and check
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_distance(*city_coordinates[city1], *city_coordinates[city2])
    
    # Check the rounded accuracy of cost up to 2 decimal places
    if round(calculated_cost, 2) != round(total_cost, 2):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Coordinates of the cities
city_coordinates = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Provided solution details
tour = [0, 1, 10, 13, 8, 14, 3, 6, 12, 4, 9, 5, 0]
total_cost = 251.16

# Check if the provided solution is correct
result = verify_solution(tour, total_cost, city_coordinates)
print(result)