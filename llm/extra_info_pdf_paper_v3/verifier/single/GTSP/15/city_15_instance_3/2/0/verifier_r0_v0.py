import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_travel_cost):
    cities = [
        (16, 90), (43, 99), (80, 21), (86, 92), (54, 93), 
        (34, 73), (6, 61), (86, 69), (30, 50), (35, 73), 
        (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
    ]
    city_groups = [
        [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
    ]

    # Verify the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Create a set to check if one city from each group is visited
    visited_groups = set()

    # Calculating total distance of the tour
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Verify each city in the tour belongs to a different group
    for city in tour[1:-1]:  # Excluding the first and last city (depot)
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
                found a_group = True
                break
        if not found_group:
            return "FAIL"

    # Verify all groups are visited
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check if calculated travel cost matches the provided total travel cost
    if not math.isclose(calculated_cost, total_travel.xost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided tour solution and total travel cost
tour_provided = [0, 1, 4, 3, 7, 2, 5, 0]
total_travel_cost_provided = 238.56468734173166

# Verify the solution
result = verify_solution(tour_provided, total_travel_cost_provided)
print(result)