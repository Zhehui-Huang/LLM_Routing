import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(tour, coordinates, total_cost, max_edge_cost):
    # Ensure tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once (excluding the depot, which should appear twice)
    if len(set(tour)) != 10 or tour.count(0) != 2:
        return "FAIL"
    
    # Compute total travel cost and maximum edge cost
    calculated_total_cost = 0
    calculated_max_edge_cost = 0

    for i in range(len(tour) - 1):
        distance = euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_total_cost += distance
        calculated_max_edge_cost = max(calculated_max_edge_cost, distance)
        
    # Validate computed cost and edge cost against provided values
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_edge_cost, max_edge_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Coordinates of each city including the depot
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Provided solution details
tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
total_travel_cost = 384.7863591860825
maximum_distance_between_consecutive_cities = 78.63841300535

# Run the validation test
verification_result = check_tour(tour, coordinates, total_travel_cost, maximum_distance_between_consecutive_cities)
print(verification_result)