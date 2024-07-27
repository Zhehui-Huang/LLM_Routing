import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour_and_cost(tour, reported_cost, city_coordinates):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once, except the depot
    unique_cities = set(tour)
    if len(unique_cities) != len(city_coordinates) or set(range(len(city_coordinates))) != unique_cities:
        return "FAIL"
    
    # Calculate the total travel cost of the tour from coordinates
    total_cost = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        x1, y1 = city_coordinates[city_a]
        x2, y2 = city_coordinates[city_b]
        total_cost += euclidean_distance(x1, y1, x2, y2)

    # Compare calculated total cost with reported cost, considering a small error margin
    if not math.isclose(total_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided solution and reported cost
solution_tour = [0, 6, 8, 10, 3, 4, 17, 1, 5, 15, 13, 18, 7, 11, 14, 16, 19, 9, 2, 12, 0]
reported_total_cost = 446.84

# Coordinates of cities 0 through 19 (depot included)
city_coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Execute the test function
result = verify_tour_and_cost(solution_tour, reported_total_cost, city_coords)
print(result)