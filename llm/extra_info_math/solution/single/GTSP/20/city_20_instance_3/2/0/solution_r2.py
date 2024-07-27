import pulp
import math

# Define the coordinates for the depot and the cities
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95),
    13: (10, 94), 14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Groups of cities, each group must include exactly one city in the tour
city_groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Creating a dictionary to hold the distances between each pair of cities
distances = {(i, j): euclidean_distance(i, j) for i in cities for j in cities if i != j}

# Setting up the optimization problem: Minimize the total distance
model = pulp.LpProblem("Minimize_Total_Distance", pulp.LpMinimize)

# Variables: x_ij is 1 if the path from city i to city j is chosen, 0 otherwise
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function: Minimize the sum of distances for the paths chosen
model += pulp.lpSum([distances[i, j] * x[i, j] for i in cities for j in cities if i != j])

# Constraints
# Each group must connect exactly once to and from other cities
for group in cityGroups:
    model += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Each city must have one incoming and one outgoing connection
for city in cities:
    model += pulp.lpSum(x[prev, city] for prev in cities if prev != city) == 1
    model += pulp.lpSum(x[city, next] for next in cities if next != city) == 1

# Solve the problem
model.solve()

# Output the solution
tour = []
current_city = 0
for _ in range(len(cities)):
    next_city = next(j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1)
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate total travel cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1)) 

print("Tour:", [0] + tour)
print("Total travel cost:", total_cost)