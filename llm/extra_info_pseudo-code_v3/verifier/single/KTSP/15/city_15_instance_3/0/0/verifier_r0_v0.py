import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two points (x1, y1) and (x2, y2). """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, tour, reported_cost):
    # Define city coordinates
    city_coordinates = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    
    # Check number of cities
    if len(city_coordinates) != 15:
        return "FAIL"
    
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour visits exactly 10 cities including the depot
    if len(tour) != 11:
        return "FAIL"
    
    # Calculate travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        if tour[i] not in city_coordinates or tour[i+1] not in city_coordinates:
            return "FAIL"  # Invalid city in tour
        total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    
    # Check if travel cost is correct
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-3):
        return "FAIL"
    
    # Check if all indices in tour are unique except for the starting and ending city
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 9:
        return "FAIL"
    
    return "CORRECT"

# Provided example solution
tour = [0, 14, 5, 9, 4, 10, 8, 6, 13, 0]
reported_cost = 182.82

# Call the verification function with the provided solution
result = verify_solution(city_coordinates=None, tour=tour, reported_cost=reported_cost)
print(result)  # Expected output: "CORRECT" assuming all checks pass or "FAIL" if any check fails