import math

# Test data setup
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Proposed solution to test
tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 14, 8, 7, 12, 18, 0]
proposed_total_cost = 428.08321234909306

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Requirement checks
def test_solution():
    # Check start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check visiting all cities exactly once
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != len(cities) - 1 or not all(city in unique_cities for city in cities if city != 0):
        return "FAIL"
    
    # Check output format and total travel cost calculation
    calculated_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    if not math.isclose(calculated_cost, proposed_total_cost, rel_tol=1e-6):
        return "FAIL"
    
    # If all tests pass
    return "CORRECT"

# Run the test
print(test_solution())