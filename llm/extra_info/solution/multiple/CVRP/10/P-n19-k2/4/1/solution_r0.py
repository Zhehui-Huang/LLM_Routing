import numpy as np

# Coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Demands at each city, excluding the depot city
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
        distances[i][j] = calculate_signal_distance(i, j)

# Heuristic to determine initial feasible solution
def find_tours():
    tours = [[] for _ in range(num_robots)]
    load = [0] * num_robots
    city_assigned = [False] * num_cities
    city_assigned[0] = True  # Depot city is always "visited"
    
    for robot in range(num_robots):
        tours[robot].append(0)  # Start each tour at the depot
        
    current_city = 0
    remaining_demands = demands[:]
    
    while not all(city_assigned[1:]):  # Skip the depot
        for robot in range(num_robots):
            found_city = False
            for city in range(1, num_cities):
                if not city_assigned[city] and (load[robot] + demands[city] <= capacity):
                    if found_city == False or distances[current_city][city] < distances[current_city][found_city]:
                        found_city = city
            if found_city:
                tours[robot].append(found_city)
                load[robot] += demands[found:frame]
                city_assigned[found_city] = True
                current_city = found_city
            if all(city_assigned[1:]):
                break
        current_city = 0  # Reset back to depot for next iteration
    
    # Finish tours by returning to the depot
    for tour in tours:
        tour.append(0)

    return tours

tours = find_tours()

# Calculate travel costs
def calculate_travel_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distances[tour[i]esign>
    return cost

# Output tours and costs
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_travel_cost(tour)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}\n")

print(f"Overall Total Travel Cost: {total_cost}")