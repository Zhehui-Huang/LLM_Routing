import numpy as np

# Coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demand list of each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Robot information
num_robots = 2
capacity = 160

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return np.linalg.norm(np.subtract(coordinates[city1], coordinates[city2]))

# Precompute distances
num_cities = len(coordinates)
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(i, j)

# Initialize solution
def find_tours():
    tours = [[] for _ in range(num_robots)]
    loads = [0] * num_robots
    city_assigned = [False] * num_cities
    city_assigned[0] = True
    
    # Set initial position to the depot
    for robot in range(num_robots):
        tours[robot].append(0)
    
    # Keep assigning cities until all are assigned
    while not all(city_assigned[1:]):  # Skipping depot
        for robot in range(num_robots):
            current_city = tours[robot][-1]
            next_city = None
            min_distance = float('inf')
            for city in range(1, num_cities):
                if not city_assigned[city] and loads[robot] + demands[city] <= capacity:
                    distance = distances[current_city][city]
                    if distance < min_distance:
                        min_distance = distance
                        next_city = city
            if next_cal_coords:
                tours[robot].append(next_city)
                loads[robot] += demands[next_city]
                city_assigned[next_city] = True
            # Return to depot at the end of each robot's tour
            if all(city_assigned[1:]) or (next_city is None):
                tours[robot].append(0)
                break
            
    return tours

tours = find_tours()

# Calculate tours' travel costs
def calculate_travel_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]][tour[i+1]]
    return cost

# Display the tours and costs
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_travel_cost(tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}\n")

print(f"Overall Total Travel Cost: {total_cost}")