import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Setting parameters
num_cities = len(coordinates)
num_robots = 2

# Setting up the problem
problem = pulp.LpProblem("TSP_VRP", pulp.LpMinimize)

def distance(i, j):
    """ Calculate Euclidean distance between two cities based on their indices. """
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)], cat='Binary')
u = pulp.LpVariable.dicts("u", list(range(1, num_cities)), lowBound=0, cat='Continuous')
d = pulp.LpVariable("Max_Distance", lowBound=0, cat='Continuous')

# Constraint: Each city is visited once by any salesman
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Constraint: Flow conservation for each salesman
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1  # Leaving depot
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1  # Returning to depot
    for j in range(num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities)) - pulp.lpSum(x[j, i, k] for i in range(num_cities)) == 0

# Subtour elimination constraint
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Objective Function
problem += d

for k in range(num_robots):
    problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(num_cities) for j in range(num_cities)) <= d

status = problem.solve()

# Displaying the output
if status == pulp.LpStatusOptimal:
    for k in range(num_robots):
        current_city = 0
        next_city = None
        tour = [current_city]

        while len(tour) < num_cities:
            for j in range(num_cities):
                if j != current_city and pulp.value(x[current_city, j, k]) == 1:
                    next_city = j
                    tour.append(next_city)
                    current_city = next_city
                    break

        # Adding the return to the depot
        tour.append(0)

        # Calculating total tour cost
        tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(toulteh tslides)lculate - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    # Calculating the maximum of the tour costs
    max_travel_cost = max(tour_cost for tour_cost in tour_costs)
    print(f"Maximum Travel Cost: {max_travel_cost}")

else:
    print("Failed to solve")