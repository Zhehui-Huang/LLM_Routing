import gurobipy as gp
from gurobipy import GRB
import numpy as np
import matplotlib.pyplot as plt

# Example data
num_customers = 7
vehicle_capacity = 50
customer_demands = [0, 10, 20, 15, 25, 10, 5, 15]  # including depot demand (0)
depot = 0

# Generate random coordinates for customers including the depot
np.random.seed(1)
customer_locations = np.random.rand(num_customers + 1, 2) * 100

# Calculate distance matrix
distance_matrix = np.zeros((num_customers + 1, num_customers + 1))
for i in range(num_customers + 1):
    for j in range(num_customers + 1):
        if i != j:
            distance_matrix[i, j] = np.linalg.norm(customer_locations[i] - customer_locations[j])

# Number of vehicles
num_vehicles = int(np.ceil(sum(customer_demands) / vehicle_capacity))

# Create the model
model = gp.Model("CVRP")

# Decision variables
x = model.addVars(num_vehicles, num_customers + 1, num_customers + 1, vtype=GRB.BINARY, name="x")

# Objective function: minimize total travel cost
model.setObjective(gp.quicksum(distance_matrix[i, j] * x[v, i, j]
                               for v in range(num_vehicles)
                               for i in range(num_customers + 1)
                               for j in range(num_customers + 1) if i != j), GRB.MINIMIZE)

# Degree constraints: each customer is visited exactly once
model.addConstrs((gp.quicksum(x[v, i, j] for v in range(num_vehicles) for i in range(num_customers + 1) if i != j) == 1
                  for j in range(1, num_customers + 1)), name="degree")

# Depot constraints: each vehicle leaves the depot once
model.addConstrs((gp.quicksum(x[v, depot, j] for j in range(1, num_customers + 1)) == 1
                  for v in range(num_vehicles)), name="leave_depot")

# Flow conservation constraints
model.addConstrs((gp.quicksum(x[v, i, j] for j in range(num_customers + 1) if i != j) ==
                  gp.quicksum(x[v, j, i] for j in range(num_customers + 1) if i != j)
                  for v in range(num_vehicles)
                  for i in range(num_customers + 1)), name="flow")

# Capacity constraints: total demand on each route does not exceed vehicle capacity
model.addConstrs((gp.quicksum(customer_demands[j] * x[v, i, j] for i in range(num_customers + 1) for j in range(1, num_customers + 1) if i != j) <= vehicle_capacity
                  for v in range(num_vehicles)), name="capacity")

# Sub-tour elimination constraints using MTZ formulation
u = model.addVars(num_vehicles, num_customers + 1, vtype=GRB.CONTINUOUS, name="u")
model.addConstrs((u[v, i] - u[v, j] + (num_customers + 1) * x[v, i, j] <= num_customers
                  for v in range(num_vehicles)
                  for i in range(1, num_customers + 1)
                  for j in range(1, num_customers + 1) if i != j), name="subtour")

# Optimize the model
model.optimize()

# Check if a solution was found
if model.status == GRB.OPTIMAL:
    print('Optimal solution found')
else:
    print('No optimal solution found')

# Visualization
plt.figure(figsize=(10, 8))
plt.scatter(customer_locations[:, 0], customer_locations[:, 1], c='red')
for i, txt in enumerate(range(num_customers + 1)):
    plt.annotate(txt, (customer_locations[i, 0], customer_locations[i, 1]))

for v in range(num_vehicles):
    for i in range(num_customers + 1):
        for j in range(num_customers + 1):
            if i != j and x[v, i, j].x > 0.5:
                plt.plot([customer_locations[i, 0], customer_locations[j, 0]],
                         [customer_locations[i, 1], customer_locations[j, 1]], 'b-')

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Capacitated Vehicle Routing Problem Solution')
plt.show()
