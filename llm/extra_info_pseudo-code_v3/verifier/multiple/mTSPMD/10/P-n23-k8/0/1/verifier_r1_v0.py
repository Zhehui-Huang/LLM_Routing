import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_solution():
    # Provided city coordinates
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
        20: (45, 35), 21: (32, 39), 22: (56, 37)
    }
    
    # Provided tour
    tour = [0, 21, 9, 17, 20, 14, 22, 13, 10, 8, 15, 11, 12, 19, 18, 16, 0]
    reported_cost = 242.0990837380884
    
    # Check if tour starts and ends at same depot
    if tour[0] != tour[-1]:
        return "FAIL"
    
    # Check if each city is visited exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1:
        return "FAIL"
    
    # Calculate the total cost
    total_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    # Check if the reported total cost is roughly equal to the calculated cost (allowing for small floating-point differences)
    if not math.isclose(total_cost, reported_constraint_cost, rel_tol=1e-9):
        return "FAIL"
    
    # If all tests pass
    return "CORRECT"

# Run the test
print(test_solution())