import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_solution(tour, total_cost, max_distance):
    cities = [
        (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
        (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
        (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
        (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
    ]
    
    # Check if tour starts and ends at the depot (Requirement 1 and Requirement 5)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities (except depot visited twice) are visited exactly once (Requirement 2)
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Calculate the actual travel cost and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check if the total cost and maximum distance are correct (Requirement 6 and Requirement 7)
    if not math.isclose(total_cost, calculated_total_cost, abs_tol=1e-2):
        return "FAIL"
    if not math.isclose(max_distance, calculated_max_distance, abs_tol=1e-2):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Test the solution
result = test_solution(
    tour=[0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 5, 1, 17, 4, 3, 10, 8, 6, 9, 2, 0],
    total_cost=478.43,
    max_distance=80.61
)
print(result)