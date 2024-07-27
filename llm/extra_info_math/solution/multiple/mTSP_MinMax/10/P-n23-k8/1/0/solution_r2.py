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
    dx = cities[city1][0] - cities[city2][0]
    dy = cities[city1][1] - cities[city2][1]
    return math.sqrt(dx * dx + dy * dy)

# Create the LP problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots)), cat='Binary')

# Objective function
prob += pulp.lpSum(x[i, j, k] * distance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(num_robots))

# Constraints
# Each city visited exactly once and only by one salesman
for j in range(1, num_cities):
    prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j for k in range(num_robots)) == 1

# Flow continuity
for k in range(num_robots):
    # Start from depot
    prob += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    # Return to depot
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1
    for j in range(1, num_cities):
        prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) == pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j)

# Solve the model
prob.solve()

# Print results
if pulp.LpStatus[prob.status] == 'Optimal':
    print("Optimal solution found.")
    for k in range(num_robots):
        tour = [0]
        last_city = 0
        while True:
            next_city = [j for j in range(num_cities) if pulp.value(x[last_city, j, k]) == 1]
            if not next_city:
                break
            next_city = next_city[0]
            if next_city == 0:
                break
            tour.append(next_city)
            last_city = next_city
        tour.append(0)
        print(f"Robot {k} Tour: {tour}")
        tour_dist = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        print(f"Robot {k} Tour Distance: {tour_dist}")
else:
    print("No optimal solution available.")