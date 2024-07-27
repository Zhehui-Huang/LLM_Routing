import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_solution():
    # City coordinates: city_index: (x, y)
    cities = {
        0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
        5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
        10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
        15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
    }

    # City groups and the solution
    city_groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]
    solution_tour = [0, 19, 6, 2, 13, 12, 18, 0]
    reported_cost = 158.65862319241174

    # Check if the tour starts and ends at the depot city (city 0)
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot city"

    # Check for exactly one city from each group
    visited_groups = [0] * len(city_groups)
    for city in solution_tour[1:-1]:  # Exclude starting and ending depot
        found_group = False
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i] == 1:
                    return f"FAIL: City {city} from group {i} is visited more than once"
                visited_groups[i] = 1
                found_group = True
                break
        if not found_group:
            return f"FAIL: City {city} does not belong to any required group"

    if not all(visited_groups):
        return "FAIL: Not all city groups are visited exactly once"

    # Check the total travel cost
    calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        city1 = solution_tour[i]
        city2 = solution_tour[i + 1]
        calculated_cost += calculate_euclidean_distance(cities[city1][0], cities[city1][1], cities[city2][0], cities[city2][1])

    # Check if the calculated travel cost is approximately equal to the reported cost
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-5):
        return f"FAIL: Calculated cost {calculated_cost} does not match reported cost {reported_cost}"

    return "CORRECT"

# Running the test function
output = test_solution()
print(output)