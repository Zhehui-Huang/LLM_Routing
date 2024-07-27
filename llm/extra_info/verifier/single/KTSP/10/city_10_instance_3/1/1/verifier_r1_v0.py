import math

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)

def verify_solution(tour, cities):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly 7 cities are visited (including the depot)
    if len(set(tour)) != 8:
        return "FAIL"
    
    # Compute the total travel cost
    expected_cost = 159.97
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Allow a small floating point margin
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# Proposed solution tour and provided total cost
tour = [0, 4, 2, 1, 7, 3, 8, 0]
total_cost = 159.97

# Check the solution
result = verify_solution(tour, cities)
print(result)