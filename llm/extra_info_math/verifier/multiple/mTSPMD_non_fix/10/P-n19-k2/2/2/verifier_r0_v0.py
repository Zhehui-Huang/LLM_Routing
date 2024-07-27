import math

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define tours and costs from the solution
tours = [
    [0],
    [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]
costs = [0, 0]
starting_depot = 0
expected_total_cost = 0

def calculate_distance(city1, city2):
    return math.dist(cities[city1], cities[city2])

def check_solution(tours, expected_total_cost):
    visited = set()
    computed_total_cost = 0

    for idx, tour in enumerate(tours):
        # Check starting at the right depot
        if tour[0] != starting_depot:
            print("FAIL: Robot", idx, "does not start at the correct depot")
            return

        # Calculate travel cost for each tour
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_distance(tour[i], tour[i+1])
        if idx == 0:
            tour_cost += calculate_distance(tour[-1], tour[0])

        if costs[idx] != tour_cost:
            print("FAIL: Incorrect travel cost for Robot", idx)
            return

        visited.update(tour)
    
    # Check if every city is visited exactly once
    if len(visited) != len(cities) or any(city not in visited for city in cities):
        print("FAIL: Not all cities are visited or are visited more than once")
        return
    
    # Check the total travel cost
    computed_total_cost = sum(costs)
    if computed_total_cost != expected_total_cost:
        print("FAIL: Total cost does not match expected cost")
        return

    print("CORRECT")

# Run the test function
check_solution(tours, expected_total_cost)