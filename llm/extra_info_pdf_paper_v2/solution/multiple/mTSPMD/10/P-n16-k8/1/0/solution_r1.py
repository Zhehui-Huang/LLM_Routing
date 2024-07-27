import numpy as np

def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = euclidean_distance(cities[i], cities[j])
    return dist_matrix

def nearest_neighbor_tour(start_city, cities, dist_matrix):
    tour = [start_city]
    n = len(cities)
    unvisited = set(range(n))
    unvisited.remove(start_city)
    
    current_city = start_city
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: dist_matrix[current_city, city])
        total_cost += dist_matrix[current_city, next_city]
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(current_city)
    
    # Return to start
    total_cost += dist_matrix[current_city, start_city]
    tour.append(start_city)
    
    return tour, total_cost

def solve_mtsp(cities, robots):
    dist_matrix = create_distance_matrix(cities)
    results = []
    total_travel_cost = 0
    
    for robot_id, start_city in enumerate(robots):
        tour, cost = nearest_neighbor_tour(start_city, cities, dist_matrix)
        total_travel_cost += cost
        results.append((robot_id, tour, cost))
    
    return results, total_travel_cost

# Define cities and robots start positions
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Each robot starts and ends at its designated depot city
robots = [0, 1, 2, 3, 4, 5, 6, 7]  # depots correspond to the first 8 cities

# Solve the mTSP for the given setup
results, total_travel_cost = solve_mtsp(cities, robots)

for result in results:
    robot_id, tour, cost = result
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}\n")

print(f"Overall Total Travel Cost: {total_travel_cost}")