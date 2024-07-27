def euclidean_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def verify_solution(tour, total_cost_calculated):
    # Coordinates of each city
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    # City groups
    groups = [
        [1, 2, 6],  # Group 0
        [3, 7, 8],  # Group 1
        [4, 5, 9]   # Group 2
    ]

    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[i] = True
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited

    # Requirement 3
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        total_travel_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    if not (abs(total_travel_cost - total_cost_calculated) < 0.01):
        return "FAIL"

    return "CORRECT"

# Provided solution details
tour = [0, 5, 6, 7, 0]
total_cost = 72.82824391360948

# Run the test
result = verify_solution(tour, total_cost)
print(result)