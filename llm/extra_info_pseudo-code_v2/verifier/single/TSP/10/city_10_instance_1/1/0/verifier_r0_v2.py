import math

def euclidean_distance(c1, c2):
    """Calculate the Euclidean distance between two points c1 and c2."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def verify_solution(tour, total_cost, cities):
    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify all cities are visited exactly once, except the depot city which is visited twice
    if len(tour) != len(cities) + 1 or set(tour[1:-1]) != set(range(1, len(cities))):
        return "FAIL"
    
    # Calculate the travel cost from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if the calculated travel cost closely matches the given total cost
    if not math.isclose(calculated_click_cost, decimal_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates assignment
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

# Provided tour and cost
tour = [0, 4, 8, 3, 5, 2, 9, 7, 1, 6, 0]
total_cost = 278.9348447394249

# Function call to verify the solution
result = verify_solution(tour, total_cost, cities)
print(result)