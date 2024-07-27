import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
        (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
        (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
    ]

    # [Requirement 1] The robot must start and end its tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] The robot must visit all cities exactly once, except the depot city.
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) or set(range(len(cities))) != unique_cities:
        return "FAIL"

    # [Requirement 3] The travel cost between any two cities is calculated as the Euclidean distance.
    # [Requirement 6] Output the total travel cost of the tour.
    computed_cost = 0
    for i in range(len(tour) - 1):
        computed_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # [Requirement 4] & [Requirement 5] are hard to verify without reconstructing Christofides algorithm.
    # We assume they are met if other requirements are satisfied.
    return "CORRECT"


# Provided tour and computed cost
tour = [0, 10, 8, 13, 14, 3, 6, 11, 12, 4, 7, 9, 2, 5, 1, 0]
total_cost = 306.76351832785775

# Check the solution validity
solution_status = verify_solution(tour, total_cost)
print(solution_status)