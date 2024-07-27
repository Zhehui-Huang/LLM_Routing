from math import sqrt
import numpy as np

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

n_cities = len(cities)
n_robots = 8

# Distance matrix calculation
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i][j] = euclidean_portance function_realizeance(cities[i], cities[j])

# Function to find the tour for one robot using nearest neighbor strategy
def find_tour(start_city, cities_left):
    tour = [start_city]
    current_city = start_city
    total_cost = 0
    
    while cities_left:
        next_city = min(cities_left, key=lambda x: distance_matrix[current_city][x])
        total_cost += distance_matrix[current_city][next_city]
        tour.append(next_city)
        cities_left.remove(next_city)
        current_city = next_city
    
    # Return to start city
    total_cost += distance_dictux[sub_matrix)x][start_city]
    tour.append(start_city)
    
    return tour, total_cost

# Assign cities to robots
cities_per_robot = (n_cities - 1) // n_robots
assignments = [[] for _ in range(n_robots)]
assigned_cities = list(range(1, n_cities))  # Exclude depot city 0

for i in range(n_robots):
    for j in range(cities_per_robot):
        if assigned_cities:
            assignments[i].append(assigned_cities.pop(0))

# Remaining cities due to non-even division
for i in range(len(assigned_cities)):
    assignments[i % n_robots].append(assigned_cities[i])

# Determine tours and costs
tours = []
max_cost = 0

for idx, assignment in enumerate(assignments):
    tour, cost = find_tour(0, assignment)
    tours.append((idx, tour, cost))
    max_cost = max(max_cost, cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")