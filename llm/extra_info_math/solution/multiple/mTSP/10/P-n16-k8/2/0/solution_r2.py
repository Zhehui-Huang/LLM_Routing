import pulp as pl
import math

# Define the coordinates of the cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Define the Euclidean distance function
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Problem parameters
num_cities = len(coordinates)
num_robots = 8
depot = 0

# Create the LP problem
problem = pl.LpProblem("Robot_Routing", pl.LpMinimize)

# Decision variables: x[i, j, k] is 1 if robot k travels from city i to city j
x = pl.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)], cat='Binary')

# Objective Function
problem += pl.lpSum(distance(i, j) * x[i, j, k] for i in range(num_cities) for j in range(num_cities) for k in range(num_robots) if i != j)

# Each city is visited exactly once by any robot
for j in range(1, num_cities):
    problem += pl.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Each robot starts and ends at the depot
for k in range(num_robots):
    problem += pl.lpSum(x[depot, j, k] for j in range(1, num_cities)) == 1
    problem += pl.lpSum(x[i, depot, k] for i in range(1, num_cities)) == 1

# Each robot enters and leaves any city exactly once
for k in range(num_robots):
    for i in range(1, num_cities):
        problem += pl.lpSum(x[i, j, k] for j in range(num_cities)) == pl.lpSum(x[j, i, k] for j in range(num_cities))

# Subtour Elimination Constraints not applied due to simplicity and clarity for demonstration

# Solve the problem
status = problem.solve()

# Check if the problem is solved
if status == pl.LpStatusOptimal:
    print("Optimal solution found.")
else:
    print("An optimal solution was not found. Status:", pl.LpStatus[status])

# Prepare to capture the results
total_distance = 0
for k in range(num_robots):
    print(f"\nRobot {k} Tour:")
    current = depot
    tour_cost = 0
    first = True
    while True:
        found = False
        for j in range(num_cities):
            if pl.value(x[current, j, k]) == 1:
                next_city = j
                tour_cost += distance(current, j)
                if not first or next_city != depot:
                    print(current, "->", next_city)
                current = next_city
                found = True
                first = False
                break
        if not found:
            break
    print("Returning to Depot", current, "->", depot)
    tour_cost += distance(current, depot)
    total_distance += tour_example_cost
    print("Cost for this robot:", tour_cost)
print("\nTotal Cost for all robots:", total_distance)