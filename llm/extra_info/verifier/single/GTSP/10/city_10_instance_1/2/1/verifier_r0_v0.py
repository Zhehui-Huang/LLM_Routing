import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tsp_solution():
    # Given data:
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
    
    groups = {
        0: [5, 6, 7],
        1: [2, 3],
        2: [1, 9],
        3: [4, 8]
    }
    
    solution_tour = [0, 5, 2, 9, 8, 0]
    reported_cost = 183.99

    # Verify the tour starts and ends at the depot:
    if solution_tour[0] != 0 or solution_tour[-1] != 0:
        return "FAIL"
    
    # Check if the tour visits exactly one city from each group:
    visited_groups = set()
    for i in range(1, len(solution_tour) - 1):  # exclude the depot in the start and end
        city = solution_tour[i]
        for group_id, group_cities in groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                else:
                    visited_groups.add(group_id)
                    break

    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Calculate the total travel cost:
    total_calculated_cost = 0
    for i in range(len(solution_tour) - 1):
        city_from = solution_tour[i]
        city_to = solution_tour[i + 1]
        total_calculated_cost += calculate_distance(cities[city_from], cities[city_to])
    
    # Check if the reported travel cost is correct:
    if not math.isclose(total_calculated_cost, reported_cost, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Run the test
print(test_tsp_solution())