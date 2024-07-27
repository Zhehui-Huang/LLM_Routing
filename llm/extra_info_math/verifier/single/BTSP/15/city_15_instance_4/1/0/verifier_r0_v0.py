import math

# Provided solution
tour = [0, 8, 6, 3, 14, 13, 1, 10, 11, 4, 12, 5, 2, 7, 9, 0]
maximum_distance = 35.77708763999664

# Data points coordinates for each city, including the depot
coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Verify if the robot starts and ends at depot (city index 0)
def check_starts_ends_at_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if each city is visited exactly once, except the starting city
def check_all_cities_visited_once(tour):
    for city in range(1, 15):  # Check cities from 1 to 14
        if tour.count(city) != 1:
            return False
    return True

# Check if the reported maximum distance is correctly calculated
def check_maximum_distance(tour, reported_max_distance):
    max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        if distance > max_distance:
            max_distance = distance
    return math.isclose(max_distance, reported_max_distance, rel_tol=1e-5)

# Unit test execution
def run_unit_tests(tour, max_distance):
    if not check_starts_ends_at_depot(tour):
        return "FAIL"
    if not check_all_cities_visited_once(tour):
        return "FAIL"
    if not check_maximum_distance(tour, max_distance):
        return "FAIL"
    return "CORRECT"

# Run test and print the result
result = run_unit_tests(tour, maximum_distance)
print(result)