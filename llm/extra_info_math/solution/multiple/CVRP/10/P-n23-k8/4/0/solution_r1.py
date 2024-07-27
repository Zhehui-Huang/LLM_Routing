import numpy as np
import pulp
import math

# Define Euclidean distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Setup and solve the CVRP
def solve_cvrp():
    # City coordinates and demands
    city_coords = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 49),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 48),
        14: (58, 27),
        15: (37, 69),
        16: (38, 46),
        17: (61, 33),
        18: (62, 63),
        19: (63, 69),
        20: (45, 35),
        21: (32, 39),
        22: (56, 37),
    }
    demands = [
        0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19,
        11, 12, 26, 17, 6, 15, 5, 10
    ]
    num_cities = len(city_coords)
    num_robots = 8
    robot_capacity = 40

    # Create distance matrix
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(city_coords[i], city_coords[j])

    # Setup optimization problem
    problem = pulp.LpProblem("CVRP", pulp.LpMinimize)

    # Decision variables
    x = pulp.LpVariable.dicts("x", ((r, i, j) for r in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j),
                              cat='Binary')

    # Objective function
    problem += pulp.lpSum([x[r, i, j] * distances[i][j] for r in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j])

    # Constraints
    # Each city is visited exactly once by any robot
    for j in range(1, num_cities):
        problem += pulp.lpSum(x[r, i, j] for r in range(num_robots) for i in range(num_cities) if i != j) == 1

    # Departure and return for each vehicle
    for r in range(num_robots):
        problem += pulp.lpSum(x[r, 0, j] for j in range(1, num_cities)) <= 1  # max one departure from depot
        problem += pulp.lpSum(x[r, j, 0] for j in range(1, num_cities)) <= 1  # max one return to depot

    # Capacity constraints
    for r in range(num_robots):
        problem += pulp.lpSum(demands[j] * x[r, i, j] for i in range(num_cities) for j in range(1, num_cities) if i != j) <= robot_capacity

    # Solve the problem
    problem.solve()

    # Gather results
    total_cost = 0
    robot_tours = []
    for r in range(num_robots):
        tour = [0]
        for i in range(num_cities):
            for j in range(num_cities):
                if i != j and pulp.value(x[r, i, j]) == 1:
                    tour.append(j)
                    break
            if tour[-1] == 0:
                break
        if len(tour) > 1:
            robot_tours.append(tour)
            cost = sum(distances[tour[k]][tour[k + 1]] for k in range(len(tour) - 1))
            total_cost += cost
            print(f"Robot {r} Tour: {tour}")
            print(f"Robot {r} Total Travel Cost: {cost}")

    print(f"Overall Total Travel Cost: {total_cost}")

solve_cvrp()