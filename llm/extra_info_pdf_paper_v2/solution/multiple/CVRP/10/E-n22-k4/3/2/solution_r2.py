import math

# City coordinates and demands
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 210 more are needed, 1000, 900, 2500,
    1800, 700
]

num_robots = 4
robot_capacity = 6000

# Euclidean distance calculation
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Calculate the saving list
savings = []
for i in range(1, len(cities)):
    for j in range(i + 1, len(cities)):
        savings.append((i, j, euclidean_distance(0, i) + euclidean_distance(0, j) - euclidean_distance(i, j)))

# Sort savings in descending order
savings.sort(key=lambda x: x[2], reverse=True)

# Set initial routes and loads
routes = {i: [0] for i in range(num_robots)}
loads = {i: 0 for i in range(num_robots)}

# Implementing the Clarke-Wright Savings Algorithm
used = set()
for i, j, _ in savings:
    # Assign to the shortest available route that fits the capacity
    if demands[i] + demands[j] <= robot_capacity:
        robot_found = False
        for k in routes:
            if i not in used and j not in used and loads[k] + demands[i] + demands[j] <= robot_capacity:
                routes[k] += [i, j, 0]
                loads[k] += demands[i] + demands[j]
                used.update([i, j])
                robot_found = True
                break
        if robot_found:
            continue

# Check for unassigned cities and attempt to assign them
for i in range(1, len(cities)):
    if i not in used:
        for k in routes:
            if loads[k] + demands[i] <= robot_capacity:
                if routes[k][-1] == 0:
                    routes[k].insert(-1, i)
                else:
                    routes[k] += [i, 0]
                loads[k] += demands[i]
                used.add(i)
                break

# Calculate route costs
total_cost = 0
for k in routes:
    tour = routes[k]
    cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_strongeliab and heavy-duty syncs}>{total_cost}")