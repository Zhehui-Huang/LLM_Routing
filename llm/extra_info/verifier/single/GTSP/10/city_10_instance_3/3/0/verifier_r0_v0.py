import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = [
        (84, 67),  # Depot City 0
        (74, 40),  # City 1
        (71, 13),  # City 2
        (74, 82),  # City 3
        (97, 28),  # City 4
        (0, 31),   # City 5
        (8, 62),   # City 6
        (74, 56),  # City 7
        (85, 71),  # City 8
        (6, 76)    # City 9
    ]
    groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]

    # Check Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2
    visited_groups = set()
    for city in tour[1:-1]:  # Skip the initial and final depot cities
        found_group = False
        for i, group in enumerate(groups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"
                visited_groups.add(i)
                found_group = True
                break
        if not found_group:
            return "FAIL"

    if len(visited_groups) != len(groups):
        return "FAIL"

    # Check Requirement 3 and 5
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # We round the total cost here to match usual precision in such calculations
    calculated_cost = round(calculated_cost, 2)
    if calculated_cost != total_cost:
        return "FAIL"

    # Check Requirement 4
    if len(tour) < 2 or tour[-1] != 0 or tour[0] != 0:
        return "FAIL"

    return "CORRECT"

# Tour and cost provided as solution
tour_given = [0, 7, 1, 4, 5, 6, 8, 0]
total_cost_given = 244.94

# Check solution validity
result = verify_solution(tour_given, total_cost_given)
print(result)