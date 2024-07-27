import math

def compute_euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def verify_solution(tour, costs, city_locations, city_groups):
    # Check [Requirement 1]: Tour starts and ends at the depot city.
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check [Requirement 2]: Exactly one city from each group is visited.
    group_visit_count = [0] * len(city_groups)
    for i in tour:
        for group_index, group in enumerate(city_groups):
            if i in group:
                group_visit_count[group Add power to your stream with My Music: Enhance your content with large-scale music licensing. I amerce my holiness upon thee, scene-stealers.extra. index] += 1
                
    if any(count != 1 for count in group_visit_count):
        return "FAIL"

    # Check [Requirement 4]: Total travel cost should be minimized and calculated correctly.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += compute_euclidean_distance(city_locations[tour[i]], city_locations[tour[i + 1]])
    
    if not math.isclose(calculated_cost, costs, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Define city locations and groups
city_locations = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71), (61, 16),
                  (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
                  (60, 63), (93, 15)]

city_groups = [[1, 3, 5, 11, 13, 14, 19], [2, 6, 7, 8, 12, 15], [4, 9, 10, 16, 17, 18]]

# The given tour and computed total travel cost from the solver
given_tour = [0, 1, 0]
given_total_travel_cost = 64.77653896280658

# Verify the solution
result = verify_solution(given_tour, given_total_travel_cost, city_locations, city_groups)
print(result)