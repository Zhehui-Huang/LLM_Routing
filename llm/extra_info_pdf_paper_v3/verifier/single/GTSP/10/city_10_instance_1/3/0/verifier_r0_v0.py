import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates, groupings):
    # Check start and end at the depot city, i.e., city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check one city from each group is visited
    visited_groups = set()
    for city_index in tour:
        for group_index, group in enumerate(groupings):
            if city_index in group:
                visited_groups.add(group_index)
    if len(visited_groups) != len(groupings):
        return "FAIL"

    # Compute and check the total travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(city_coordinates[city1], city_coordinates[city2])

    # Check if the computed cost is approximately equal to the provided total cost
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=1e-6):
        return "FAIL"

    return "CORRECT"

# City coordinates
city_coordinates = {
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

# Groupings
groupings = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Solution tour and total travel cost
solution_tour = [0, 9, 5, 3, 8, 0]
solution_total_travel_cost = 169.9409598467532

# Perform verification
result = verify_solution(solution_tour, solution_total_travel_cost, city_coordinates, groupings)
print(result)