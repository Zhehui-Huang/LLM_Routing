import math

# Coordinates of the depot and cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Define number of robots
robots = 4

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Simple function to assign cities to robots 
def assign_cities_to_robots(robots, coordinates):
    tours = {i: [0] for i in range(robots)}  # Start each tour at the depot
    for city in range(1, len(coordinates)):  # Assigning cities to each robot in round robin fashion
        robot = (city - 1) % robots
        tours[robot].append(city)
    for key in tours:
        tours[key].append(0)  # Return to depot
    return tours

tours = assign_cities_to_robots(robots, coordinates)

# Compute the cost for each tour
tour_costs = {}
max_cost = 0

for key, tour in tours.items():
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i+1])
    tour_costs[key] = cost
    max_cost = max(max_cost, cost)
    print(f"Robot {key} Tour: {tour}")
    print(f"Robot {key} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")