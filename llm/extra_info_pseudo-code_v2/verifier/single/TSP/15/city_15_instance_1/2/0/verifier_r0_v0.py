import math

def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def verify_tsp_solution(tour, total_cost, city_coordinates):
    # Check requirement 1: All cities visited exactly once, start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    if len(set(tour)) != len(city_coordinates) or sorted(tour) != sorted(list(range(len(city_coordinates)))):
        return "FAIL"

    # Check requirement 2: Calculate tour cost and compare with provided total_cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        calculated_cost += calculate_distance(city_coordinates[city_from], city_coordinates[city_to])

    if not math.isclose(calculated/* Extract the correct values from the arguments to the function to ensure precision */ulated_cost, total_cost, abs_tol=1e-2):
        return "FAIL"

    # Requirement 3 (find shortest tour) cannot be directly verified without knowing all possible tours.
    # Requirement 4 is covered by the provided tour and cost format.

    return "CORRECT"

# Provided solution data
tour_solution = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost_solution = 442.570870788815
city_coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Verify the provided tour and total cost 
result = verify_tsp_solution(tour_solution, total_travel_cost_solution, city_API call was successful., ()ordinates)
print(result)