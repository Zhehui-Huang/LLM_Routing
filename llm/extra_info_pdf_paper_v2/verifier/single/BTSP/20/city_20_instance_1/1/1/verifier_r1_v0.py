import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, cities):
    # Extracting city coordinates
    city_coords = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
        5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
        10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
        15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
    }
    
    # [Requirement 1] Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Each city visited exactly once
    if len(tour) != len(cities) + 1 or len(set(tour)) != len(cities) + 1:
        return "FAIL"
    
    # Calculate total travel cost and the maximum distance
    total_travel_cost = 0
    maximum_distance = 0
    for i in range(1, len(tour)):
        dist = calculate_euclidean_distance(city_coords[tour[i-1]], city_coords[tour[i]])
        total_travel_cost += dist
        if dist > maximum_distance:
            maximum_distance = dist
    
    # [Requirement 3] Goal is to minimize the longest distance, yet no specific target given
    # So only checking requirements and computed details here:
    # [Requirement 6] Given total travel cost should match the calculated one
    # [Requirement 7] Given maximum distance between any two consecutive cities
    if math.isclose(total_travel_cost, 477.0516251264448) and math.isclose(maximum_distance, 87.45856161634491):
        # [Requirement 4] and [Requirement 5] implicitly checked by the tour and cost structures
        return "CORRECT"
    else:
        return "FAIL"

# Tour provided
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]

# Check the solution
result = verify_solution(tour, set(range(20)))  # Set of all cities including depot as 0
print(result)