from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution():
    cities = {0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 6: (79, 77), 
              7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)}
    tour = [0, 1, 11, 10, 0]
    reported_cost = 109.39

    # Check number of cities
    if len(cities) != 15:
        return "FAIL"

    # Check depot city
    if cities[0] != (9, 93):
        return "FAIL"

    # Check tour starting and ending at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if tour visits exactly 4 cities
    if len(tour) != 5:
        return "FAIL"

    # Calculate and check the total travel cost
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])

    if abs(total_cost - reported_cost) > 0.01:  # Allowing some small floating point error margin
        return "FAIL"

    # If all checks pass
    return "CORRECT"

# Run the check
result = check_solution()
print(result)