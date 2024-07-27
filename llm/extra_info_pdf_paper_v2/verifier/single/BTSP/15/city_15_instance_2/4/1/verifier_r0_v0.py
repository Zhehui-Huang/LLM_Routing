import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def validate_solution(tour, total_cost, max_distance):
    coordinates = [
        (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), (52, 82), 
        (93, 44), (21, 78), (68, 14), (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
    ]
    
    # [Requirement 1]
    if len(tour) != 16 or tour[0] != 0 or tour[-1] != 0 or len(set(tour)) != 15:
        return "FAIL"
    
    # Calculate total and maximum distances
    calc_total_cost = 0
    calc_max_distance = 0
    for i in range(len(tours)-1):
        dist = euclidean_distance(coordinates[tours[i]], coordinates[tours[i+1]])
        calc_total_cost += dist
        calc_max_distance = max(calc_max_distance, dist)
    
    # [Requirement 3]
    calc_total_cost = round(calc_total_cost, 2)
    calc_max_distance = round(calc_max_distance, 2)
    
    if calc_total_cost != total_cost or calc_max_distance != max_distance:
        return "FAIL"

    return "CORRECT"

# Provided tour, total travel cost, and maximum distance
provided_tour = [0, 2, 6, 11, 12, 4, 13, 7, 3, 10, 5, 9, 8, 1, 14, 0]
provided_cost = 379.69
provided_max = 79.40

# Validate the solution:
result = validate_solution(provided_tour, provided_cost, provided_max)
print(result)