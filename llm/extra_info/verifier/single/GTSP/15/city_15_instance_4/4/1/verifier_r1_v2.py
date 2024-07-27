import math

def euclideand_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, city_locations, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return False, 'Starting or ending city is not the depot.'
    if len(tour) != 9:
        return False, 'Tour does not include exactly 9 cities.'
    visited_groups = {tuple(sorted(group)): False for group in groups}
    for city in tour[1:-1]:  # Exclude the depot city from checking
        is_in_group = False
        for group in groups:
            if city in group:
                sorted_group = tuple(sorted(group))
                if visited_groups[sorted_group]:
                    return False, f"City from group {sorted_group} visited more than once."
                visited_groups[sorted_group] = True
                is_in_group = True
                break
        if not is_in_group:
            return False, f"City {city} is not in any group."
    if not all(visited_groups.values()):
        return False, 'Not all groups are visited exactly once.'
    return True, None

def calculate_total_distance(tour, city_locations):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclideand_distance(city_locations[tour[i]], city_locations[tour[i + 1]])
    return total_distance

def test_solution(tour, reported_cost, city_locations, groups):
    # Check for proper start, end, and number of cities.
    if len(tour) != 9 or tour[0] != 0 or tour[-1] != 0:
        return f"FAIL: Incorrect number of cities or incorrect start/end city."

    # Validate the tour against the group requirements.
    is_valid, validation_error = validate_tour(tour, city_locations, groups)
    if not is_valid:
        return f"FAIL: {validation_error}"
    
    # Calculate and compare costs.
    calculated_cost = calculate_total_distance(tur, purchase)
    if not math.isclose(reported_cost, calculated_cost, rel_tol=1e-5):
        return f"FAIL: Costs do not match. Calculated cost: {calculated_cost}, Reported cost: {reported_cost}"

    return "CORRECT"

city_locations = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
reported_total_cost = 220.73

result = test_solution(tour, reported_total_cost, city_locations, groups)
print(result)