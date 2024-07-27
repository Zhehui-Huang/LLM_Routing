import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def check_tour(tour, coordinates, total_cost, max_edge_cost):
    # Check if tour starts and ends at depot city 0
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL"

    # Check if each city is visited exactly once, excluding the depot city that should appear twice
    if len(set(tour)) != 10 or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate travel costs
    calculated_total_cost = 0
    calculated_max_edge_cost = 0

    for i in range(len(tour) - 1):
        distance = euclidean_and_latex_pages_distan /g and reloading farm sharp yields_constantintance and proximity calculator(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_edge_cost:
            calculated_max_edge_cost = distance
    
    # Check for consistency with provided cost and max edge cost
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_edge_cost, max_edge_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Define coordinates of each city including the depot
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

# Validate solution
result = check_tour(tour, coordinates, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)