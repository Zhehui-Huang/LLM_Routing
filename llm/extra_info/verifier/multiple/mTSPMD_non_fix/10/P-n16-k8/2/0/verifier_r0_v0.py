import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Tours and costs
robots_info = [
    {"tour": [0, 13, 9, 0], "cost": 36.33154210805005},
    {"tour": [0, 15, 12, 0], "cost": 36.15742310068936},
    {"tour": [0, 6, 0], "cost": 12.041594578792296},
    {"tour": [0, 4, 11, 0], "cost": 29.233818096473218},
    {"tour": [0, 5, 14, 0], "cost": 31.57207413546896},
    {"tour": [0, 8, 3, 0], "cost": 40.26021115508256},
    {"tour": [0, 1, 10, 0], "cost": 20.963511801315278},
    {"tour": [0, 2, 7, 0], "cost": 29.567799786946168}
]

# Function to compute Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(robots_info):
    all_visited = set()
    total_calculated_cost = 0

    # Check all robots
    for robot in robots_info:
        tour = robot['tour']
        actual_cost = robot['cost']
        calculated_cost = 0
        
        # Check tours starting and ending at depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Calculate the distances and verify costs
        for i in range(len(tour) - 1):
            calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
            all_visited.add(tour[i])
        
        all_visited.add(tour[-1])  # add last visited city

        # Compare calculated and provided costs
        if not math.isclose(calculated_cost, actual_cost, rel_tol=1e-5):
            return "FAIL"

        total_calculated_cost += calculated_cost

    # Check if all cities are visited exactly once
    if len(all_visited) != 16:
        return "FAIL"

    # Check if combined calculated cost matches expected
    if not math.isclose(total_calculated_cost, sum(robot['cost'] for robot in robots_info), rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Run the validation function
result = verify_solution(robots_info)
print(result)