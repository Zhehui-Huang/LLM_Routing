import math

# Define a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define cities coordinates
cities_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Provided solution details
tour = [0, 1, 5, 2, 9, 7, 0, 0, 0, 10, 3, 6, 8, 13, 14, 11, 12, 4, 0]
total_travel_cost = 433.8889882032202
max_distance = 32.449961479175904

# Unit Test to verify Requirement 1: Tour validation
def test_tour_validation(tour):
    # Checks if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return False
    # Creates a set of cities to visit (excluding the depot duplicates)
    cities_to_visit = set(range(len(cities_coordinates)))  # cities from 0 to 14
    visited_cities = set(tour) - {0}  # remove redundant 0s
    # Check if each city is visited exactly once
    return cities_to_visit == visited_cities

# Unit Test to verify Requirement 2: Correct calculation of travel cost
def test_total_travel_cost(tour, reported_cost):
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    return math.isclose(calculated_cost, reported_cost, rel_tol=1e-5)

# Unit Test to verify Requirement 3: Minimizing the maximum distance
def test_max_distance(tour, reported_max_distance):
    max_dist = 0
    for i in range(len(tour)-1):
        dist = euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
        if dist > max_dist:
            max_dist = dist
    return math.isclose(max_dist, reported_max_distance, rel_tol=1e-5)

# Run unit tests
if (test_tour_validation(tour) and
    test_total_travel_cost(tour, total_travel_cost) and
    test_max_distance(tour, max_distance)):
    print("CORRECT")
else:
    print("FAIL")