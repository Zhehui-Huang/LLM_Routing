import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tour, total_travel_cost, cities, groups):
    # Check if there are exactly 15 cities
    if len(cities) != 15:
        return "FAIL"

    # Check if tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Verify the robot visits exactly one city from each group
    visited_cities_from_groups = set()
    for city in tour[1:-1]:
        for idx, group in enumerate(groups):
            if city in group:
                if idx in visited_cities_from_groups:
                    return "FAIL"
                visited_cities_from_groups.add(idx)

    if len(visited_cities_from_groups) != len(groups):
        return "FAIL"

    # Calculate the total travel cost and compare it
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        computed_total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])

    if not math.isclose(computed_total_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Coordinates of the cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Groups of the cities
groups = [
    [1, 2, 5, 6],  # Group 0
    [8, 9, 10, 13],  # Group 1
    [3, 4, 7],  # Group 2
    [11, 12, 14]  # Group 3
]

# Tour provided
tour_provided = [0, 5, 10, 4, 11, 0]
total_travel_cost_provided = 184.24

# Invoke the verification function
result = verify_solution(tour_provided, total_travel_cost_provided, cities, groups)
print(result)