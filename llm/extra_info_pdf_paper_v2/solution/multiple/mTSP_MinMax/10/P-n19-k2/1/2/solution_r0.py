import math

# City coordinates with the depot as the first element
coords = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
          (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Function to calculate Euclidean distance between two cities
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0]) ** 2 + (coords[i][1] - coords[j][1]) ** 2)

# Number of robots
num_robots = 2

# Assign cities to robots, attempt to divide evenly
cities_per_robot = len(coords[1:]) // num_robots
assignments = [coords[1:i * cities_per_robot + 1] for i in range(1, num_robots)]
assignments.append(coords[num_robots * cities_per_robot + 1:])

tours = []
costs = []

# Finding tours for each robot
for idx, assignment in enumerate(assignments):
    current_city = 0
    tour = [0]
    total_cost = 0
    visited = set(tour)

    # Sort cities by nearest to the depot or last city added in tour for a greedy choice
    while len(tour) < len(assignment) + 1:
        next_city = min((i for i in range(1, len(coords)) if i not in visited), 
                        key=lambda x: distance(current_city, x))
        visited.add(next_city)
        tour.append(next_city)
        total_cost += distance(current_city, next_city)
        current_city = next_city

    # Return to depot
    total_cost += distance(current_city, 0)
    tour.append(0)

    tours.append(tour)
    costs.append(total_cost)

# Calculate maximum travel cost
max_cost = max(costs)

# Output results
for idx, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")

print(f"Maximum Travel Cost: {round(max_cost, 2)}")