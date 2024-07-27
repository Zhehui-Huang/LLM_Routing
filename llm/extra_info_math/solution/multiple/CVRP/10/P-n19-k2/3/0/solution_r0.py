import math

# Data initialization
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
capacity = 160
num_robots = 2

# Calculate Euclidean distances between cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate savings
n = len(coordinates)
savings_list = []
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            save = distance(0, i) + distance(0, j) - distance(i, j)
            savings_list.append((save, i, j))
savings_list.sort(reverse=True, key=lambda x: x[0])  # Sort by savings in decreasing order

# Assign routes to robots using savings
tours = {robot: [[0]] for robot in range(num_robots)}
capacities = {robot: capacity for robot in range(num_robots)}

for save, i, j in savings_list:
    added = False
    for robot in range(num_robots):
        for tour in tours[robot]:
            if capacities[robot] >= (demands[i] + demands[j]) and (i in tour) + (j in tour) == 1:
                if i in tour:
                    tour.append(j)
                else:
                    tour.append(i)
                capacities[robot] -= (demands[i] + demands[j])
                added = True
                break
        if added:
            break

# Creating complete tours
for robot in range(num_robots):
    for tour in tours[robot]:
        if tour[-1] != 0:
            tour.append(0)  # Return to depot

# Calculating travel costs
travel_costs = {robot: 0 for robot in range(num_robots)}
for robot in tours:
    for tour in tours[robot]:
        for k in range(len(tour) - 1):
            travel_costs[robot] += distance(tour[k], tour[k+1])

# Output the routes and costs
overall_cost = sum(travel_costs.values())
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {tours[robot][0]}")
    print(f"Robot {robot} Total Travel Cost: {travel_costs[robot]}")
print(f"Overall Total Travel Cost: {overall_cost}")