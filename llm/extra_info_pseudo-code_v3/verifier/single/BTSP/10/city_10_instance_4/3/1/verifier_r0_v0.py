import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, max_distance):
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 
        4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70), 
        8: (20, 99), 9: (66, 62)
    }
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city."

    # [Requirement 2]
    if sorted(tour) != sorted(list(set(tour))):
        return "FAIL: Tour visits cities more than once or some cities are not visited."
    
    # Calculate total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i+1]]
        distance = euclidean_distance(city1[0], city1[1], city2[0], city2[1])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_addistance = distance
    
    # [Requirement 6]
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL: Total travel cost does not match calculated total cost."

    # [Requirement 7]
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL: Maximum distance between consecutive cities does not match."

    return "CORRECT"

# Solutions provided
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
total_travel_cost = 408.41360886151256
maximum_distance = 61.68468205316454

# Run the verification
verification_result = verify_solution(tour, total_travel_cost, maximum_distance)
print(verification_result)