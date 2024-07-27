import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, travel_cost, max_distance):
    # Coordinates of each city
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), 
        (45, 84), (4, 56), (54, 82), (37, 28), (27, 45), 
        (90, 85), (98, 76), (6, 19), (26, 29), (21, 79), 
        (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # Requirements for the unit tests
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: The tour does not start and end at the depot city 0."
    
    if len(set(tour)) != len(coordinates) or len(tour) != len(coordinates) + 1:
        return "FAIL: The tour must visit each city exactly once plus return to the depot."
    
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
        calculated_cost += dist
        calculated_max_distance = max(calculated_max_distance, dist)
    
    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-2):
        return f"FAIL: The calculated total travel costs {calculated_cost} does not match provided {travel_cost}."
    
    if not math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2):
        return f"FAIL: The calculated maximum distance {calculated_max_distance} does not match provided {max_distance}."
    
    return "CORRECT"

# Example output provided
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
total_travel_cost = 477.05
maximum_distance_between_consecutive_cities = 87.46

# Call the verification function
result = verify_solution(tour, total_travel_cost, maximum_distance_between_consecutive_cities)
print(result)