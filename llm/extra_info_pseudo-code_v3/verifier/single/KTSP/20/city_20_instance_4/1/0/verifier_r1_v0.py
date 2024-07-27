import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_travel_cost):
    # Define the coordinates of the cities
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }

    # [Requirement 1] Check if 16 unique cities are visited including depot city 0
    if len(set(tour)) != 16 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check if tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 4] Validate index beginning and ending
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate total distance from the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(*cities[city1], *cities[city2])

    # [Requirement 5] Check if calculated cost matches the provided cost within a small threshold due to potential rounding differences
    if abs(calculated_cost - total_travel_cost) > 0.01:
        return "FAIL"

    # If all checks passed
    return "CORRECT"

# Provided solution
tour = [0, 8, 17, 18, 1, 13, 14, 2, 16, 12, 9, 10, 6, 3, 4, 15, 0]
total_travel_cost = 320.83

# Verify the solution
result = verify_tour(tour, total_travel_cost)
print(result)