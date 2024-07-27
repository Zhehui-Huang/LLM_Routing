import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def validate_solution(tour, total_cost, max_distance):
    # City coordinates
    positions = [
        (50, 42), # depot city 0
        (41, 1),  # city 1
        (18, 46), # city 2
        (40, 98), # city 3
        (51, 69), # city 4
        (47, 39), # city 5
        (62, 26), # city 6
        (79, 31), # city 7
        (61, 90), # city 8
        (42, 49)  # city 9
    ]
    
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2]
    if sorted(tour) != [0, 0] + list(range(1, 10)):
        return "FAIL"

    # [Requirement 3] & [Requirement 5] & [Requirement 6] & [Requirement 7]
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        dist = euclidean_distance(*positions[city1], *positions[city2])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist

    calculated_total_cost = round(calculated_total_cost, 2)
    calculated_max_distance = round(calculated_max_distance, 2)

    # [Requirement 6]
    if calculated_total_cost != total_cost:
        return "FAIL"
    
    # [Requirement 7]
    if calculated_max_distance != max_distance:
        return "FAIL"
    
    return "CORRECT"

# Test the solution
test_tour = [0, 1, 5, 6, 7, 0, 2, 9, 4, 3, 8, 0]
test_total_cost = 288.16
test_max_distance = 49.24

result = validate_solution(test_tour, test_total_cost, test_max_distance)
print(result)