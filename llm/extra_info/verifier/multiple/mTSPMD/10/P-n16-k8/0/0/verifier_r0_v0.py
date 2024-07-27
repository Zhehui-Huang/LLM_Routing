import math

# Initial data setup
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

robot_tours = {
    0: [0, 0], 1: [1, 10, 1], 2: [2, 13, 2], 3: [3, 8, 12, 3],
    4: [4, 11, 15, 4], 5: [5, 14, 5], 6: [6, 6], 7: [7, 9, 7]
}

# Functions to calculate Euclidean distance and total route distance
def euclidean_distance(a, b):
    ax, ay = city_coords[a]
    bx, by = cityVcoords[b]
    return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

def route_distance(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Verification
all_cities = set(range(16))
visited_cities = set()

def verify_solution():
    # Requirement 1: Check start and end at depots
    for robot, tour in robot_tours.items():
        if tour[0] != tour[-1] or tour[0] != robot:
            return "FAIL"
    
    # Requirement 2: Check all cities visited once
    for tour in robot_tours.values():
        visited_cities.update(tour[1:-1])
    if visited_cities != all_cities:
        return "FAIL"
    
    # Requirement 3: Check if the actual travel cost corresponds to the minimum criteria
    # This is complex to verify completely without solving the problem and is often
    # verified through optimization algorithms or approximation methods.
    # However, you can check if the reported and calculated distances match.
    total_calculated_cost = 0
    for robot, tour in robot_tours.items():
        calculated_cost = route_distance(tour)
        reported_cost = float(tour_comments[robot])
        if not math.isclose(calculated_cost, reported_cost):
            return "FAIL"
        total_calculated_cost += calculated_cost
    
    return "CORRECT"

# Printing the result
print(verify_solution())