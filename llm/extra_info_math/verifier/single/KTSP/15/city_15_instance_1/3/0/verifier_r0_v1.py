import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour_and_cost(tour, total_travel_cost):
    # Coordinates of cities
    coordinates = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    
    # [Requirement 1] Check if the tour includes exactly 6 cities, starting and ending at the depot city
    if len(tour) != 7 or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if cities are visited once, except for the depot city
    if len(set(tour)) != 7 or tour.count(0) != 2:
        return "FAIL"

    # [Requirement 3] Validate the total cost is minimal and correctly calculated
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        calculated_cost += calculate_euclidean_distance(*coordinates[city1], *coordinates[city2])

    if not math.isclose(total_travel_cost, calculated_path_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Provided solution details
tour = [0, 6, 1, 7, 3, 9, 0]
total_travel_cost = 118.90

# Run the test
print(validate_tour_and_cost(tour, total_travel_cost))