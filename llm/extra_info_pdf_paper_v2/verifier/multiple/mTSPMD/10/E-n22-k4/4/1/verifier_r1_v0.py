import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def verify_tour(robot_tour, expected_total_cost):
    coordinates = [(145, 215), (151, 264), (159, 261), (130, 254),
                   (128, 252), (163, 247), (146, 246), (161, 242),
                   (142, 239), (163, 236), (148, 232), (128, 231),
                   (156, 217), (129, 214), (146, 208), (164, 208),
                   (141, 206), (147, 193), (164, 193), (129, 189),
                   (155, 185), (139, 182)]
    tour_cost = 0
    for i in range(len(robot_tour) - 1):
        tour_cost += calculate_euclidean_distance(coordinates[robot_tour[i]], coordinates[robot_tour[i+1]])
    return abs(tour_cost - expected_total_cost) < 0.001

robot_tours = {
    0: ([0, 14, 16, 13, 11, 0], 67.25305914663984),
    1: ([1, 2, 5, 7, 9, 1], 65.27703607480547),
    2: ([2, 1, 5, 7, 9, 2], 66.38035372181793),
    3: ([3, 4, 8, 6, 10, 3], 72.56313447842228)
}

overall_total_cost_given = 67.25305914663984
calculated_total_cost = sum(cost for _, cost in robot_tours.values())

# Checking requirement: Each city visited once by exactly one robot
all_tours_combined = sum([tour[:-1] for tour, _ in robot_tours.values()], [])  # Ignore last element as it is the depot repeat
if len(set(all_tours_combined)) != 22:
    print("FAIL")
    exit()

# Checking tours for start-end depot correctness and calculating total travel cost
for robot_id, (tour, expected_cost) in robot_tours.items():
    if tour[0] != tour[-1] or not verify_tour(tour, expected_cost):
        print("FAIL")
        exit()

# Check minimization requirement (incorrect example calculation logic, just a mock check)
if abs(calculated_total_cost - overall_total_cost_given) > 0.001:
    print("FAIL")
    exit()

print("CORRECT")