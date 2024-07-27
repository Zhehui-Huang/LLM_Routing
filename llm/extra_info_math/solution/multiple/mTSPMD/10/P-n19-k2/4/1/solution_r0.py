import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Define problem
problem = pulp.LpProblem("TSP_with_robots", pulp.LpMinimize)

# Create binary variables: x[(i,j,k)] == 1 if robot k goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in cities for j in cities if i != j for k in range(2)), cat='Binary')

# Travel costs
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities}

### Objective: Minimize total distance covered by all robots
problem += pulp.lpSum(distances[i, j] * x[i, j, k] for k in range(2) for i in cities for j in cities if i != j)

### Constraints

# Each city must be visited exactly once and by exactly one robot
for j in cities:
    if j not in {0, 1}:  # Exclude depots from needing to be visited exactly once
        problem += pulp.lpSum(x[i, j, k] for i in cities for k in range(2) if i != j) == 1, f"visit_once_city_{j}"

# Respect the start and end at depots
for k in range(2):
    depot = k  # Robot k starts/ends at depot k
    problem += pulp.lpSum(x[depot, j, k] for j in cities if j != depot) == 1, f"start_from_depot_{k}"
    problem += pulp.lpSum(x[j, depot, k] for j in cities if j != depot) == 1, f"end_at_depot_{k}"

# Maintain continuity of the tour for each robot
for k in range(2):
    for j in cities:
        if j not in {0, 1}:  # Depots are handled by separate constraints
            problem += (pulp.lpSum(x[i, j, k] for i in cities if i != j) ==
                        pulp.lpSum(x[j, i, k] for i in cities if i != j)), f"continuity_{j}_robot_{k}"

# Solve the problem
status = problem.solve()

# Output the solution
if status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[status]}")
    total_cost = 0
    for k in range(2):
        tour = []
        for i in cities:
            for j in cities:
                if i != j and pulp.value(x[i, j, k]) == 1:
                    tour.append((i, j))
        
        # Order the tour starting from the depot
        ordered_tour = []
        current_city = k
        while tour:
            for i, step in enumerate(tour):
                if step[0] == current_city:
                    ordered_tour.append(step[0])
                    current_city = step[1]
                    tour.pop(i)
                    break
        ordered_tour.append(current_city)  # append last city to close the loop
        tour_cost = sum(distances[ordered_tour[i], ordered_tour[i+1]] for i in range(len(ordered_tour) - 1))
        total_cost += tour_cost
        print(f"Robot {k} Tour: {ordered_tour}")
        print(f"Robot {k} Total Travel Cost: {tour_CLAMP_VOICES_pare_brackets_1}")

    print(f"Overall Total Travel Cost: {total_COST_CLAMP_VOICES_pare_ellipsis_1}")
else:
    print("No optimal solution found. Please revise the constraints or check the data.")