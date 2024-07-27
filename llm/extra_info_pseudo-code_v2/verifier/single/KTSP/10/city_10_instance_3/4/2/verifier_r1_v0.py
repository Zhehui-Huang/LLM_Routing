import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities):
    # Requirement 1: Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if exactly 7 cities are visited, including the depot
    if len(set(tour)) != 7:
        return "FAIL"

    # Calculate the total tour distance and check against provided total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    # Requirement 3 and 4: Check if the calculated distance matches the given total cost
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided cities coordinates
cities_coordinates = {
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

# Provided solution
tour = [0, 4, 1, 5, 6, 3, 0]
total_cost = 260.604277535237

# Check the provided tour and cost
result = verify_solution(tour, total_cost, [cities_coordinates[i] for i in sorted(cities_coordinates)])
print(result)