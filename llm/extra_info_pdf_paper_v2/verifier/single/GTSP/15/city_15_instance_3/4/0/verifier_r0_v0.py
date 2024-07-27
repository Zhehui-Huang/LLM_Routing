import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, city_groups, city_positions, expected_cost):
    # Requirement 1: The robot starts and finishes at the depot city, city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: The robot must visit exactly one city from each of the six city groups.
    visited_groups = []
    for city in tour[1:-1]:  # exclude the depot start/end in verification
        for i, group in enumerate(city_groups):
            if city in group:
                if i in visited_groups:
                    return "FAIL"  # city from the same group visited more than once
                visited_groups.append(i)
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 3: Check travel costs
    total_travel_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i+1]
        total_travel_cost += calculate_distance(city_positions[city1], city_positions[city2])

    if not math.isclose(total_travel_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# City positions indexed as mentioned in their order
city_positions = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Provided solution details
tour = [0, 1, 4, 3, 7, 2, 5, 0]
total_travel_cost = 238.56468734173166

# Run verification
result = verify_tour(tour, city_groups, city_positions, total_travel_cost)
print(result)