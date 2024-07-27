import math

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def check_solution(tour, total_cost):
    solution_tour = [0, 12, 10, 4, 3, 2, 0]
    reported_cost = 138.15
    city_coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
                        (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
                        (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]
    city_groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]

    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 4]
    if tour != solution_tour:
        return "FAIL"

    # [Requirement 2]
    unique_cities = set(tour[1:-1])  # Exclude the depot city at start and end
    if len(unique_cities) != 5:
        return "FAIL"
    for group in city_essentials["groups"]:
        if not any(city in group for city in unique_cities):
            return "FAIL"

    # [Requirement 3] and [Requirement 5]
    calculated_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
                          for i in range(len(tour) - 1))
    if abs(reported_cost - total_cost) > 1e-2:
        return "FAIL"
    if abs(calculated_cost - total_cost) > 1e-2:
        return "FAIL"

    return "CORRECT"

# Given solution details
solution_tour = [0, 12, 10, 4, 3, 2, 0]
given_total_cost = 138.15

# Check the solution
result = check_solution(solution_tour, given_total_cost)
print(result)