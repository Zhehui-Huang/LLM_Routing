import math
import pulp

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Calculate Euclidean distances between all pairs of cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

num_cities = len(cities)
num_robots = 2

# Creating a problem variable to minimize the maximum cost
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# x[i][j][k]: robot k travels from city i to city j (binary variables)
x = pulp.LpVariable.dicts("x", 
                          ((i, j, k) for i in range(num_cities) 
                                      for j in range(num_cities) 
                                      if i != j for k in range(num_robots)), 
                          cat='Binary')

# u[i]: prevents subtours
u = pulp.LpVariables("u", range(1, num_cities), lowBound=0, upBound=num_cities-1, cat='Continuous')
max_distance = pulp.LpVariable("max_distance")

# The objective function to minimize the maximum cost
prob += max_distance

# Constraints
# Each city must be visited exactly once by one robot
for j in range(1, num_cities):
    prob += sum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# Each robot must leave and return to the depot
for k in range(num_robots):
    prob += sum(x[0, j, k] for j in range(1, num_cities)) == 1
    prob += sum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                prob += u[i] - u[j] + (num_cities-1) * x[i, j, k] <= num_cities-2

# Limit each robot's distance to not exceed the max distance
for k in range(num_robots):
    prob += sum(calc_distance(i, j) * x[i, j, k] for i in range(num_cities)
                for j in range(num_cities) if i != j) <= max_cost

# Solve the problem
prob.solve()

# Print results
for k in range(num_robots):
    path = []
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and pulp.value(x[i, j, k]) == 1:
                path.append((i, j))

    # Order the path (you may need to reorder the elements in the path tuple)
    tour = [0]
    next_location = path[0][1]
    while next_location != 0:
        tour.append(next_location)
        next_location = [z[1] for z in path if z[0] == next_location][0]

    tour.append(0)

    distance = sum(calc_distance(tour[z], tour[z+1]) for z in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {distance}")

max_cost_value = max(sum(calc_distance(tour[z], tour[z+1]) for z in range(len(tour)-1)) for k in range(num_robots))
print(f"Maximum Travel Cost: {max_cost_value}")