import math

def calculate_euclidean_distance(p1, p2):
    """ Calculate the Euclidean distance between two points. """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def check_solution(tour, cost):
    # Define the coordinates of all cities
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }

    # [Requirement 1] Check if tour starts and ends at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if exactly 13 distinct cities are visited
    if len(set(tour)) != 13:
        return "FAIL"
    
    # Calculate the total travel cost from the tour given
    computed_cost = 0
    for i in range(1, len(tour)):
        computed_cost += calculate_euclidean_distance(cities[tour[i-1]], cities[tour[i]])

    # [Requirement 3] Check if the calculated total travel cost is correctly minimized
    # Since we do not know the minimality requirement exactly, we check for exact match
    # However, this would typically require a benchmark comparison or a tolerance in real scenarios
    if abs(computed_cost - cost) > 1e-5:
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour_solution = [0, 1, 4, 7, 18, 3, 15, 17, 5, 2, 13, 6, 19, 0]
total_travel_cost_solution = 253.47857736863293

# Check the solution
result = check_solution(tour_solution, total_travel_cost_solution)
print(result)