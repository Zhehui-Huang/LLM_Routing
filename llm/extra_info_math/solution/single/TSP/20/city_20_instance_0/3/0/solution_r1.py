import pulp
import math

# City coordinates
coordinates = [
    (8, 11),   # depot
    (40, 6),
    (95, 33),
    (80, 60),
    (25, 18),
    (67, 23),
    (97, 32),
    (25, 71),
    (61, 16),
    (27, 91),
    (91, 46),
    (40, 87),
    (20, 97),
    (61, 25),
    (5, 59),
    (62, 88),
    (13, 43),
    (61, 28),
    (60, 63),
    (93, 15)
]

n = len(coordinates)

# Calculate the Euclidean distance between each pair of nodes
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(cost[i][j] * x[i,j] for i in range(n) for j in range(n) if i != j)

# Constraints ensuring each city is left and entered exactly once
for i in range(n):
    model += pulp.lpSum(x[i,j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j,i] for j in range(n) if i != j) == 1

# Subtour elimination constraints using lazy constraints could be added here if cycles were found without them.
# However, as an initial approach, we usually solve without them and add them iteratively if needed.

# Solve the problem
model.solve()

# Gathering results if an optimal solution was found
if pulp.LpStatus[model.status] == 'Optmpal':
    # Get the route from the solution
    non_zero_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    
    # Reformulate the list to start from the depot city and reconstruct the path
    tours = []
    for starting_point in non_zero_edges:
        if starting_manager[0] == 0: # start at depot
            tour = [starting_point]
            while tour[-1][1] != 0: # terminate at depot
                next_city = tour[-1][1]
                next_step = [edge for edge in non_zero_edges if edge[0] == next_city]
                if next_step:
                    tour.append(next_step[0])
            tours.append(tour)

    # Calculate the cost of the tour
    total_cost = sum(cost[edge[0]][edge[1]] for tour in tours for edge in tour)
    
    # Display the results
    print("Tour:", [edge[0] for edge in tours[0]] + [0])  # Includes the return to the depot
    print("Total travel cost:", total_cost)

else:
    print("No optimal solution found.")