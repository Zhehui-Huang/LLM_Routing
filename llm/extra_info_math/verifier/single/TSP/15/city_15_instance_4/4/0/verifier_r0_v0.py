import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    cities = [
        (35, 40),  # depot city 0
        (39, 41),
        (81, 30),
        (5, 50),
        (72, 90),
        (54, 46),
        (8, 70),
        (97, 62),
        (14, 41),
        (70, 44),
        (27, 47),
        (41, 74),
        (53, 80),
        (21, 21),
        (12, 39)
    ]
    
    tour = [0, 1, 5, 9, 2, 7, 4, 12, 11, 6, 3, 8, 14, 13, 10, 0]
    reported_cost = 284.40117604696553

    # Check if starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except depot city 0
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or any(i not in visited for i in range(1, len(cities))):
        return "FAIL"
    
    # Check the travel cost calculation
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Tolerance for floating point comparison
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())