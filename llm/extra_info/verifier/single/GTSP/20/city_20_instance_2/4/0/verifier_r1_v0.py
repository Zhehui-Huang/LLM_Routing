import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost, city_coordinates, city_groups):
    # Requirement 1: Tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    city_group_count = {i: 0 for i in range(len(city_groups))}
    for city in tour[1:-1]:  # excluding the depot city at start and end
        found_group = False
        for group_index, group in enumerate(city_groups):
            if city in group:
                city_group_count[group_index] += 1
                found_group = True
                break
        if not found_group:
            return "FAIL"

    if any(count != 1 for count in city_group_count.values()):
        return "FAIL"
    
    # Requirement 4: Output has tour list starting and ending at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Calculate the actual travel cost
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        computed_total_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Requirement 5: Output has total cost
    computed_total_cost = round(computed_total_cost, 2)
    if computed_total_cost != total_cost:
        return "FAIL"

    return "CORRECT"

# Cities Coordinates
cities = {
    0: (3, 26),   1: (85, 72),  2: (67, 0),   3: (50, 99),  4: (61, 89),
    5: (91, 56),  6: (2, 65),   7: (38, 68),  8: (3, 92),   9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

proposed_tour = [0, 16, 19, 18, 11, 6, 0]
proposed_cost = 150.53

# Check the solution
solution_status = verify_solution(proposed_tour, proposed_cost, cities, groups)
print(solution_status)