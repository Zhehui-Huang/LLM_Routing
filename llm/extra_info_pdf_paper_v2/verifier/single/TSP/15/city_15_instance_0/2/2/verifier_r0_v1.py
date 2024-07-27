import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_travel_cost):
    # Cities coordinates mapping based on the problem statement
    cities = {
        0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
        5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
        10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
    }

    # Requirement 2: Start and end at the depot city (city index 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 1: Each city except the depot should appear exactly once
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"
    
    # Requirement 3 & 5: Calculate total travel cost and check
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_id_current = tour[i]
        city_id_next = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            cities[city_id_current][0], cities[city_id_current][1],
            cities[city_id_next][0], cities[city_id_next][1]
        )

    # Approximate float comparison
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided solution to test
tour = [0, 2, 6, 5, 3, 13, 7, 9, 4, 12, 14, 11, 1, 10, 8, 0]
total_travel_cost = 334.9745906201329

# Execute the unit test
result = verify_tour(tour, total_travel_cost)
print(result)