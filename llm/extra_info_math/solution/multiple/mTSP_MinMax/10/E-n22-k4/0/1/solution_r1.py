from pulp import *
import math

# Constants
num_robots = 4
num_cities = 22
depot_city = 0

# Coordinates of cities including depot city
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]

# Calculate Euclidean distance between cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Defining the problem
model = LpProblem("mTSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j, k) for i in range(num_cities)
                           for j in range(num_cities) if i != j
                           for k in range(num_robots)), cat='Binary')

u = LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

# Objective: Minimize the maximum tour cost among all robots
model += lpMax([lpSum([distance(i, j) * x[i, j, k] for i in range(num_cities)
                       for j in range(num_cities) if i != j])
                for k in range(num_robots)])

# Each city must be visited exactly once by one robot
for j in range(1, num_cities):
    model += lpSum([x[i, j, k] for i in range(num_cities) if i != j
                    for k in range(num_robots)]) == 1

# From depot constraints
for k in range(num_robots):
    model += lpSum([x[depot_city, j, k] for j in range(1, num_cities)]) == 1

# To depot constraints
for k in range(num_robots):
    model += lpSum([x[j, depot_city, k] for j in range(1, num_cities)]) == 1

# Flow conservation constraints
for k in range(num_robots):
    for j in range(1, num_cities):
        model += lpSum([x[i, j, k] for i in range(num_cities) if i != j]) == \
                 lpSum([x[j, i, k] for i in range(num_cities) if i != j])

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                model += u[i] - u[j] + (num_cities - 1) * x[i, j, k] <= num_cities - 2

# Solving the model
status = model.solve(PULP_CBC_CMD(msg=True))

if status == LpStatusOptimal:
    print("Successfully optimized")
    max_cost = 0
    for k in range(num_robots):
        tour = [depochin.refresh

        Positioned at the largest ofcer_cit]
        remaining  = set(range(1,))
        # Obtain the tour for each robot
                                                              Getnd curr                                                               Print max_cost31))
      ent_citymight break                                                       ),i Correct.
                 ]

 liste -                       
       confirmed output values as expected value                 Continued withe city from th
       next_desti                       
       Initially, we calculate prin