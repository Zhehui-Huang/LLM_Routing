import numpy as np
from scipy.spatial.distance import pdist, squareform

# City coordinates and demands
coordinates = np.array([
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
])
demands = np.array([
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 
    1800, 700
])

# Robot parameters
num_robots = 4
capacity = 6000

# Calculate distance matrix
distance_matrix = squareform(pdist(coordinates, 'euclidean'))

# Simplified heuristic: assign cities to robots until their capacity is reached, then proceed the tour
tours = [[] for _ in range(num_robots)]
loads = np.zeros(num_robots)
tour_costs = np.zeros(num_robots)

# Assign cities to robots
city_indices = list(range(1, len(coordinates)))  # city 0 is depot
robot_index = 0

while city_indices:
    city = city_indices.pop(0)
    if loads[robot_index] + demands[city] <= capacity:
        if not tours[robot_index]:  # start new tour if empty
            tours[robot_index].append(0)  # start at depot
        tours[robot_index].append(city)
        loads[robot_index] += demands[city]
        last_city = tours[robot_index][-1]
        tour_costs[robot_index] += distance_matrix[tours[robot_index][-2]][last_city] if len(tours[robot_index]) > 1 else 0
    else:
        city_indices.append(city)  # re-add city at the end of the list for next robot
        tours[robot_index].append(0)  # go back to depot
        robot_index = (robot_index + 1) % num_robots  # move to next robot
        continue

    if city_indices:
        continue

    # Finalize current robot's tour
    tours[robot_index].append(0)
    tour_costs[robotpath] += distance_matrix[tours[robot_index][-2]][0]  # return to depot

# Calculate Overall Total Travel Cost
total_cost = np.sum(tour_costs)

# Output the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")
print(f"Overall Total Travel Cermerging latest code block ost: {total_cost}")