import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def check_tour(test_tour, cities):
    if len(set(test_tour)) != len(cities):
        return "FAIL"
    if test_tour[0] != 0 or test_tour[-1] != 0:
        return "FAIL"
    for city in range(1, len(cities)):
        if city not in test_tour:
            return "FAIL"
    return "CORRECT"

def verify_max_distance(test_tour, cities, expected_max_distance):
    max_distance = 0
    for i in range(1, len(test_tour)):
        dist = calculate_distance(cities[test_tour[i-1]], cities[test_tour[i]])
        if dist > max_distance:
            max_distance = dist
    if max_distance > expected_max_distance:
        return "FAIL"
    return "CORRECT"

def unit_test_solution():
    cities = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
        6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
        12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    test_tour = [0, 10, 4, 9, 13, 1, 7, 3, 6, 14, 8, 11, 12, 2, 5, 0]
    expected_max_dist = 50.21951811795888

    # Check requirements
    check1_result = check_tour(test_tour, cities)
    max_dist_result = verify_max_distance(test_tour, cities, expected_max_dist)
    
    # Combine results
    if check1_result == "CORRECT" and max_dist_result == "CORRECT":
        return "CORRECT"
    else:
        return "FAIL"

# Running the unit test to verify the solution
output = unit_test_solution()
print(output)