from math import sqrt

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robots information
num_robots = 2
capacities = [160 for _ in range(num_robots)]

# Function to calculate Euclidean distance
def distance(a, b):
    return sqrt((coordinates[a][0] - coordinates[b][0])**2 + (coordinates[a][1] - coordinates[b][1])**2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = [[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Cluster cities for robots based on nearest unassigned city and capacity
tours = [[] for _ in range(num_robots)]
remaining_capacity = capacities[:]
assigned_cities = set()

for robot in range(num_robots):
    tours[robot].append(0)  # Start at depot
    current_city = 0
    
    # Create a route for the robot
    while True:
        # Find nearest unvisited city that fits capacity
        next_city = None
        min_dist = float('inf')
        
        for city in range(1, num_cities):
            if city not in assigned_cities and remaining_capacity[robot] >= demands[city] and distance_matrix[current_city][city] < min_dist:
                min_dist = distance_matrix[current_city][city]
                next_city = city
                
        if next_city is None:
            break  # No further allocation possible
        tours[robot].append(next_city)
        assigned_cities.add(next_city)
        remaining_capacity[robot] -= demands[next_city]
        current_city = next_city

    tours[robot].append(0)  # Return to depot

# Calculate costs
total_costs = []
for tour in tours:
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_costs.append(cost)

# Output the results
overall_total_cost = sum(total_costs)
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_total_cost}")