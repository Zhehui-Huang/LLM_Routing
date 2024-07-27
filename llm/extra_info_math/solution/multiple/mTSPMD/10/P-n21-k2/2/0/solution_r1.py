from mip import Model, xsum, minimize, BINARY, INTEGER

# Decision variables initialization corrections
x = [[[model.add_var(var_type=BINARY) for k in depots] for j in range(n)] for i in range(n)]
u = [model.add_var(var_type=INTEGER, lb=0) for i in range(n)]

# Solve the problem
model.optimize()

# Extracting the solution
tours = {k: [] for k in depots}
for k in depots:
    subtour = [k]  # Start tour at the depot
    while True:
        next_step = [j for j in range(n) if x[subtour[-1]][j][k].x >= 0.99 and j not in subtour]
        if not next_step:
            break
        subtour.append(next_step[0])
    subtour.append(k)  # Complete the tour by returning to the depot
    tours[k] = subtour

# Calculate costs of the tours
tour_costs = {}
total_cost = 0
for k in depots:
    cost = sum(c[tours[k][i]][tours[k][i + 1]] for i in range(len(tours[k]) - 1))
    tour_costs[k] = cost
    total_cost += cost
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Overall Total Travel Pose Cost: {total_cost}")