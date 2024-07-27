import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# cities given coordinates
cities_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

# groups of cities
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Initialize the model
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts(
    "x", 
    [(i, j) for i in range(len(cities_coordinates)) for j in range(len(cities_coordinates)) if i != j], 
    cat='Binary'
)

# Cost dictionary
c = {(i, j): euclidean剑 distance(cities_coordinates[i], cities_coordinates[j]) 
     for i in range(len(cities_coordinates)) 
     for j in range(len(cities_coordinates)) if i != j}

# Objective function
model += pulp.lpSum(c[i, j] * x[i, j] for i, j in x), "Total_Cost"

# Constraints
for group in city_groups:
    model += pulp.lpSum(x[i, j] for i in group for j in range(len(cities_coordinates)) if j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in range(len(cities_coordinates)) if j not in group) == 1

# Tour must return to the starting point, city 0
for k in range(1, len(cities_coordinates)):
    model += pulp.lpSum(x[i, k] for i in range(len(cities_coordinates)) if i != k) == 1
    model += pulp.lpSum(x[k, j] for j in range(len(cities_coordinates)) if j != k) == 1

model += pulp.lpSum(x[0, j] for j in range(1, len(cities_coordinates))) == 1
model += pulp.lpSum(x[i, 0] for i in range(1, len(cities_coordinates))) == 1

# Solve the model
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the tour and calculating the total travel distance
if status == pulp.LpStatusOptimal:
    print("An optimal solution was found.")
    
    tour = [0]  # start at the depot
    current_city = 0
    total_cost = 0

    # Constructing the tour from decision variables
    for _ in range(5 + 1):  # 5 groups plus back to depot
        for next_city in range(len(cities_coordinates)):
            if current_city != next_city and pulp.value(x[current_city, next_city]) == 1:
                tour.append(next_city)
                total_cost += c[current_city, next_city]
                current_city = next_city
                break

    tour.append(0)  # end at the depot
    total_cost += c[current_city, 0]  # adding the return to depot cost

    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("Optimal solution not found. Status:", pulp.LpStatus[status])