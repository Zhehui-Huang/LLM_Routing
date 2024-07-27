import math

# Data for cities' coordinates
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

# Provided solution
solution_tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]
solution_total_cost = 291.41
solution_max_distance = 56.61

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_solution(tour, total_cost, max_distance):
    # Check if starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities are visited exactly once except the depot city
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or not all(city in unique_cities for city in cities):
        return "FAIL"

    # Calculate total travel cost and max distance between consecutive cities
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i + 1])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Compare calculated and provided values
    if (round(calculated_total_cost, 2) != round(total_cost, 2) or
            round(calculated_max_distance, 2) != round(max_distance, 2)):
        return "FAIL"

    return "CORRECT"

# Testing the solution
test_result = verify_solution(solution_tour, solution_total_cost, solution_max_distance)
print(test_result)