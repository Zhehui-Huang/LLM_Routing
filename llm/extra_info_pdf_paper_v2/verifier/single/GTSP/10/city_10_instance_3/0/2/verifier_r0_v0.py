import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

def validate_tour(tour, city_positions, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, "Tour must start and end at depot city 0."

    visited_cities = tour[1:-1]  # exclude depot at start and end

    # Each group should have exactly one city in the tour, excluding the depot
    visited_from_each_group = [False] * len(city_groups)
    for city in visited_cities:
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_from_each_group[i]:
                    return False, f"More than one city from group {i} visited."
                visited_from_each_group[i] = True

    if not all(visited_from_each_group):
        missing_groups = [i for i, visited in enumerate(visited_from_each_group) if not visited]
        return False, f"No city visited from groups {missing_groups}."

    return True, ""

def calculate_total_cost(tour, city_positions):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    return total_cost

def test_solution(tour, city_positions, city_groups, expected_cost):
    validation_result, message = validate_tour(tour, city_positions, city_groups)
    if not validation_result:
        return "FAIL: " + message
    
    calculated_cost = calculate_total_cost(tour, city_positions)
    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-5):
        return f"FAIL: Expected cost {expected_cost}, but got {calculated_cost}"

    return "CORRECT"

# Define the city positions and groups based on the task description
city_positions = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]
city_groups = [[7, 9], [1, 3], [4, 6], [8], [5], [2]]

# Define the tour and the expected travel cost
tour_provided = [0, 7, 1, 4, 8, 5, 2, 0]
expected_travel_cost = 324.18

# Perform the test
result = test_solution(tour_provided, city_positions, city_groups, expected_travel_cost)
print(result)