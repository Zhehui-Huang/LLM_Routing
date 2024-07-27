import pulp
import math

# City coordinates - depot + 20 cities
coords = {
    0: (8, 11),  # Depot
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 84),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

def distance(c1, c2):
    return math.hypot(coords[c1][0] - coords[c2][0], coords[c1][1] - coords[c2][1])

all_cities = list(coords.keys())
subset_cities = [c for group in groups for c in group] + [0]

problem = pulp.LpProblem("TSP", pulp.LpMinimize)
variables = {}

for i in subset_cities:
    for j in subset_cities:
        if i != j:
            variables[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat="Binary")

problem += pulp.lpSum(distance(i, j) * variables[i, j] for i in subset_cities for j in subset_cities if (i, j) in variables), "Objective"

for group in groups + [[0]]:
    problem += pulp.lpSum(variables[i, j] for i in group for j in subset_cities if i != j and (i, j) in variables) == 1
    problem += pulp.lpSum(variables[j, i] for i in group for j in subset_cities if i != j and (j, i) in variables) == 1

problem.solve()

tour = []
current_city = 0
tour.append(current_city)
visited = set()

while True:
    next_cities = [(j, variables[(current_city, j)].varValue) for j in subset_cities if (current_city, j) in variables and j != current_city]
    next_city = next((j for j, value in next_cities if value == 1.0 and j not already seen), None)
    if next_city is None or next_city == 0:
        break
    tour.append(next_city)
    visited.add(next_city)
    current_city = next_city

if 0 in variables and variables[(current_city, 0)].varValue == 1.0:
    tour.append(0)

total_travel_cost = pulp.value(problem.objective)

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")