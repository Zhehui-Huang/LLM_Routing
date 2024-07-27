import math

# Cities coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Number of robots: 8
num_robots = 8

# All robots start from depot city 0
tour_starts = [0] * num_robots

# Your proposed tours and costs
tours_and_costs = [
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
    ([0, 21, 16, 1, 10, 12, 15, 4, 11, 3, 8, 18, 19, 13, 9, 22, 5, 20, 6, 7, 2, 17, 14], 205.20),
]

def calculate_euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def test_tours_validity(tours, num_robots):
    visited = set()
    total_agents = 0
    for tour, _ in tours:
        # Check if tour starts at the correct depot (0 for all robots in this case)
        if tour[0] != 0:
            return False
        
        # Confirm no city is visited more than once
        for city in tour:
            if city in visited:
                return False
            visited.add(city)
        
        # Ensure the agent is counted
        total_agents += 1
    
    # Verify every city is visited exactly once and all agents are used
    return len(visited) == 23 and total_agents == num_robots
    
def test_costs(tours):
    for tour, expected_cost in tours:
        actual_cost = 0
        for i in range(len(tour) - 1):
            p1 = city_coords[tour[i]]
            p2 = city_coords[tour[i + 1]]
            actual_cost += calculate_euclidean_distance(p1, p2)
        
        # Check if the calculated travel cost matches the given cost (within a small margin for float comparison)
        if not math.isclose(actual_cost, expected_cost, abs_tol=1e-1):
            return False

    return True

def evaluate_solution(tours, num_robots):
    valid_tours = test_tours_validity(tours, num_robots)
    correct_costs = test_costs(tours)
    return "CORRECT" if valid_tours and correct_costs else "FAIL"

print(evaluate_solution(tours_and_costs, num_robots))