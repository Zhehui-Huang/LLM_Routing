import math

# Robot tour details
robots_tours = {
    0: [0, 20, 0],
    1: [0, 4, 0],
    2: [0, 10, 0],
    3: [0, 21, 0],
    4: [0, 2, 0],
    5: [0, 16, 0],
    6: [0, 1, 0],
    7: [0, 6, 0]
}

# Coordinates of cities
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
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

def calculate_distance(city1, city2):
    return math.hypot(cities[city1][0] - cities[city2][0], cities[city1][1] - cities[city2][1])

def verify_solution():
    visited_cities = set()
    all_cities = set(range(1, 23))  # excluding depot city 0

    # Check every city is visited exactly once and in only one robot's tour
    for robot, tour in robots_tours.items():
        # Check flow conservation and departure from depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Robot", robot, "does not start and end at the depot.")
            return

        for i in range(1, len(tour) - 1):
            city = tour[i]
            if city in visited_cities:
                print("FAIL: City", city, "visited more than once.")
                return
            visited_cities.add(city)

    # Ensure all cities are visited
    if visited_cities != all_cities:
        print("FAIL: Not all cities are visited.")
        return
    
    # Subtour elimination constraints implicitly held by single visit verification
    # Binary constraints for assignment variables implicitly held by solution structure
    # Continuous variables for node position not explicitly required to be checked as per solution structure

    print("CORRECT")

verify_solution()