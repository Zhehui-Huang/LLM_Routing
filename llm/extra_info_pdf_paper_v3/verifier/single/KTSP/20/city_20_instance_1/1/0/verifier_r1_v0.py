import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, reported_cost, city_coordinates):
    # Confirm that the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at city 0."
    
    # Confirm that exactly 7 cities are visited, including the depot
    if len(set(tour)) != 7 or len(tour) != 8:
        return "FAIL: Tour does not visit exactly 7 cities."

    # Calculate the total tour cost and compare with reported cost
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL: Total tour cost calculated as {:.2f}, reported as {:.2f}.".format(total_cost, reported_cost)

    # If all checks pass:
    return "CORRECT"

# City coordinates indexed from 0 to 19
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Tour and reported cost provided
tour = [0, 2, 13, 1, 15, 9, 14, 0]
reported_cost = 150.98

# Output the result of the validation
print(verify_solution(tour, reported_cost, city_coordinates))