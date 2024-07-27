import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, total_cost, max_dist):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Check if tour starts and ends at the depot, city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, excluding the depot which should be visited twice
    unique_cities = set(tour)
    if len(unique_cities) != 10 or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate the total distance and maximum distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist
    
    # Compare calculated and given values for total cost and max distance
    if not (math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9) and math.isclose(calculated_max_dist, max_dist, rel_tol=1e-9)):
        return "FAIL"
    
    # If all checks are passed
    return "CORRECT"

# Provided solution
tour = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
total_travel_cost = 379.3436985835247
maximum_distance_between_cities = 68.26419266350405

# Verify the solution
result = verify_tour(tour, total_travel_cost, maximum_distance_between_cities)
print(result)