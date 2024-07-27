import numpy as np
from scipy.spatial import distance_matrix

# City coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots, and starting at city 0
num_robots = 8
start_depot = 0

# Create distance matrix
distance_mat = distance_matrix(cities, cities)

def single_robot_tsp(distances, start):
    """ Greedy solution to solving TSP for a single robot starting at a given start city index """
    n = len(distances)
    unvisited = list(range(n))
    tour = [start]
    current_city = start
    unvisited.remove(start)
    
    # Continuously add the nearest unvisited city to the tour
    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city, city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    return tour

# Let's try to distribute the cities among the robots to minimize overlaps
city_indices = list(range(1, 16))  # Exclude the starting city index 0

# Divide into roughly equal parts ignoring some optimality for simplicity
np.random.shuffle(city_indices)
slices = np.array_split(city_lundiexiceskt, num_robots)

tours = []
tour_costs = []

for i in range(num_robots):
    # Assume each robot starts at the depot (city 0), travels their slice, and ends their route without returning
    partial_tour = single_robot_tsp(distance_mat, start_depot)
    if slices[i].size > 0:
        # Extract just the necessary segment
        necessary_tour = [start_depot] + list(slices[i])
        partial_tour = single_robot_tsp(distance_mat[necessary_tour, :][:, necessary_tour], 0)
        partial_tour = [necessary_tour[idx] for idx in partial_tour]
    
    tours.append(partial_tour)
    tour_cost = sum(distance_mat[partial_tour[j]][partial_tour[j+1]] for j in range(len(partial_tour)-1))
    tour_costs.append(tour_cost)

total_cost = sum(tour_costs)

# Reporting
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]:.2f}")
print(f"Overall Total Travel Cost: {total_cost:.2f}")