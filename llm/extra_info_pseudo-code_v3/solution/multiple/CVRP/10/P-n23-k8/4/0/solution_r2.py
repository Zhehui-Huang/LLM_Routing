import math
from itertools import combinations

# Data definitions
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

num_robots = 8
robot_capacity = 40

# Calculate the Euclidean distance
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Solution function
def generate_initial_solution():
    routes = []
    load = [0] * num_robots
    for robot in range(num_robots):
        current_city = 0
        route = [0]
        remaining_capacity = robot_capacity
        
        # Follow a greedy algorithm choosing next closest city that fits
        while True:
            best_next_city = None
            best_distance = float('inf')
            
            for next_city in range(1, len(coordinates)):
                if next_city not in route and demands[next_city] <= remaining_capacity:
                    if distance_matrix[current_city][next_city] < best_distance:
                        best_next_city = next_city
                        best_distance = distance_matrix[current_city][next_city]
            
            if best_next_city is None:
                break
                
            route.append(best_next_city)
            remaining_capacity -= demands[best_next_city]
            current_city = best_next_city
            
        route.append(0)  # Return to depot
        routes.append(route)
        load[robot] = robot_capacity - remaining_capacity

    return routes, load

# Calculate tour costs using the tour routes
def calculate_tour_costs(routes):
    tour_costs = []
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            cost += distance_matrix[route[i]][route[i+1]]
        tour_costs.append(cost)
    return tour_costs

# Run the solution generation and calculate costs
routes, loads = generate_initial_solution()
tour_costs = calculate_tour_costs(routes)

# Output results
total_cost = sum(tour_costs)
for robot_id, (route, cost) in enumerate(zip(routes, tour_costs)):
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")