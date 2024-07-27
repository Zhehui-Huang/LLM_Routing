import math

# Define the cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

def calculate_distance(city1, city2):
    """Calculates Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def validate_solution(tour, reported_cost):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city (except depot) is visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != 9 or any(city not in visited for city in range(1, 10)):
        return "FAIL"

    # Check if the output contains the starting and ending city as depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total travel cost and compare with the reported cost
    actual_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(actual_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Test the provided solution
tour = [0, 3, 6, 2, 8, 9, 1, 5, 7, 4, 0]
reported_cost = 320.79
result = validate_solution(tour, reported_cost)
print(result)