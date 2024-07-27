import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, cost):
    # Coordinates of cities, ordered by city index
    coordinates = [
        (8, 11), (40, 6), (95, 33), (80, 60), (25, 18),
        (67, 23), (97, 32), (25, 71), (61, 16), (27, 91),
        (91, 46), (40, 87), (20, 97), (61, 25), (5, 59),
        (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
    ]

    # Define city groups
    group_0 = [1, 3, 5, 11, 13, 14, 19]
    group_1 = [2, 6, 7, 8, 12, 15]
    group_2 = [4, 9, 10, 16, 17, 18]

    # Verify start and end city
    if tour[0] != 0 or tour[-1] != 0:
        print("FAIL")
        return

    # Check inclusion of one city from each group
    found_group_0 = any(city in group_0 for city in tour)
    found_group_1 = any(city in group_1 for city in tour)
    found_group_2 = any(city in group_2 for city in tour)
    if not (found_group_0 and found_group_1 and found_group_2):
        print("FAIL")
        return

    # Calculate and verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(x1, y1, x2, y2)

    # Comparing the float costs with a tolerance to handle floating point arithmetic issues
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        print("FAIL")
        return

    print("CORRECT")

# Solution to validate
tour = [0, 1, 8, 4, 0]
total_travel_cost = 110.09

# Call the verification function
verify_solution(tour, total_travel_cost)