import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def validate_tour(tour, groups, city_positions):
    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour does not start and end at the depot."
    
    # Check if tour visits exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the depot at the start and end
        for i, group in enumerate(groups):
            if city in group:
                if i in visited_groups:
                    return False, "Multiple cities visited from one group."
                visited_groups.add(i)
    
    if len(visited_groups) != len(groups):
        return False, "Not all groups are visited exactly once."
    
    return True, "All checks passed."

def calculate_total_travel_cost(tour, city_positions):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(city_positions[tour[i-1]], city_positions[tour[i]])
    return total_cost

city_positions = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

groups = [[2, 7, 10, 11, 14], [1, 3, 5, 8, 13], [4, 6, 9, 12]]

provided_tour = [0, 10, 1, 9, 0]
provided_cost = 122.22

# Check if the provided solution meets all specifications
is_valid, message = validate_tour(provided_tour, groups, city_positions)
if not is_valid:
    print("FAIL:", message)
else:
    calculated_cost = calculate_total_travel_cost(provided_tour, city_positions)
    if abs(calculated_cost - provided_cost) < 1e-2:
        print("CORRECT")
    else:
        print("FAIL: Calculated cost does not match provided cost. Calculated:", calculated_cost, "Provided:", provided_cost)