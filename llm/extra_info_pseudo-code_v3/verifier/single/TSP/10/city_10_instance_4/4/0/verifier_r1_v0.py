import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def validate_solution(tour, total_cost, cities):
    # Requirement 2: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 3: Must visit all other cities exactly once
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(range(len(cities))) != unique_cities:
        return "FAIL"

    # Calculate and check the total travel cost
    calculated_cost = 0
    for i in range(1, len(tour)):
        city_a = cities[tour[i-1]]
        city_b = cities[tour[i]]
        calculated_cost += calculate_euclidean_distance(city_a[0], city_a[1], city_b[0], city_b[1])
    
    # Requirement 6: Check the provided total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-3):
        return "FAIL"
    
    # If all checks pass
    return "CORRECT"

# Defined cities as per the task description
cities = [
    (79, 15),  # City 0 - Depot
    (79, 55),  # City 1
    (4, 80),  # City 2
    (65, 26),  # City 3
    (92, 9),  # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)  # City 9
]

# Provided solution for verification
tour = [0, 0, 3, 6, 2, 8, 9, 1, 7, 5, 4, 0]
total_cost = 328.58

# Calling the validation function
result = validate_solution(tour, total_cost, cities)
print(result)