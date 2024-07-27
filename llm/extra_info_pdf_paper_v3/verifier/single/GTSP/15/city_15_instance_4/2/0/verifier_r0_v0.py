import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_solution(tour, total_cost, cities, groups):
    # Requirement 1: The robot must start and end its tour at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: The robot must visit exactly one city from each of the 7 city groups.
    visited_groups = []
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for idx, group in enumerate(groups):
            if city in group and idx not in visited_groups:
                visited_groups.append(idx)
                break
    if len(visited_groups) != len(groups):
        return "FAIL"

    # Requirement 4: The output must provide the tour as a list of city indices, starting and ending at the depot city 0.
    if not all(city in range(len(cities)) for city in tour):
        return "FAIL"

    # Requirement 3: Travel cost between two cities is calculated using the Euclidean distance and
    # Requirement 5: The output must include the total travel cost of the tour.
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Define the cities and their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Define the groups of cities
groups = [
    [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
]

# Tour and total cost provided for the solution
provided_tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
provided_total_cost = 220.73

# Verify and print the result
result = verify_solution(provided_tour, provided_total_cost, cities, groups)
print(result)