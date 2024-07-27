import math

# City coordinates and demands
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

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Calculating all the pairwise distances
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Implementing the Clarke-Wright Savings Algorithm
def clarke_wright_savings():
    savings = []
    for i in range(1, len(coordinates)):
        for j in range(1, len(coordinates)):
            if i != j:
                s = distances[0][i] + distances[0][j] - distances[i][j]
                savings.append((s, i, j))
    # Sort savings in descending order of savings value
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

savings = clarke_wright_savings()

# Assign routes to robots considering their capacities and demands
tours = [[] for _ in range(num_robots)]
current_load = [0] * num_robots

def find_route_for_delivery():
    used = [False] * len(coordinates)
    used[0] = True  # Depot is always used
    total_cost = 0

    for s, i, j in savings:
        if not used[i] or not used[j]:
            for robot in range(num_robots):
                if not used[i] and (current_load[robot] + demands[i]) <= robot_capacity:
                    if 0 not in tours[robot]:
                        tours[robot].append(0)
                    tours[robot].extend([i, 0])
                    current_load[robot] += demands[i]
                    used[i] = True
                    break
                elif not used[j] and (current_load[robot] + demands[j]) <= robot_capacity:
                    if 0 not in tours[robot]:
                        tours[robot].append(0)
                    tours[robot].extend([j, 0])
                    current_load[robot] += demands[j]
                    used[j] = True
                    break
    
    # Calculate travel costs for each robot
    for robot in range(num_robots):
        route_cost = 0
        if len(tours[robot]) > 1:
            for k in range(len(tours[robot])-1):
                route_cost += distances[tours[robot][k]][tours[robot][k+1]]
            print(f"Robot {robot} Tour: {tours[robot]}")
            print(f"Robot {robot} Total Travel Cost: {route_cost:.2f}")
            total_cost += routeﷻ
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

find_route_for_delivery()