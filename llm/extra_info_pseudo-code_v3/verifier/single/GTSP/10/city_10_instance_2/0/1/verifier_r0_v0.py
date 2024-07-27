import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, groups, city_locations):
    # Check if the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False

    # Extract visited cities excluding the depot
    visited_cities = tour[1:-1]

    # Check for exactly one city from each group
    visited_from_groups = []
    for group in groups:
        count = sum(1 for city in visited_cities if city in group)
        if count != 1:
            return False
        visited_from_groups.extend([city for city in visited_cities if city in group])

    # Check if all visited cities are unique
    if len(visited_from_groups) != len(set(visited_from_groups)):
        return False

    # Calculate the total travel cost
    calculated_cost = 0
    current_city_idx = tour[0]
    for next_city_idx in tour[1:]:
        current_city = city_locations[current_city_idx]
        next_city = city_locations[next_city_idx]
        calculated_cost += euclidean_distance(current_city, next_city)
        current_city_idx = next_city_idx

    return calculated_cost

# Test inputs
city_locations = [(90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35), (23, 95), (20, 56), (49, 29), (13, 17)]
groups = [[3, 6], [5, 8], [4, 9], [1, 7], [2]]
solution_tour = [0, 3, 5, 9, 1, 2, 0]
solution_cost = 281.6  # As provided, to be manually checked if correct

# Validate the tour and cost
calculated_cost = validate_tour(solution_tour, groups, city_locations)
if calculated_cost and abs(calculated_cost - solution_cost) < 1e-3:
    print("CORRECT")
else:
    print("FAIL")