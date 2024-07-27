import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_solution(cities_coords, tour, total_cost):
    # Requirement 1: Number of cities (checks indirectly via the tour length against city list)
    if len(cities_coords) != 15:
        return "FAIL: Number of cities is not 15."

    # Requirement 2: Starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start or end at the depot."

    # Requirement 3: Visit each city exactly once
    visited = set(tour)
    if len(visited) != len(cities_coords) or len(tour) - 1 != len(cities_coords):
        return "FAIL: Not all cities are visited exactly once."

    # Requirement 6: Check the tour structure
    if len(tour) < 2 or tour[0] != tour[-1]:
        return "FAIL: Tour structure is incorrect. It should start and end at the same city (depot)."
    
    # Requirement 5: Total travel cost calculation
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += euclidean_distance(cities_coords[tour[i]], cities_coords[tour[i+1]])

    if not math.isclose(total_cost, calculated_total_cost, rel_tol=1e-5):
        return f"FAIL: Calculated travel cost {calculated_total_batchet_cost:.2f} does not match provided total cost {total_cost:.2f}."

    # Additional check: If VISUAL or further logical validation is required
    print("All verifications passed with calculated travel cost: {:.3f}".format(calculated_total_cost))
    return "CORRECT"

# Cities' coordinates (Assuming these are coordinates from the description)
cities = [
    (9, 93),  # City 0 (Depot)
    (8, 51),  # City 1
    (74, 99), # City 2
    (78, 50), # City 3
    (21, 23), # City 4
    (88, 59), # City 5
    (79, 77), # City 6
    (63, 23), # City 7
    (19, 76), # City 8
    (21, 38), # City 9
    (19, 65), # City 10
    (11, 40), # City 11
    (3, 21),  # City 12
    (60, 55), # City 13
    (4, 39)   # City 14
]

# Provided solution details
tour_solution = [0, 3, 13, 11, 14, 12, 2, 6, 5, 7, 4, 9, 1, 10, 8, 0]
total_travel_cost_solution = 492.22910702149534

# Verify the solution
print(verify_tour_solution(cities, tour_solution, total_travel_cost_solution))