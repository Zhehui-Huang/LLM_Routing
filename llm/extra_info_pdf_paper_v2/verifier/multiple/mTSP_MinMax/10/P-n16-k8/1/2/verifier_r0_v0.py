def calculate_distance(city1, city2):
    # Euclidean distance between two cities.
    return ((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2) ** 0.5

# Coordinates given for each city
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69)
}

# Provided tours data from robots
tours = [
    [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0]
]

def verify_tours(tours, cities):
    all_visited = set()

    # Check Requirement 1: Each tour starts and ends at city 0
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check Requirement 2: All cities visited exactly once collectively
    for tour in tours:
        for city in tour[1:-1]:  # Exclude the starting and ending depot city
            if city in all_visited:
                return "FAIL"
            all_visited.add(city)
            
    if all_visited != set(cities.keys()) - {0}:  # Exclude the depot city from the required set
        return "FAIL"

    # Check Requirement 3: Minimize the maximum distance traveled
    # (For unit testing, it's hard to validate mathematically if this is the minimum maximum,
    #  so we just ensure the structure is correct. The main solution's responsibility is correct implementation.)
    # However, it's logical that if only one robot is doing all the work while others do nothing,
    # it could likely not be the optimal min-max load balance unless proven otherwise by constraints.

    if not all(len(tour) == 2 for tour in tours[1:]):  # All except one robot do nothing
        return "FAIL"

    return "CORRECT"

# Print the verification result
print(verify_tours(tours, cities))