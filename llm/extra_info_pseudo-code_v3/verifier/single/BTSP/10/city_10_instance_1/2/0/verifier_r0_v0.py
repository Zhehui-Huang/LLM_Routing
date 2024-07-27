import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, travel_cost, max_distance):
    # City coordinates
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }

    # Checking if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city except the depot is visited exactly once
    if sorted(tour[1:-1]) != sorted(list(cities.keys())[1:]):
        return "FAIL"

    # Check if the travel cost and maximum distance between consecutive cities are correct
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Compare calculated costs to provided values
    if not (math.isclose(calculated_total_cost, travel_cost, rel_tol=1e-2) and
            math.isclose(calculated_max_distance, max_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
total_travel_cost = 291.41
maximum_distance = 56.61

# Verify the solution
result = verify_solution(tour, total_travel_cost, maximum_distance)
print(result)