import pulp
import math

# Coordinates of the cities including depots
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27),
    14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two points
def euclidean_distance(id1, id2):
    return math.sqrt((cities[id1][0] - cities[id2][0])**2 + (cities[id1][1] - cities[id2][1])**2)

num_cities = len(cities)
num_robots = 2

model = pulp.LpProblem("MultiDepotTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat=pulp.LpBinary)

# Objective: Minimize the total traveling cost
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j), "Total Travel Cost"

# Constraint: Each non-depot city is visited exactly once
for j in range(2, num_cities):
    model += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1

# Constraint: Departing from each non-depot city exactly once
for i in range(2, num_cities):
    model += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) == 1

# Constraint: Robot starting conditions
for k in range(num_robots):
    model += pulp.lpSum(x[k, j] for j in range(num_cities) if j != k) == 1

# Constraint: Prevent subtours
for i in range(2, num_cities):
    for j in range(2, num_cities):
        if i != j:
            model += pulp.lpSum(x[i, k] for k in range(num_cities) if k != i and k != j) - pulp.lpSum(x[k, j] for k in range(num_cities) if k != i and k != j) >= 0

model.solve()

# Checking the status of the solution
status = pulp.LpStatus[model.status]
if status == 'Optimal':
    print("Optimal solution found.")
    total_cost = 0
    for k in range(num_robots):
        tour = []
        current_city = k
        while True:
            tour.append(current_city)
            next_cities = [j for j in range(num_cities) if x[current_city, j].varValue == 1]
            if not next_cities:
                break
            current_city = next_cities[0]
        tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Travel Cost for Robot {k}: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print(f"No optimal solution, status is {status}")