import math

# Provided city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# City demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12,
    26, 17, 6, 15, 5, 10
]

# Robot's capacity
capacity = 40

# Provided tours
tours = [
    [0, 18, 19, 3, 19, 13, 19, 0],
    [0, 3, 18, 12, 15, 9, 22, 0],
    [0, 3, 12, 12, 18, 9, 19, 0],
    [0, 11, 15, 15, 19, 9, 14, 13, 22, 10, 19, 0],
    [0, 5, 22, 15, 18, 7, 22, 0],
    [0, 7, 17, 3, 9, 11, 19, 0],
    [0, 2, 8, 10, 13, 0],
    [0, 8, 15, 10, 11, 0]
]

def calculate_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Check Requirement 1: Each tour should start and end at depot 0.
def check_tour_starts_ends_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

# Check Requirement 2: Each city's specific demand must be fully met.
def check_demands_met(tours, demands):
    delivery_count = [0] * len(demands)
    for tour in tours:
        for city in tour:
            delivery_count[city] += 1
    return all(delivery_count[city] * demands[city] >= demands[city] for city in range(len(demands)))

# Check Requirement 3: No robot exceeds its carrying capacity.
def check_capacity_constraints(tours, demands, capacity):
    for tour in tours:
        load = 0
        for city in tour:
            load += demands[city]
            if load > capacity:
                return False
        if load > capacity:
            return False
    return True

# Implement unit tests
def test_solution():
    if not check_tour_starts_ends_depot(tours):
        return "FAIL"
    if not check_demands_met(tours, demands):
        return "FAIL"
    if not check_capacity_constraints(tours, demands, capacity):
        return "FAIL"
    return "CORRECT"

# Output the test results
print(test_solution())