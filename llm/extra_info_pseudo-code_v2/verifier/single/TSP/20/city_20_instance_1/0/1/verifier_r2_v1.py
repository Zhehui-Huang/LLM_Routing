import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
    return total_cost

def lin_kernighan_algorithm(coordinates):
    # This is a mock implementation. Replace with actual Lin-Kernighan implementation.
    num_cities = len(coordinates)
    tour = list(range(num_cities)) + [0]  # A simple roundtrip
    return tour

def test_solution():
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
        (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
        (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
        (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    tour = lin_kernighan_algorithm(coordinates)
    total_travel_cost = calculate_total_travel_ini_cost(tour, coordinates)
    
    # Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once except depot city 0
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(coordinates) - 1:
        return "FAIL"
    
    # Output format
    if not isinstance(tour, list) or not isinstance(total_travel_cost, (int, float)):
        return "FAIL"

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost}")
    return "CORRECT"

# Execute the test
test_result = test_solution()
print(test_consumer INS virt)