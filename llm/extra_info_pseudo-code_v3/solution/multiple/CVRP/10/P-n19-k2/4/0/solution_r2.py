import numpy as np

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Parameters
num_robots = 2
robot_capacity = 160

# Compute distance matrix
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i][j] = float('inf')  # Avoid staying in the same place

# Greedy Solution
def greedy_solution():
    robots_tours = [[] for _ in range(num_robots)]
    robots_loads = [0] * num_robots
    city_visited = [False] * num_cities
    city_visited[0] = True  # depot visited
    
    while not all(city_visited):
        for robot in range(num_robots):
            current_city = 0 if not robots_tours[robot] else robots_tours[robot][-1]
            if current_city != 0:  # start a new tour to depot if not at depot
                robots_tours[robot].append(0)
                current_city = 0
            while True:
                next_city = np.argmin(distance_matrix[current_city])
                if demands[next_city] + robots_loads[robot] <= robot_capacity and not city_visited[next_city]:
                    robots_tours[robot].append(next_city)
                    city_visited[next_city] = True
                    robots_loads[robot] += demands[next_city]
                    current_city = next_city
                else:
                    break
    # Close all routes by returning to depot
    for robot in range(num_robots):
        if robots_tours[robot][-1] != 0:
            robots_tours[robot].append(0)

# Calculate Costs
def calculate_cost(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Tour: {tour} Cost: {tour_cost}")
        total_cost += tour_cost
    return total_cost

greedy_solution()

cost_array = []
for i in range(num_robots):
    print(f"Robot {i}")
    cost = calculate_cost([robots_tours[i]])
    cost_array.append(cost)
print(f"Overall Total Travel Cost: {sum(cost_array)}")