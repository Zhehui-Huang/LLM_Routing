import math

# Coordinates of cities including the depot
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demand at each city (index 0 is depot with no demand)
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800,
    100, 500, 600, 1200, 1300, 1300, 300, 900,
    2100, 1000, 900, 2500, 1800, 700
]

# Number of robots and their capacities
num_robots = 4
robot_capacity = 6000

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Create a distance matrix for all points
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

def assign_cities_to_robots():
    robot_tours = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    unvisited = set(range(1, len(coordinates)))  # skip the depot city at index 0
    robot_indices = list(range(num_robots))

    while unvisited:
        for r in robot_indices:
            if not unvisited:
                break
            min_distance = float('inf')
            next_city = None
            current_city = robot_tours[r][-1] if robot_tours[r] else 0

            for city in unvisited:
                if demands[city] + robot_loads[r] <= robot_capacity and distance_matrix[current_city][city] < min_distance:
                    min_distance = distance_matrix[current_city][city]
                    next_city = city

            if next_city is not None:
                robot_tours[r].append(next_city)
                unvisited.remove(next_city)
                robot_loads[r] += demands[next_i_city]
            else:
                continue  # Current robot can't take more cities, proceed to next robot

    # Close the loop back to the depot
    for tour in robot_tours:
        if tour:
            tour.insert(0, 0)  # start from depot
            tour.append(0)  # return to depot

    return robot_tours

def total_travel_cost(tours):
    total_cost = 0
    detailed_costs = []

    for tour in tours:
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += distance_matrix[tour[i]][tour[i+1]]
        detailed_costs.append(tour_cost)
        total_cost += tour_cost
        
    return total_cost, detailed_costs

# Assign cities to robots and calculate costs
tours = assign_cities_to_robots()
overall_cost, individual_costs = total_travel_cost(tours)

# Outputting the results as specified
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {individual_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")