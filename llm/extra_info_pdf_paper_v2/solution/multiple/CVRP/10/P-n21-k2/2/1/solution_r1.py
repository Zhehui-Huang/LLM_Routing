import numpy as np

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), 
    (31, 62), (52, 33), (42, 41), (52, 41), 
    (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), 
    (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Parameters for robots
num_robots = 2
capacity = 160

# Calculate Euclidean distance between two points
def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Compute distance matrix
n = len(coordinates)
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Clarke-Wright Savings Algorithm Initialization
def savings_list(depot, nodes):
    savings = []
    for i in nodes:
        for j in nodes:
            if i != j:
                s = distance_matrix[depot][i] + distance_matrix[depot][j] - distance_matrix[i][j]
                savings.append((s, i, j))
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])
    return savings

# Implement a modified Clarke-Wright algorithm
def clarke_wright(depot, demands, capacity, num_robots):
    nodes = list(range(1, len(demands)))  # exclude the depot
    savings = savings_list(depot, nodes)
    tours = [[] for _ in range(num_robots)]
    loads = [0] * num_robots

    # Assign each feasible saving to a vehicle if it does not violate constraints
    for s, i, j in savings:
        for k in range(num_robots):
            if i in tours[k] or j in tours[k] or all(i in t for t in tours) or all(j in t for t in tours):
                continue
            if loads[k] + demands[i] <= capacity and loads[k] + demands[j] <= capacity:
                if not tours[k]:
                    tours[k].extend([i, j])
                    loads[k] += (demands[i] + demands[j])
                    break
                elif i in tours[k] and not any(j in t for t in tours):
                    tours[k].append(j)
                    loads[k] += demands[j]
                    break
                elif j in tours[k] and not any(i in t for t in tours):
                    tours[k].append(i)
                    loads[k] += demands[i]
                    break

    # Make sure to return to the depot
    tours = [[depot] + tour + [depot] for tour in tours if tour]

    return tours, loads

# Run the Clarke-Wright algorithm
tours, loads = clarke_wright(0, demands, capacity, num_robots)

# Calculate and print costs and tours
total_cost = 0
for idx, tour in enumerate(tours):
    tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")