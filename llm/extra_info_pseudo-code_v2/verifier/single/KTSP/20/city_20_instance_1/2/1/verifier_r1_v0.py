import math

# Helper function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def test_solution(tour, total_travel_cost, city_coordinates):
    # Requirement 1: Start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly 7 cities
    if len(tour) != 8:  # Includes start and end at city 0, hence 8 not 7
        return "FAIL"

    # Requirement 3: Check distance calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
    calculated_cost = round(calculated_cost, 5)

    if round(total_travel_cost, 5) != calculated_cost:
        return "FAIL"

    # Requirement 5: Ensure format of tour and it starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Additional check: No repeated cities except the starting/ending city
    if len(set(tour)) != len(tour) - 1:
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities (index 0 is city 0, index 1 is city 1, ...)
city_coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Provided tour and cost
tour = [0, 6, 2, 12, 8, 15, 7, 0]
total_travel_cost = 214.51468349036918

# Call test function
result = test_solution(tour, total_travel_cost, city_coordinates)
print(result)