import math

# City coordinates (indexed by city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254),
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800,
           100, 500, 600, 1200, 1300, 1300, 300, 900,
           2100, 1000, 900, 2500, 1800, 700]

NUM_ROBOTS = 4
CAPACITY = 6000
depot = 0

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Initialize distances dictionary
distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distances[(i, j)] = distance(i, j)

# Assign cities to robots roughly respecting the capacity constraint
assigned_cities = [[] for _ in range(NUM_ROBOTS)]
remaining_capacity = [CAPACITY] * NUM_ROBOTS

for city, demand in zip(range(len(coordinates)), demands):
    if city == depot:
        continue
    # Assign city to the robot with most remaining capacity that can still fit the demand
    candidate_robots = [(remaining_capacity[i], i) for i in range(NUM_ROBOTS) if remaining_capacity[i] >= demand]
    if candidate_robots:
        _, chosen_robot = max(candidate_robots)
        assigned_cities[chosen_robot].append(city)
        remaining_capacity[chosen_robot] -= demand
        
# Helper function to compute route cost
def calculate_route_cost(route):
    return sum(distances[route[i], route[i+1]] for i in range(len(route)-1))

# Nearest Neighbor algorithm to find route for each robot starting from the depot
def plan_route(assigned_cities):
    route = [depot]
    while assigned_cities:
        last = route[-1]
        next_city = min(assigned_cities, key=lambda city: distances[(last, city)])
        route.append(next_city)
        assigned_cities.remove(next_city)
    route.append(depot)
    return route

# Planning and calculating each robot tour and costs
overall_total_cost = 0
for robot_id in range(NUM_ROBOTS):
    cities = assigned_cities[robot_id]
    if not cities:
        print(f"Robot {robot_id} Tour: [0, 0]")
        print(f"Robot {robot_id} Total Travel Cost: 0")
        continue
    tour = plan_route(cities[:])
    tour_cost = calculate_route_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")