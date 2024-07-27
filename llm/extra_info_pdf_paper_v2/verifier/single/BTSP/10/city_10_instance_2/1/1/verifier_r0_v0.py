import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def check_tour(tour, distances, total_cost, max_edge_cost):
    # Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once, excluding the depot city that should appear twice
    unique_cities = set(tour)
    if len(unique_cities) != 10 or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate total cost and maximum edge cost from the tour
    calculated_total_cost = 0
    calculated_max_edge_cost = 0
    
    for i in range(len(tour) - 1):
        distance = euclidean_distance(distances[tour[i]], distances[tour[i+1]])
        calculated_total cost += distance
        calculated_max_edge_cost = max(calculated_max_edge_cost, distance)
    
    # Check total travel cost and max edge cost with given values
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(calculated_max_edge_cost, max_edge_cost, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Cities coordinates
cities_coordinates = [
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

# Given solution details
tour = [0, 8, 5, 4, 7, 2, 1, 9, 6, 3, 0]
total_travel_cost = 384.7863591860825
maximum_distance_consecutive_cities = 78.63841300535

# Check validity of the solution
result = check_tour(tour, cities_coordinates, total_travel_cost, maximum_distance_consecutive_cities)
print(result)