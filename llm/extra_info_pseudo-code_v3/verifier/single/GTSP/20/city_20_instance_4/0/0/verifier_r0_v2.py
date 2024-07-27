import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates, city_groups):
    # Check if the tour starts and ends at the depot (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group was visited.
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the start and end depot city
        for idx, group in enumerate(city_groups):
            if city in group:
                if idx in visited_groups:
                    return "FAIL"
                visited_idexes.append(index)

    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])

    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# City coordinates
city_coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2),
    (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25),
    (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Given solution
tour = [0, 8, 1, 11, 2, 5, 7, 10, 0]
total_travel_cost = 244.38839284908462

# Verify the given solution
result = verify_solution(tour, total_travel_cost, city_coordinates, city_groups)
print(result)