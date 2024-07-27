import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def check_tour(tour, coordinates):
    # Check if starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    # Check each city is visited exactly once, except the depot (0) which needs to appear twice
    unique_cities = set(tour)
    if len(unique_cities) != 10 or tour.count(0) != 2:
        return "FAIL"
    # Check to ensure cities from 1 to 9 appear exactly once
    for city in range(1, 10):
        if tour.count(city) != 1:
            return "FAIL"
    # Calculate and check all distances
    max_distance_calculated = 0
    total_distance_calculated = 0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        distance = euclidean_distance(*coordinates[city1], *coordinates[city2])
        total_distance_calculated += distance
        if distance > max_distance_calculated:
            max_distance_calculated = distance
    
    # Compare calculated values with provided values
    proposed_max_distance = 45.18849411078001
    proposed_total_distance = 299.22080186207336
    if not math.isclose(max_distance_calculated, proposed_max_distance, rel_tol=1e-5):
        return "FAIL"
    if not math.isclose(total_distance_calculated, proposed_total_distance, rel_tol=0.01):
        return "CORRECT"

# Provided solution data
tour_solution = [0, 7, 6, 1, 5, 2, 4, 3, 8, 9, 0]
coordinates = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Execute the verification
print(check_tour(tour_solution, coordinates))