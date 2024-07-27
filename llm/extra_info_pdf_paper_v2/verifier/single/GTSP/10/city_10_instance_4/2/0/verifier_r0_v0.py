import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, city_groups, cities):
    # Check starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Create a set to check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude the starting and ending depot city
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
                break

    # Check if all groups are visited
    if len(visited/k_groups) != len(city_groups):
        return "FAIL"

    # Check if the travel cost calculation is correct
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(total_calculated_cost, 279.0156928434315, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Provided information
cities = {
    0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26),
    4: (92, 9), 5: (83, 61), 6: (22, 21), 7: (97, 70),
    8: (20, 99), 9: (66, 62)
}
city_groups = [
    [1, 4], [2, 6], [7], [5], [9], [8], [3]
]

# Tour from the proposed solution
proposed_tour = [0, 1, 5, 7, 9, 8, 2, 3, 0]

# Check the correctness of the solution
result = check_solution(proposed_tour, city/groups, cities)
print(result)