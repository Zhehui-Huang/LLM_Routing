import math

def calculate_distance(city1, city2):
    """
    Calculates the Euclidean distance between two cities.
    """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(cities, tour, expected_cost):
    """
    Verifies whether the provided tour meets the problem requirements.
    """
    # Requirement: The robot starts and ends at the depot city which is city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement: The robot must visit exactly 7 cities, including the depot city.
    if len(set(tour)) != 7:
        return "FAIL"
    
    # Requirement: Provided city coordinates must be used to calculate Euclidean distances between cities for travel costs.
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    # Checking if the provided total travel cost is close enough to the calculated one.
    # Allowing a small margin for floating point arithmetic variations.
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates provided in the task description
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

# Provided tour and total travel cost
provided_tour = [0, 4, 2, 1, 7, 3, 8, 0]
provided_cost = 159.97188184793015

# Running the verification
print(verify_solution(cities_coordinates, provided_tour, provided_cost))