import pulp
import math

# Cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

n = len(cities)  # number of cities
depots = [0, 1, 2, 3]
robots = len(depots)

# Calculate the Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Creating a cost (distance) matrix
costs = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the optimization problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in depots),
                          cat=pulp.LpBinary)

# Objective function: Minimize the total distance traveled by all robots
problem += pulp.lpSum(costs[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in depots)

# Constraints
# Each non-depot city is visited exactly once by exactly one robot
for j in range(n):
    if j not in depots:
        problem += pulp.lpSum(x[i][j][k] for i in range(n) for k in depots) == 1

# Each robot starts and ends at its depot
for k in depots:
    problem += pulp.lpSum(x[k][j][k] for j in range(n)) == 1
    problem += pulp.lpSum(x[j][k][k] for j in range(n)) == 1

# Maintain flow: for non-depot cities
for k in depots:
    for i in range(n):
        if i not in depots:
            problem += (pulp.lpSum(x[i][j][k] for j in range(n)) - 
                        pulp.lpSum(x[j][i][k] for j in range(n))) == 0

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
else:
    print("No optimal solution available. Status:", pulp.LpStatus[status])

# Extracting the solution
overall_cost = 0
for k in depots:
    cur_node = k
    tour = [cur_node]
    tour_cost = 0
    while True:
        for j in range(n):
            if pulp.value(x[cur_node][j][k]) == 1:
                next_node = j
                tour_cost += costs[cur_node][next_node]
                cur_node = next_node
                tour.append(cur_node)
                break
        if curslice == k:
            break
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")