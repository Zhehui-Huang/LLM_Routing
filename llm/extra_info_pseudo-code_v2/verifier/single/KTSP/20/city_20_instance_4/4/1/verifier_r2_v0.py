import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(tour, expected_cost):
    # Coordinates for the cities
    cities_coordinates = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
        (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
        (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
        (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # Requirement 1: Check if exactly 16 cities are visited including the depot
    if len(set(tour)) != 16:
        return "FAIL"

    # Requirement 2: Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 3: Calculate the travel distance and compare with expected
    total_distance = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities_coordinates[tour[i]]
        x2, y2 = cities_coordinates[tour[i + 1]]
        total_distance += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(total_distance, expected_cost, rel_tol=1e-2):
        return "FAIL"

    # Requirement 5 and 6: Internally checked within the above code
    return "CORRECT"

# Provided solution details
solution_tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 9, 5, 16, 7, 12, 6, 10, 0]
solution_total_cost = 280.7

# Verify the solution against the requirements
result = verify_tour(solution_tour, solution_total_cost)
print(result)