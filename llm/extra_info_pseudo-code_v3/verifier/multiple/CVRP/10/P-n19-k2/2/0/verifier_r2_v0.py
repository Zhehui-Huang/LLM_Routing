import math

# City information
cities = {
    0: {'coord': (30, 40), 'demand': 0},
    1: {'coord': (37, 52), 'demand': 19},
    2: {'coord': (49, 43), 'demand': 30},
    3: {'coord': (52, 64), 'demand': 16},
    4: {'coord': (31, 62), 'demand': 23},
    5: {'coord': (52, 33), 'demand': 11},
    6: {'coord': (42, 41), 'demand': 31},
    7: {'coord': (52, 41), 'demand': 15},
    8: {'coord': (57, 58), 'demand': 28},
    9: {'coord': (62, 42), 'demand': 14},
    10: {'coord': (42, 57), 'demand': 8},
    11: {'coord': (27, 68), 'demand': 7},
    12: {'coord': (43, 67), 'demand': 14},
    13: {'coord': (58, 27), 'demand': 19},
    14: {'coord': (37, 69), 'demand': 11},
    15: {'coord': (61, 33), 'demand': 26},
    16: {'coord': (62, 63), 'demand': 17},
    17: {'coord': (63, 69), 'demand': 6},
    18: {'coord': (45, 35), 'demand': 15}
}

# Robot tours
robot_tours = [
    [0, 12, 11, 1, 15, 10, 13, 3, 7, 4, 17, 0],
    [0, 9, 16, 2, 5, 6, 8, 18, 14, 0]
]

# Robot capacities
robot_capacities = [160, 160]

def calculate_euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def verify_solution(tours, capacities):
    # Check if all cities are visited exactly once and demands are met
    visit_count = {key: 0 for key in cities}
    for tour in tours:
        load = 0
        prev_city = tour[0]
        for city in tour[1:]:
            load += cities[city]['demand']
            visit_count[city] += 1
            if city != 0:  # Depot can be visited multiple times
                if visit_count[city] > 1:
                    return False, "City visited more than once"
        if load > capacities[tours.index(tour)]:
            return False, "Capacity exceeded"

    for city, count in visit_count.items():
        if city != 0 and count != 1:
            return False, "A city was missed or visited multiple times"

    # Check if all tours start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False, "Tour does not start and end at depot"

    # Calculate and verify the travel cost
    reported_costs = [326.9569998127075, 213.53789276444567]
    for index, tour in enumerate(tours):
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_euclidean_distance(cities[tour[i]]['coord'], cities[tour[i+1]]['coord'])
        if not math.isclose(cost, reported_costs[index], rel_tol=1e-6):
            return False, f"Cost mismatch: expected {reported_costs[index]}, got {cost}"

    return True, "All checks passed"

# Running checks
correct, message = verify_solution(robot_tours, robot_capacities)
if correct:
    print("CORRECT")
else:
    print("FAIL:", message)