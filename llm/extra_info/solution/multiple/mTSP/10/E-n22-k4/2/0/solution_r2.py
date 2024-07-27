import math
import numpy as np

# Define city coordinates
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
    (139, 182)
]

# Calculate distance matrix
def calculate_distances():
    distance_matrix = np.zeros((len(coordinates), len(coordinates)))
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            distance_matrix[i][j] = math.sqrt((coordinates[i][0] - coordinates[j][0])**2 +
                                              (coordinates[i][1] - coordinates[j][1])**2)
    return distance_matrix

dist_matrix = calculate_distances()

# Number of robots
num_robots = 4

def find_tours():
    # Assign each non-depot city to a robot
    city_assignments = {i: [] for i in range(num_robots)}
    cities = list(range(1, len(coordinates)))  # Exclude the depot
    
    # Greedy distribution of cities to robots
    while cities:
        for r in range(num_robots):
            if not cities:
                break
            # assign closest remaining city to current robot
            closest_city = min(cities, key=lambda x: dist_matrix[0][x])
            city_assignments[r].append(closest_city)
            cities.remove(closest_city)
    
    # Conduct tours based on assigned cities
    tours = {}
    total_costs = {}
    overall_cost = 0
    
    for r in range(num_robots):
        tour = [0]  # Start at the depot
        current_city = 0
        cities = city_assignments[r]
        
        while cities:
            # Move to the nearest unvisited city
            next_city = min(cities, key=lambda x: dist_matrix[current_city][x])
            tour.append(next_city)
            cities.remove(next_city)
            current_city = next_city
        
        tour.append(0)  # Return to depot
        tours[r] = tour
        cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_costs[r] = cost
        overall_cost += cost
    
    return tours, total_costs, overall_cost

tours, total_costs, overall_cost = find_tours()

# Output the results
for r in range(num_robots):
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {total_costs[r]}")
print(f"Overall Total Travel Cost: {overall_cost}")