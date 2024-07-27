import pulp
import math

# Define cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Define groups of cities ("clusters")
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Calculate Euclidean distance between each pair of cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)


# Create the ILP problem
problem = pulp.LpProblem('TSP_GroupProblem', pulp.LpMinimize)

# Decision variables: x_ij where i, j are cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: minimize the sum of travel costs over all routes
problem += pulp.lpSum(x[i, j] * distance(i, j) for i in cities for j in cities if i != j)

# Constraints

# Each group must connect outside exactly once and receive one connection
for group in groups:
    # Sum of outgoing connections from groups to the rest of the graph should be one
    problem += pulp.lpSum(x[i, j] for i in group for j in set(cities) - set(group)) == 1
    # Sum of incoming connections to groups from the rest of the graph should be one
    problem += pulp.lpSum(x[j, i] for i in group for j in set(cities) - set(group)) == 1

# - Ensure every city except the depot city has one entrance and one exit
for city in cities:
    if city != 0:  # Except depot city
        problem += pulp.lpSum(x[j, city] for j in cities if j != city) == 1
        problem += pulp.lpSum(x[city, j] for j in cities if j != city) == 1

# Including depot city constraints (since it must start and end the tour)
problem += pulp.lpSum(x[0, j] for j in cities if j != 0) == 1
problem += pulp.lpSum(x[j, 0] for j in cities if j != 0) == 1

# Solve the problem
problem.solve()

# Output the result
if pulp.LpStatus[problem.status] == 'Optimal':
    print(f"Optimal solution found")
    tour = []
    cur_city = 0
    for _ in range(len(cities)):
        tour.append(cur_city)
        for next_city in cities:
            if cur_city != next_city and pulp.value(x[cur_city, next_city]) == 1:
                cur_city = next_city
                break
    tour.append(0)  # Return to depot

    # Calculate the total travel cost from the tour
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution available.")