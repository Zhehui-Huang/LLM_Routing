import math

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution():
    cities_coordinates = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }

    given_tour = [0, 9, 5, 6, 0]
    given_total_cost = 61.66

    # [Requirement 1] Check for 10 cities
    if len(cities_coordinates) != 10 or any(c not in cities_coordinates for c in range(10)):
        return "FAIL"

    # [Requirement 2] Start at city 0 and visit exactly 4 cities total, including city 0
    if len(given_tour) != 5 or given_tour[0] != 0 or given_tour[-1] != 0:
        return "FAIL"

    # [Requirement 3] Tour begins and ends at the depot city
    if given_tour[0] != 0 or given_tour[-1] != 0:
        return "FAIL"

    # [Requirement 4] Itinerary exactly 5 segments: 0, three other cities, 0
    if any(city not in cities_coordinates for city in given_tour):
        return "FAIL"

    # [Requirement 5] Calculate the travel cost and compare with given
    calculated_cost = 0
    for i in range(len(given_tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[given_tour[i]], cities_coordinates[given_tour[i + 1]])

    calculated_cost = round(calculated_cost, 2)
    if calculated_cost != given_total_cost:
        return "FAIL"

    return "CORRECT"

# Run the verification function
result = verify_solution()
print(result)