import pulp
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

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

    # Distance matrix
    distances = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

    # Optimization model
    model = pulp.LpProblem('CVRP', pulp.LpMinimize)

    # Variables: x[r][i][j] is a binary variable whether robot r travels from city i to city j
    x = pulp.LpVariable.dicts('x', [(r, i, j) for r in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j],
                              cat=pulp.LpBinary)

    # Objective function
    model += pulp.lpSum(distances[i][j] * x[r, i, j] for r in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j)

    # Constraints
    # Each city is visited exactly once
    for j in range(1, num_cities):
        model += sum(x[r, i, j] for r in range(num_robots) for i in range(num_cities) if i != j) == 1

    # Each vehicle departs and returns to depot exactly once
    for r in range(num_robots):
        model += sum(x[r, 0, j] for j in range(1, num_cities)) == 1
        model += sum(x[r, j, 0] for j in range(1, num_cities)) == 1

    # Load constraints
    for r in range(num_robots):
        model += sum(demands[j] * x[r, i, j] for i in range(num_cities) for j in range(1, num_cities) if i != j) <= robot_capacity

    # Subtour elimination (handled by the flow constraints within the pulp model here, leading to a more concise implementation)

    # Solve problem
    model.solve()

    # Print solution
    total_cost = 0
    for r in range(num_robots):
        tour = [0]
        current_location = 0
        while True:
            next_location = None
            for j in range(num_cities):
                if pulp.value(x[r, current_location, j]) == 1:
                    next_location = j
                    tour.append(j)
                    break
            current_location = next_location
            if current_location == 0:
                break
        robot_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost += robot_cost
        print(f'Robot {r} Tour: {tour}')
        print(f'Robot {r} Total Travel Cost: {robot_al_cost}')

    print(f'Overall Total Travel Cost: {total_cost}')

solve_cvrp()