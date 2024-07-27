import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost):
    city_coordinates = {
        0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98),
        4: (51, 69), 5: (47, 39), 6: (62, 26), 7: (79, 31),
        8: (61, 90), 9: (42, 49)
    }
    city_groups = {
        0: [1, 2, 6], 
        1: [3, 7, 8], 
        2: [4, 5, 9]
    }
    
    # Check tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check exactly one city per group is visited
    visited_groups = {0: False, 1: False, 2: False}
    for index in tour[1:-1]:  # exclude the depot city at start and end
        group_found = False
        for group, cities in city_groups.items():
            if index in cities:
                if visited_groups[group]:
                    return "FAIL"
                visited_groups[group] = True
                group_found = True
                break
        if not group_found:
            return "FAIL"
    
    if not all(visited_groups.values()):
        return "FAIL"
    
    # Calculate total travel cost and verify
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i + 1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if abs(calculated_cost - total_cost) > 1e-5:
        return "FAIL"
    
    return "CORRECT"

# Test the function with provided sample solution
sample_tour = [0, 6, 7, 5, 0]
sample_total_cost = 74.94753083872993
result = verify_solution(sample_tour, sample_total_capture_cost)
print(result)