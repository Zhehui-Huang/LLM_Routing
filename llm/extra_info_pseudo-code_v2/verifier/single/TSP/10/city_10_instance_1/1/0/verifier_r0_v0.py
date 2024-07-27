import math

def euclidean_distance(c1, c2):
    """Compute the Euclidean distance between two cities with coordinates c1 and c2."""
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Verify tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify all cities are visited exactly once, except depot which is visited twice
    unique_visits = set(tour)
    if len(tour) != len(cities) + 1 or unique_visits != set(range(len(cities))):
        return "FAIL"
    
    # Calculate the travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Compare the calculated travel cost with the given total_cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
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

# Provided solution's output
tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
total_cost = 278.9348447394249

# Verify the solution
result = verify_solution(tour, total, cities)
print(result)