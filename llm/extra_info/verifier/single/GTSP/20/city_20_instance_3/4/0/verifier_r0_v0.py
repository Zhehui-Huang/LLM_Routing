import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    # City coordinates
    city_coordinates = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
        (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), 
        (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
        (53, 76), (19, 72)
    ]

    # City groups
    city_groups = [
        [4, 10, 13, 17],
        [6, 7, 14],
        [9, 12, 16],
        [2, 5, 15],
        [1, 3, 19],
        [8, 11, 18]
    ]

    # Verify requirement 1: Tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify requirement 2: Tour contains exactly one city from each group
    groups_visited = {}
    for i in range(6):
        groups_visited[i] = 0
    
    for city in tour[1:-1]:
        for group_id, group in enumerate(city_groups):
            if city in group:
                groups_visited[group_id] += 1
    
    if any(count != 1 for count in groups_visited.values()):
        return "FAIL"

    # Verify requirement 3: Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_1 = city_coordinates[tour[i]]
        city_2 = city_coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(city_1, city_2)
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Given solution output and total cost
output_tour = [0, 19, 6, 2, 13, 12, 18, 0]
output_cost = 158.65862319241174

# Call verification function
result = verify_solution(output_tour, output_cost)
print(result)