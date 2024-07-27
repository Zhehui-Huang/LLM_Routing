import math

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_tour():
    # City coordinates
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # Groups of cities
    groups = {
        0: [3, 8], 1: [4, 13], 2: [1, 2], 3: [6, 14], 4: [5, 9], 
        5: [7, 12], 6: [10, 11]
    }
    
    # Given Solution
    tour = [0, 13, 14, 8, 11, 12, 5, 1, 0]
    reported_cost = 156.56
    
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if one city from each group is visited
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.append(group_id)
                
    if len(visited_groups) != 7:
        return "FAIL"
    
    # Calculate and validate the total travel cost
    total_calculated_cost = 0
    for i in range(len(tour)-1):
        total_calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check against reported cost with a tolerance for floating-point precision
    if not math.isclose(total_calculated_cost, reported_cost, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Run test
print(test_tour())