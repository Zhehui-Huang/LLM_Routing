import numpy as np

def euclidean_distance(p1, p2):
    return round(np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2), 2)

def verify_tour(tour, total_cost, max_distance):
    cities_coordinates = [
        (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
        (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
    ]
    
    # Requirement 1 and Requirement 4
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2
    if sorted(tour) != sorted(list(range(len(cities_coordinates)))):
        return "FAIL"
    
    # Calculate total travel cost and maximum distance
    calculated_cost = 0
    calculated_max_dist = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(
            cities_coordinates[tour[i]], 
            cities_coordinates[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_dist:
            calculated_max_dist = dist
    
    # Requirement 3 is not verifiable with provided data alone.
    calculated_cost = round(calculated_cost, 2)
    calculated_max_dist = round(calculated_max_dist, 2)
    
    # Requirement 5
    if calculated_cost != total_cost:
        return "FAIL"
    
    # Requirement 6
    if calculated_max_dist != max_distance:
        return "FAIL"
    
    return "CORRECT"

# Given solution details
tour = [0, 8, 3, 9, 5, 6, 7, 1, 2, 4, 0]
total_cost = 345.92
max_distance = 68.26

# Verify the solution
result = verify_tour(tour, total_cost, max_distance)
print(result)