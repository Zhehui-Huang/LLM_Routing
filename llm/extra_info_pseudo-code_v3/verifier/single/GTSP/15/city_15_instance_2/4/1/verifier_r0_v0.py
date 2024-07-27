import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_requirements(tour, total_cost, cities, city_groups):
    # Requirement 1: Start and end at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour must start and end at the depot city."
    
    # Requirement 2: Exactly one city from each group
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the depot start and end in the checking
        group_found = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return f"FAIL: More than one city visited from group {group_index}."
                visited_groups.append(group); group_found = True
                break
        if not group_found:
            return f"FAIL: City {city} does not belong to any defined group."
    if len(visited_groups) != len(city_groups):
        return "FAIL: Not all groups are visited."

    # Requirement 3 and 5: Check total cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return f"FAIL: Incorrect travel cost. Calculated: {calculated_cost}, Reported: {total_cost}"

    # All checks passed
    return "CORRECT"

# Define cities and groups
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}
city_groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Provided solution
tour = [0, 12, 10, 4, 3, 2, 0]
total_cost = 138.15

# Validate the solution
result = check_requirements(tour, total_cost, cities, city_groups)
print(result)