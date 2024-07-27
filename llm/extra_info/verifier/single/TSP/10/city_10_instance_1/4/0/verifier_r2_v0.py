import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour_and_cost(tour, cost, cities):
    # Check Requirement 1 and 4: The tour starts and ends at city 0 and includes all cities exactly once
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    if sorted(tour[1:-1]) != sorted(range(1, len(cities))):
        return "FAIL"
    
    # Check Requirement 2 is inherently checked by the above conditions as both start and end should be 0
    
    # Check Requirement 3 and 5: Total tour cost calculation
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(computed_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates indexed by city number
cities = [
    (53, 68),  # Depot city 0
    (75, 11),  # City 1
    (91, 95),  # City 2
    (22, 80),  # City 3
    (18, 63),  # City 4
    (54, 91),  # City 5
    (70, 14),  # City 6
    (97, 44),  # City 7
    (17, 69),  # City 8
    (95, 89)   # City 9
]

# Provided solution
tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
total_cost = 278.9348447394249

# Verify the solution
result = verify_tour_and_cost(tour, total_cost, cities)
print(result)