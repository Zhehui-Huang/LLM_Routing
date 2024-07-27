import math

# Data Setup
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
num_robots = 8
robot_capacity = 40

# Distance calculator function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Create distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Clarke-Wright Savings Calculation
def clarke_wright_savings():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(1, i):
            if i != j:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings.append((s, i, j))
    return sorted(savings, reverse=True, key=lambda x: x[0])

savings = clarke_wright_savings()

# Initialize tours and loads for each robot
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots
used = [False] * len(coordinates)
used[0] = True  # Depot is used by default

# Route assignment per robot
for save, i, j in savings:
    for robot in range(num_robots):
        if not used[i] and current_loads[robot] + demands[i] <= robot_capacity:
            tours[robot].append(i)
            current_loads[robot] += demands[i]
            used[i] = True
        if not used[j] and current_loads[robot] + demands[j] <= robot_capacity:
            tours[robot].append(j)
            current_loads[robot] += demands[j]
            used[j] = True

# Complete the tours with the depot
for tour in tours:
    if tour:
        tour.insert(0, 0)  # Start at depot
        tour.append(0)  # Return to depot

# Calculate travel costs
overall_total_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")