import pulp
import math
import itertools

# Input data: cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create the problem
prob = pulp.LpProblem("Multiple_Traveling_Salesman_Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, upBound=len(cities)-1, cat='Continuous')

# Objective
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in cities for j in cities if i != j)

# Constraints
# Each city must be visited exactly once and leave exactly once
for j in cities:
    prob += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for i in cities if i != j) == 1

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + len(cities) * x[(i, j)] <= len(cities) - 1

# Number of vehicles
prob += pulp.lpSum(x[(0, j)] for j in cities if j != 0) == 2  # We have 2 robots (vehicles)

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Fetch the results
tours = []
if status == 1:  # Optimal solution found
    for i in cities:
        if i == 0:
            for j in cities:
                if pulp.value(x[(i, j)]) == 1:
                    tour = [i]
                    while j != 0:
                        tour.append(j)
                        next_cities = [k for k in cities if pulp.value(x[(j, k)]) == 1]
                        if next_cities:
                            j = next_cities[0]
                        else:
                            break
                    tours.append(tour + [0])

    overall_cost = sum(euclidean_distance(tour[k], tour[k + 1]) for tour in tours for k in range(len(tour) - 1))
    for index, tour in enumerate(tours):
        tour_cost = sum(euclidean_distance(tour[k], tour[k+1]) for k in range(len(tour) - 1))
        print(f"Robot {index} Tour: {tour}")
        print(f"Robot {index} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("Failed to find an optimal solution.")