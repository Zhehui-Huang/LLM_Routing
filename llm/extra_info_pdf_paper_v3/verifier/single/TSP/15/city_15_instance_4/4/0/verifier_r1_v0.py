import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_total_travel_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = coordinates[tour[i]]
        x2, y2 = coordinates[tour[i+1]]
        total_cost += euclidean_distance(x1, y1, x2, y2)
    return total_cost

def test_solution():
    # Coordinates for each city index
    coordinates = {
        0: (35, 40),
        1: (39, 41),
        2: (81, 30),
        3: (5, 50),
        4: (72, 90),
        5: (54, 46),
        6: (8, 70),
        7: (97, 62),
        8: (14, 41),
        9: (70, 44),
        10: (27, 47),
        11: (41, 74),
        12: (53, 80),
        13: (21, 21),
        14: (12, 39)
    }

    # Provided solution details
    tour = [0, 10, 8, 13, 14, 3, 6, 11, 12, 4, 7, 9, 2, 5, 1, 0]
    reported_total_cost = 306.76

    # Test if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test if all cities are visited exactly once, except depot (0)
    cities_visited = sorted(tour[1:-1])
    correct_cities = list(range(1, 15))
    if cities_visited != correct_cities:
        return "FAIL"

    # Calculate and check total cost
    calculated_total_cost = calculate_total_travel_cost(tour, coordinates)
    if not math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-2):
        return "FAIL"

    # Output the final result
    return "CORRECT"

# Run the test function and print the result
print(test_solution())