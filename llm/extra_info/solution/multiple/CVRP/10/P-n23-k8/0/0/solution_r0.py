import numpy as np

# Given data
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40
num_robots = 8

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i][j] = euclidean_data = euclidean_distance(cities[i], cities[j])
        else:
            distance_matrix[i][j] = float('inf')

# Creating tours using Nearest Neighbor heuristic that checks capacity constraints
def create_tours():
    capacity = [robot_capacity] * num_robots
    tours = [[] for _ in range(num_robots)]
    remaining_cities = set(range(1, n))  # start from 1 to exclude depot city
    
    robot_idx = 0
    while remaining_cities:
        if not tours[robot_idx]:
            tours[robot_idx].append(0)  # start from the depot
        
        current_city = tours[robot_idx][-1]
        next_city = None
        min_distance = float('inf')
        
        for city in remaining_cities:
            if distance_matrix[current_city][city] < min_distance and demands[city] <= capacity[robot_idx]:
                min_distance = distance_matrix[current_city][city]
                next_city = city
        
        if next_city is None:
            tours[robot_idx].append(0)  # return to depot if no available city
            robot_idx = (robot_idx + 1) % num_robots
            if robot_idx == 0 and all(tour[-1] == 0 for tour in tours):  # Check if all robots are back at the depot
                break
        else:
            tours[robot_idx].append(next_city)
            capacity[robot_idx] -= demands[next_city]
            remaining_cities.remove(next_city)
    
    # Ensure all tours end at the depot
    for tour in tours:
        if tour[-1] != 0:
            tour.append(0)
    
    return tours

tours = create_tours()

# Calculate costs and output
overall_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")