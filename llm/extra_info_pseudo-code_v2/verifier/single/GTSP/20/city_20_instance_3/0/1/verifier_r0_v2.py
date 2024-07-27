import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates based on the provided index information
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 
    12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 
    18: (53, 76), 19: (19, 72)
}

# Groups with listed city indices
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Provided solution tour and its reported total cost
tour = [0, 19, 6, 2, 13, 12, 18, 0]
reported_total_cost = 158.66

def validate_tour_solution(tour, reported_total_cost):
    # Ensure the tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Tour does not start and end at the depot."

    # Track visiting one city from each group
    visited_from_groups = set()
    for city_index in tour[1:-1]:  # Exclude depot city
        found = False
        for i, group in enumerate(city_groupse):
            if city_index in group:
                if i in visited_from_groups:
                    return f"FAIL: More than one city from group {i} visited."
                visited_from_groups.add(i)
                found = True
                break
        if not found:
            return f"FAIL: City {city_index} not found in any group."
    
    if len(visited_from_groups) != len(city_groups):
        return "FAIL: Not all groups are visited exactly once."

    # Calculate the total distance of the provided tour
    calculated_total_cost = 0
    for i in range(len(tour) - 1):
        calculated_total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check the accuracy of the reported total cost
    if not math.isclose(calculated_total_cost, reported_total_cost, rel_tol=1e-2):
        return f"FAIL: Reported travel cost is incorrect. Expected around {calculated_total_} got {reported_total_cost}"

    return "CORRECT"

# Execute test and print output
test_output = validate_tour_solution(tour, reported_total_cost)
print(test_output)