import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# City demand list
city_demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot info
robot_capacity = 40
robot_tours = [
    [0, 21, 1, 11, 19, 13, 9, 0],
    [0, 10, 15, 22, 5, 0],
    [0, 16, 12, 0],
    [0, 20, 7, 0],
    [0, 3, 18, 0],
    [0, 6, 14, 0],
    [0, 4, 0],
    [0, 17, 0]
]

def verify_solution():
    # Check proper start and end at city 0
    for tour in robot_tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check carrying capacities and demands
    demand_fulfilled = [0] * len(city_demands)
    for tour in robot_tours:
        load = 0
        for city in tour[1:-1]:  # exclude the starting and ending depot
            load += city_demands[city]
            demand_fulfilled[city] += city_demands[city]
        if load > robot_capacity:
            return "FAIL"

    # Check if all demands are exactly met
    if demand_fulfilled != city_demands:
        return "FAIL"

    # Optional: check for minimal total distance - cannot verify without comparing to all possibilities
    
    # If all checks pass
    return "CORRECT"

# Output the verification result
print(verify_solution())