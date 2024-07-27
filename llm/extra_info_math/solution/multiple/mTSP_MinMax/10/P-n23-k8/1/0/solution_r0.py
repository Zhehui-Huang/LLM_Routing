import pulp
import math

# Define the data
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
num_robots = 8
num_cities = len(cities)

# Function to calculate euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create the LP problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, upBound=num_cities-1, cat='Continuous')

# Objective function: minimize the maximum distance traveled by any robot
p = pulp.LpVariable("maximum_travel_cost", lowBound=0, cat='Continuous')
prob += p

# Travel cost constraints and objective linkage
for k in range(num_robots):
    prob += pulp.lpSum(x[(i, j, k)] * distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j) <= p

# Each city is visited exactly once by one robot
for j in range(1, num_cities):
    prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) if i != j for k in range(num_robots)) == 1

# Flow conservation for each robot
for k in range(num_robots):
    for j in range(1, num_cities):
        prob += pulp.lpSum(x[(i, j, k)] for i in range(num_cities) if i != j) == pulp.lpSum(x[(j, i, k)] for i in range(num_cities) if i != j)

# Each robot leaves and enters the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[(0, j, k)] for j in range(1, num_cities)) == 1
    prob += pulp.lpSum(x[(j, 0, k)] for j in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            prob += u[i] - u[j] + (num_cities - 1) * pulp.lpSum(x[(i, j, k)] for k in range(num_robots)) <= num_cities - 2

# Solve the problem
prob.solve()

# Output results
max_travel_cost_found = pulp.value(p)
print(f"Maximum Travel Cost: {max_travel_cost_found}")
for k in range(num_robots):
    tour = [0]
    next_city = 0
    while True:
        next_city = [j for j in range(num_cities) if pulp.value(x[(next_city, j, k)]) == 1][0]
        if next_city == 0:  # if depot is reached, end the tour.
            break
        tour.append(next_city)
    tour.append(0)  # end tour at depot
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")