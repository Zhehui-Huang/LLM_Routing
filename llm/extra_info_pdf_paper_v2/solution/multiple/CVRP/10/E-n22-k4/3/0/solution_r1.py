import math

# City coordinates and demand data
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
vehicle_capacity = 6000

# Pre-compute distances using Euclidean formula
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Pre-compute all the distances between every pair of nodes
cost_matrix = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        cost_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Heuristic: Start with nearest neighbor tours until the capacity is reached
tours = [[] for _ in range(num_robots)]
load = [0] * num_robots

# Nearest neighbor heuristic for initial tour formation
for robot_id in range(num_robots):
    current_city = 0
    while True:
        # Find nearest unvisited eligible city with demand not exceeding remaining capacity
        next_city = None
        min_distance = float('inf')
        for i in range(1, len(cities)):
            if demands[i] > 0 and load[robot_id] + demands[i] <= vehicle_capacity:
                if cost_matrix[(current_city, i)] < min_distance:
                    next_city = i
                    min_distance = cost_matrix[(current_city, i)]
                    
        if next_city is None:
            # No more cities can be allocated to this robot
            break
           
        # Update tour for the current robot
        tours[robot_id].append(next_city)
        load[robot_id] += demands[next_city]
        demands[next_city] = 0  # Set demand to 0 to mark as visited
        current_city = next_city

    # Complete the tour to go back to the depot
    if tours[robot_id]:
        tours[robot_id].insert(0, 0)
        tours[robot_id].append(0)

# Calculate the total distance of each tour and overall cost
tour_costs = []
overall_total_cost = 0
for tour in tours:
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += cost_matrix[(tour[i], tour[i + 1])]
    tour_costs.append(tour_cost)
    overall_total_cost += tour_cost

# Output the results
for robot_id, tour in enumerate(tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]}")
    
print(f"Overall Total Travel Cost: {overall_totalReach_day_target}halving_period ")