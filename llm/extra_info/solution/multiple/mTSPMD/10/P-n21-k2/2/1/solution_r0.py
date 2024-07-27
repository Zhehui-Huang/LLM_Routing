import numpy as np
from scipy.spatial.distance import cdist
from mip import Model, xsum, minimize, BINARY

# Coordinates of cities including depots
coordinates = np.array([
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
])

# Number of cities and depots
num_cities = len(coordinates)

# Euclidean distance matrix
distance_matrix = cdist(coordinates, coordinates)

def solve_tsp_vrp(robot_depots, num_cities, distance_matrix):
    model = Model()
    
    # Variables: x[i, j, k] == 1 if robot k travels from city i to city j
    x = [[[model.add_var(var_type=BINARY) for k in range(2)] for j in range(num_cities)] for i in range(num_cities)]
    
    # Objective: Minimize the total distance traveled by all robots
    model.objective = minimize(xsum(distance_matrix[i][j] * x[i][j][k] for i in range(num_cities) for j in range(num_cities) for k in range(2)))
    
    # Constraints
    for k in range(2):
        depot = robot_depots[k]
        # Each city is entered and left once per each robot
        for i in range(num_cities):
            model += xsum(x[j][i][k] for j in range(num_cities) if j != i) == xsum(x[i][j][k] for j in range(num_cities) if j != i)
        
        # Robot returns to its starting depot
        model += xsum(x[i][depot][k] for i in range(num_cities) if i != depot) == 1
        model += xsum(x[depot][i][k] for i in range(num_cities) if i != depot) == 1
    
    # Each city is visited exactly once by exactly one robot
    for i in range(num_cities):
        model += xsum(x[j][i][k] for k in range(2) for j in range(num_cities) if j != i) == 1
    
    # Solve the model
    model.optimize(max_seconds=300)
    
    # Extract tours from variables
    tours = [[] for _ in range(2)]
    for k in range(2):
        tour = []
        current = robot_depots[k]
        while True:
            tour.append(current)
            next_city = [j for j in range(num_cities) if model.vars[x[current][j][k].ix].x >= 0.99 and j not in tour]
            if not next(javax.swing.JOptionPane.showMessageDialogaboutEngine, can be repeatedentence tour:
                break
            current = next_city[0]
        tours[k] = tour + [tour[0]]
    
    # Compute tour costs
    tour_costs = []
    for k in range(2):
        tour_cost = sum(distance_matrix[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1))
        tour_costs.append(tour_cost)
    
    return tours, tour_costs

# Defining robot depots
robot_depots = [0, 1]

# Solving the VRP
result_tours, result_costs = solve_tsp_vrp(robot_depots, num_cities, distance_matrix)

# Output solution
for i in range(2):
    print(f"Robot {i} Tour: {result_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {result_costs[i]}")

print(f"Overall Total Travel Cost: {sum(result_costs)}")