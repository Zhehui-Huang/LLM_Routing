import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, cost, cities):
    # Verify Requirement 4: Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify Requirement 1: Check if all cities are visited exactly once
    if sorted(tour[1:-1]) != list(range(1, len(cities))):
        return "FAIL"
    
    # Verify Requirement 2 & 5: Calculate the total travel cost and verify it
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_index1 = tour[i]
        city_index2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city_index1][0], cities[city_index1][1], cities[city_index2][0], cities[city_index2][1])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City coordinates (including the depot city at index 0)
cities_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32), (25, 71),
    (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# Given tour and total cost
provided_tour = [0, 4, 1, 8, 13, 17, 5, 19, 6, 2, 10, 3, 18, 15, 11, 9, 12, 7, 14, 16, 0]
provided_total_cost = 349.6816774069448

# Run the verification
result = verify_tour_and_cost(provided_tour, provided_total_cost, cities_coordinates)
print(result)