import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
    
def test_solution():
    # Cities coordinates including the depot city
    cities = [
        (9, 93),  # Depot city 0
        (8, 51),
        (74, 99),
        (78, 50),
        (21, 23),
        (88, 59),
        (79, 77),
        (63, 23),
        (19, 76),
        (21, 38),
        (19, 65),
        (11, 40),
        (3, 21),
        (60, 55),
        (4, 39)
    ]

    # Proposed solution to test
    tour = [0, 1, 10, 8, 0]
    reported_total_cost = 90.53947981328088
    
    # Test requirement: There are 15 cities with designated coordinates including a depot city.
    if len(cities) != 15 or cities[0] != (9, 93):
        return "FAIL"

    # Test requirement: The robot starts and ends its route at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test requirement: The robot needs to visit exactly 4 cities.
    if len(tour) != 5:  # Includes the return to the depot
        return "FAIL"
    
    # Test requirement: The goal is to find the shortest possible tour that visits 4 cities starting and ending at the depot city.
    # Calculate the total travel cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Allow a small margin for floating-point arithmetic variations
    if not math.isclose(total_cost, reported_total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Running the test function
result = test_solution()
print(result)