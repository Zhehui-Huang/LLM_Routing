import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, travel_cost):
    # Cities coordinates (including depot as city 0)
    coordinates = [
        (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
        (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
        (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # [Requirement 2] Check if exactly 7 distinct cities are visited (including depot)
    visited_cities = set(tour)
    if len(visited_cities) != 7:
        return False

    # [Requirement 4] Check if the tour indeed starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Calculate the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(
            coordinates[city_a][0], coordinates[city_a][1], 
            coordinates[city_b][0], coordinates[city_b][1]
        )

    # [Requirement 5] Check if the calculated travel cost matches the given travel cost
    if not math.isclose(calculated_cost, travel_cost, rel_tol=1e-9):
        return False

    # If all validations pass
    return True

# Provided solution details
provided_tour = [0, 14, 7, 9, 2, 6, 0, 0]
provided_cost = 143.54042444291807

# Validate the provided solution
if validate_tour(provided_tour, provided_cost):
    print("CORRECT")
else:
    print("FAIL")