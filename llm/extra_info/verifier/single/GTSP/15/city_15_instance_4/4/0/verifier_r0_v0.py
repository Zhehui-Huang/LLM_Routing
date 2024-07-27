import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tsp_solution(tour, total_cost, city_coordinates, city_groups):
    # Check if the tour starts and ends at the depot city (city 0).
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if exactly one city from each group is visited.
    visited_groups = set()
    for city in tour[1:-1]:  # excluding the depot city at start and end
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
    if len(visited(group)) not 7:
        return "FAIL"

    # Calculate the total travel cost using Euclidean distance and compare with provided cost.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# City coordinates (index corresponds to city number)
city_coordinates = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# City groups
city_groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Tour and total travel cost provided
tour = [0, 5, 2, 7, 4, 6, 3, 10, 0]
total_cost = 244.73

# Call the testing function
result = test_tsp_solution(tour, total_cost, city_coordinates, city_groups)
print(result)