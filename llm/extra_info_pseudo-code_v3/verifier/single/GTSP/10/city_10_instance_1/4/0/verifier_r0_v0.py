import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_travel_cost):
    cities = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    city_groups = {
        0: {5, 6, 7},
        1: {2, 3},
        2: {1, 9},
        3: {4, 8}
    }

    # Check Requirement 1: Tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Exactly one city from each group of cities
    visited_groups = set()
    for index in tour[1:-1]:  # Exclude the depot city from checks
        for group_id, members in city_groups.items():
            if index in members:
                if group_id in visited_test:
                    return "FAIL"
                visited_groups.add(group_id)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Check Requirement 4: Compute travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Check calculated_cost approximately equals the given total_travel_cost
    if not math.isclose(calculated_cost, total_travel_cost, abs_tol=0.01):
        return "FAIL"

    return "CORRECT"

# Provided solution details
provided_tour = [0, 5, 2, 9, 8, 0]
provided_cost = 183.99

# Verify the solution
print(verify_tour(provided_tour, provided_cost))