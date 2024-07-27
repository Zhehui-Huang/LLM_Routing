import pulp as pl
import math

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
all_cities = list(cities.keys())
num_cities = len(all_cities)

# Calculate Euclidean distance between two cities
def calc_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

num_robots = 8
start_depot = 0

# Create the problem
prob = pl.LpProblem("MDMTSP", pl.LpMinimize)

# Variables
x = pl.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')

# Objective function: Minimize total travel cost
prob += pl.lpSum(x[i, j] * calc_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Constraints
# Each customer city must be visited exactly once
for j in all_cities[1:]:
    prob += pl.lpSum(x[i, j] for i in all_cities if i != j) == 1

# Each city must be exited exactly once
for i in all_cities[1:]:
    prob += pl.lpSum(x[i, j] for j in all_cities if i != j) == 1

# Number of exiting edges from depot must be equal to the number of robots
prob += pl.lpSum(x[start_depot, j] for j in all_cities if start_depot != j) == num_robots

# Subtour elimination
u = pl.LpVariable.dicts('u', all_cities, lowBound=0, upBound=num_cities-1, cat='Continuous')
for i in all_cities:
    for j in all_cities:
        if i != j and i != start_depot and j != start_depot:
            prob += u[i] - u[j] + num_cities * x[i, j] <= num_cities-1

# Solve the problem
prob.solve(pl.PULP_CBC_CMD(msg=False))

# Generate tours based on the solution
tours = {}
for k, v in x.items():
    if pl.value(v) == 1:
        if k[0] in tours:
            tours[k[0]].append(k[1])
        else:
            tours[k[0]] = [k[1]]

def find_tour(start_city, tours):
    tour = []
    next_city = start_city
    while next_city in tours and tours[next_city]:
        next_city = tours[next_city][0]
        tour.append(next_city)
        tours[next_city] = []  # Clear the city to prevent re-visiting
    return tour

# Interpreting and printing results
overall_cost = 0
for i in range(num_robots):
    tour = find_tour(start_depot, tours)
    tour_cost = sum(calc_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    overall_cost += tour_cost
    print(f"Robot {i} Tour: {[start_depot] + tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")