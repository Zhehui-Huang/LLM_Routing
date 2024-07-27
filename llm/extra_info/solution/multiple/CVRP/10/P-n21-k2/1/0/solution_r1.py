import math

# City coordinates and demands
cities = [
    (30, 16), (20, 26), (55, 56), (48, 46), (42, 68), (63, 59), (34, 44),
    (54, 67), (45, 43), (35, 51), (40, 30), (60, 50), (20, 20), (30, 10),
    (50, 60), (25, 25), (55, 15), (60, 30), (70, 70), (45, 65), (70, 52)
]

demands = [0, 10, 15, 20, 25, 5, 15, 10, 20, 22, 12, 15, 7, 5, 20, 8, 12, 30, 40, 22, 10]

# Parameters
num_robots = 2
capacity = 160
depot = 0

# Distance calculation
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

# Implementing a simple iterative heuristic for VRP
tours = [[] for _ in range(num_robots)]
loads = [0] * num_robots

assignment = [False] * len(cities)  # whether each city is served
assignment[depot] = True  # Depot does not need service

while not all(assignment):
    for robot_id in range(num_robots):
        current_city = depot
        tour = [current_city]
        load = 0
        
        while load < capacity:
            next_city = None
            min_dist = float('inf')
            
            # Find nearest unserved city within capacity limit
            for i, is_served in enumerate(assignment):
                if not is_served and loads[robot_id] + demands[i] <= capacity:
                    dist = distance_matrix[current_city][i]
                    if dist < min_dist:
                        min_dist = dist
                        next_city = i
            
            if next_city is None:
                break
            
            # Serve the city and update loads and route
            load += demands[next_city]
            loads[robot_id] += demands[next_city]
            assignment[next_node] = True
            tour.append(next_node)
            current_city = next_node
        
        tour.append(depot)  # Return to depot
        tours[robot_id].append(tour)

# Compute the travel costs for each robot
costs = [0] * num_robots
for i in range(num_robots):
    tour_cost = 0
    for j in range(1, len(tours[i])):
        tour_cost += distance_matrix[tours[i][j - 1]][tours[i][j]]
    costs[i] = tour_cost

# Output results
overall_cost = sum(costs)
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")