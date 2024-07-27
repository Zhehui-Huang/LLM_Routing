import numpy as np

cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Distance calculation
def calculate_distance(i, j):
    return np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = calculate_distance(i, j)

# Number of robots
n_robots = 4

# Split cities into chunks for initial simple solution
city_indices = list(cities.keys())[1:]  # exclude depot
chunk_size = len(city_indices) // n_robots
chunks = [city_indices[i:i + chunk_size] for i in range(0, len(city_indices), chunk_size)]

# Ensure all robots have a job if cities are not evenly divisible
while len(chunks) > n_robots:
    last_chunk = chunks.pop()
    for i in range(len(last_chunk)):
        chunks[i % n_robots].append(last_chunk[i])

# Build tours starting and ending at the depot
tours = {}
for robot in range(n_robots):
    tour = [0] + chunks[robot] + [0]
    tours[robot] = tour

# Compute travel cost for each tour
travel_costs = {}
max_cost = 0
for robot, tour in tours.items():
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    travel_costs[robot] = total_cost
    max_cost = max(max_cost, total_cost)

# Output results
for robot, tour in tours.items():
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {travel_costs[robot]}")
print(f"Maximum Travel Cost: {max_increment_costs}")