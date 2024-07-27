import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

# Coordinates of cities including the depot
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39),
}

# Function to calculate Euclidean distance
def distance(c1, c2):
    return math.hypot(cities[c1][0] - cities[c2][0], cities[c1][1] - cities[c2][1])

n = len(cities)  # number of cities including the depot

# Create the problem
prob = LpoProblem("TSP", LpMinimize)

# Decision variables: x_ij is 1 if the path from city i to city j is chosen
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective function: Minimize the sum of distances for the chosen paths
prob += lpSum(x[i, j] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints that each city is arrived at and departed from exactly once
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Depart_from_{i}"
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Arrive_to_{i}"

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Check if a valid solution has been found
if LpStatus[prob.status] == 'Optimal':
    # Extract the tour
    tour = []
    start = 0
    next_city = start
    while True:
        for j in range(n):
            if j != next_city and x[next_city, j].varValue == 1:
                tour.append(next_city)
                next_city = j
                break
        if next_city == start:
            break
    tour.append(start)  # Complete the tour by returning to the depot

    # Calculate the total travel cost of the tour
    total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    # Display the results
    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution found.")