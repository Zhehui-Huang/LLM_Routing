import numpy as np

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def compute_total_cost(tour, coords):
    return sum(euclidean_distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(start, cities, coords):
    unvisited = set(cities)
    tour = [start]
    current = start
    while unvisited:
        nearest = min(unvisited, key=lambda city: euclidean_distance(coords[current], coords[city]))
        tour.append(nearest)
        unvisited.remove(nearest)
        current = nearest
    tour.append(start)
    return tour

def two_opt_swap(tour, coords):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                new_tour = tour[:]
                new_tour[i:j + 1] = reversed(tour[i:j + 1])
                if compute_total_cost(new_tour, coords) < compute_total_cost(tour, coords):
                    tour = new_tour[:]
                    improved = True
    return tour

# Define coordinates of cities including the depot
coords = [
    (30, 40),  # Depot city
    (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57),
    (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Configuration
n_robots = 8
cities = list(range(1, 16))  # All cities except depot

# Assign cities to robots using a round-robin method
robot_assignments = {i: [] for i in range(n_robots)}
for i, city in enumerate(cities):
    robot_assignments[i % n_robots].append(city)

# Calculate tours for each robot
overall_total_cost = 0
for robot_id in range(n_robots):
    assigned_cities = robot_assignments[robot_id]
    if not assigned_cities:
        continue  # This robot has no cities assigned
    
    tour = nearest_neighbor_tour(0, assigned_cities, coords)
    optimized_tour = two_opt_swap(tour, coords)
    tour_cost = compute_total_cost(optimized_tour, coords)
    
    print(f"Robot {robot_id} Tour: {optimized_tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")
    
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")