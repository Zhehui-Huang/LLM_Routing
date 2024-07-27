import numpy as np

# Distance calculation function
def euclidean_distance(pt1, pt2):
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

# Define cities coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Creating the distance matrix
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(n_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])

# Assign cities to robots based on nearest neighbor heuristic
def find_tour(depot, unvisited):
    current = depot
    path = [depot]
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[current][x])
        total_cost += distance_matrix[current][next_city]
        path.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    
    total_cost += distance_matrix[current][depot]
    path.append(depot)
    return path, total_cost

# Cities divided amongst two robots
unvisited_cities = list(range(2, n_cities))  # Starts from 2 since 0 and 1 are depots for robots 0 and 1, respectively
midpoint = len(unvisited_cities) // 2
robot0_cities, robot1_cities = unvisited_cities[:midpoint], unvisited_cities[midpoint:]

# Robotic tours
robot0_tour, robot0_cost = find_tour(0, robot0_cities)
robot1_tour, robot1_cost = find_tour(1, robot1_cities)

overall_cost = robot0_cost + robot1_cost

print("Robot 0 Tour:", robot0_tour)
print("Robot 0 Total Travel Cost:", round(robot0_cost, 2))
print()
print("Robot 1 Tour:", robot1_tour)
print("Robot 1 Total Travel Cost:", round(robot1_cost, 2))
print()
print("Overall Total Travel Cost:", round(overall_cost, 2))