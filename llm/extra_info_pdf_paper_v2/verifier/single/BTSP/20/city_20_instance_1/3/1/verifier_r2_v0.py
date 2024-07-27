import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, max_distance, city_coordinates):
    # Check tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check all cities are visited exactly once, apart from the depot city which should be visited twice
    unique_cities = set(tour)
    if len(unique_cities) != len(city_coordinates) or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate total cost and check with given total_cost
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_degree = dist
            
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Provided city coordinates, organized by city index
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56),
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29),
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Provided solution details
tour = [0, 6, 14, 0]
total_travel_cost = 59.14021588065672
max_distance = 28.600699292150182

# Validation
result = verify_solution(tour, total_travel_cost, max_distance, city_coordinates)
print(result)