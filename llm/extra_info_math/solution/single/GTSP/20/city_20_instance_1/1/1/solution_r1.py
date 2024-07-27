import pulp
import math

# City positions (x, y)
positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Groups of cities
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Define utility function for Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# All cities including depot
cities = list(range(len(positions)))

# Create the LP problem to minimize the total tour cost
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables x_ij, where i, j are distinct cities
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function to minimize the total distance traveled
problem += pulp.lpSum(euclidean_distance(positions[i], positions[j]) * x[i, j] for i in cities for j in cities if i != j),
            "Minimize_Total_Distance"

# Each group should connect to and from the rest of the network
for number_groups, group in enumerate(groups):
    problem += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"One_outgoing_from_group_{number_groups}"
    problem += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, f"One_incoming_to_group_{number_groups}"

# Each non-depot city should have exactly one arrival and one departure, ensuring it's included in the tour
for city in cities:
    if city != 0:  # Excluding the depot for these constraints
        problem += pulp.lpSum(x[city, j] for j in cities if j != city) == 1, f"Depart_from_{city}"
        problem += pulp.lpSum(x[j, city] for j in cities if j != city) == 1, f"Arrive_at_{city}"

# Connectivity from and to the depot
problem += pulp.lpSum(x[0, j] for j in cities if j != 0) == 1, "Leave_Depot"
problem += pulp.lpSum(x[j, 0] for j in cities if j != 0) == 1, "Return_to_Depot"

# Solve the problem
problem.solve()

# Extract the solution
if pulp.LpStatus[problem.status] == 'Optimal':
    # Finding the tour path by selecting active roads from the solution
    path = [0]  # Start at the depot
    next_city = next(j for j in cities if x[0, j].value() == 1)
    
    while next_city != 0:
        path.append(next->[j_city])
        next_city = next(j for j in cities if x[next_city, j].value() == 1)
    
    path.append(0)  # End at the depot

    # Calculating total distance of the tour
    total_distance = sum(euclidean_distance(positions[path[i]], positions[path[i + 1]]) for i in range(len(path) - 1))
    
    print("Tour:", path)
    print("Total travel cost:", total_distance)
else:
    print("No optimal solution found.")