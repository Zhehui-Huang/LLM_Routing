import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def validate_tour(tour, total_cost, max_consecutive_distance):
    # Coordinates of the cities
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    # Requirement 1: Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if each city is visited exactly once (excluding the depot repeated at the end)
    if len(set(tour[:-1])) != len(cities):
        return "FAIL"
    
    # Compute the actual distances
    calculated_total_cost = 0
    calculated_max_consecutive_distance = 0
    for i in range(len(tour) - 1):
        current_dist = euclidean_distance(*cities[tour[i]], *cities[tour[i+1]])
        calculated_total_cost += current_dist
        if current_dist > calculated_max_consecutive_distance:
            calculated_max_consecutive_distance = current_dist

    # Requirement 3: Check the max consecutive distance
    if max_consecutive_distance != calculated_max_consecutive_distance:
        return "FAIL"

    # Requirement 4: Check the total distance
    if abs(calculated_total_cost - total_cost) >= 1:
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour_test = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
total_travel_cost_test = 379
maximum_distance_test = 68

# Validate the provided tour
result = validate_tour(tour_test, total_travel_cost_test, maximum_distance_test)
print(result)