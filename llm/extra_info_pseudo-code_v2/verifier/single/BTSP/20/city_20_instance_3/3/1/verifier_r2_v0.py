import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def test_solution():
    coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]

    tour = [0, 3, 19, 6, 13, 2, 15, 17, 16, 9, 5, 1, 10, 11, 4, 7, 18, 12, 14, 8, 0]
    expected_total_cost = 576.00
    expected_max_distance = 78.39

    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
        
    # Requirement 2
    unique_cities = set(tour)
    if len(unique_cities) != len(coordinates) + 1:  # Considering the depot is visited twice
        return "FAIL"
        
    # Requirement 3 and 7
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
            
    if not (abs(total_cost - expected_total_cost) < 1e-2 and abs(max_distance - expected_max_distance) < 1e-2):
        return "FAIL"
    
    # If all tests pass
    return "CORRECT"

# Execute the testing function
result = test_solution()
print(result)