import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# City demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12,
    26, 17, 6, 15, 5, 10
]

# Tour information
tours = [
    [10, 0], [20, 0], [0, 6], [0, 2], [13, 7, 14, 0], [0, 4],
    [15, 1, 0], [21, 0], [0, 11], [22, 5, 0], [0, 16, 8],
    [0, 12, 3], [0, 18, 19, 0], [0, 9, 17, 0]
]

# Actual robot tours along with demands and capacity
robot_capacity = 40
robot_tours = []
robot_tours_demand = []
for tour in tours:
    robot_tours.append(tour)
    demand_sum = sum(demands[city] for city in tour if city != 0)
    robot_tours_demand.append(demand_sum)

# Check start and end at depot, capacity, and all cities covered
start_end_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in robot_tours)
capacity_check = all(demand <= robot_capacity for demand in robot_tours_demand)

# Check if all cities are visited and demands are met
city_visit = [False] * len(coordinates)
for tour in robot_tours:
    for city in tour:
        city_visit[city] = True
all_visited = all(city_visit[1:])  # skipping the depot city

# Compute total travel costs and check route minimization
total_cost_calculated = sum(
    sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    for tour in robot_tours
)

# Given total travel cost
total_cost_given = 471.31

# Define correctness criteria
correct_solution = start_end_depot and capacity_check and all_visited and math.isclose(total_cost_calculated, total_cost_given, abs_tol=0.1)

if correct_solution:
    print("CORRECT")
else:
    print("FAIL")