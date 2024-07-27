import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, expected_cost):
    cities = [
        (79, 15),  # Depot City 0
        (79, 55),  # City 1
        (4, 80),   # City 2
        (65, 26),  # City 3
        (92, 9),   # City 4
        (83, 61),  # City 5
        (22, 21),  # City 6
        (97, 70),  # City 7
        (20, 99),  # City 8
        (66, 62)   # City 9
    ]
    
    # Verify number of cities is 10
    if len(cities) != 10:
        return "FAIL"
    
    # Verify the tour starts and ends at the depot city and visits all cities exactly once
    if tour[0] != 0 or tour[-1] != 0 or sorted(tour[1:-1]) != list(range(1,10)):
        return "FAIL"

    # Calculate the total travel cost of the provided tour
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = cities[tour[i]]
        x2, y2 = cities[tour[i + 1]]
        total_cost += calculate_euclidean_distance(x1, y1, x2, y2)

    # Allow a small margin of error in floating point comparison
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# Provided solution
tour = [0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_travel_cost = 328.58208011724435

# Checking the solution
result = verify_solution(tour, total_travel_cost)
print(result)