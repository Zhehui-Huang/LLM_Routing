import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost, city_coordinates):
    # Verify the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify that exactly 6 cities are visited
    if len(tour) != 7:  # This includes the return to the starting city
        return "FAIL"

    # Verify that no city except the depot is visited more than once
    if len(set(tour) - {0}) != len(tour) - 1:
        return "FAIL"

    # Verify correct calculation of the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not np.isclose(calculated_cost, total_cost, atol=0.05):
        return "FAIL"

    # If all checks are passed
    return "CORRECT"

# City coordinates as per the problem statement
city_coordinates = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Tour solution provided
tour = [0, np.int64(9), np.int64(1), np.int64(2), np.int64(5), np.int64(8), 0]
total_cost = 183.85

# Verify the solution
result = verify_solution(tour, total_cost, city_coordinates)
print(result)