import numpy as np

# Data
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
    1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700
]
num_robots = 4
robot_capacity = 6000

# Calculate Euclidean Distance Matrix
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def find_tour(start_idx, remaining_demands, capacity, num_cities):
    tour = [start_idx]
    current_capacity = capacity
    while True:
        min_distance = float('inf')
        next_city = None
        for i in range(1, num_cities):
            if remaining_demands[i] > 0 and remaining_demands[i] <= current_capacity:
                distance = distance_matrix[tour[-1]][i]
                if distance < min_distance:
                    min_distance = distance
                    next_city = i
        if next_city is None:
            break
        tour.append(next_city)
        current_capacity -= remaining_demands[next_city]
        remaining_demands[next_city] = 0
    tour.append(start_idx)  # return to depot
    return tour

# Generate tours
remaining_demands = demands[:]
all_tours = []
for _ in range(num_robots):
    if sum(remaining_demands) == 0:
        break
    tour = find_tour(0, remaining_demands, robot_capacity, num_cities)
    all_tours.append(tour)

# Calculate total travel cost and print results
overall_total_cost = 0
for i, tour in enumerate(all_tours):
    tour_cost = sum(distance_matrix[tour[j]][tour[j+1]] for j in range(len(tour) - 1))
    overall_total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")