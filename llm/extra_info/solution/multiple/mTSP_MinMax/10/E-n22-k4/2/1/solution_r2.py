import math
from sklearn.cluster import KMeans

# Define the cities and their coordinates
cities = [
    (145, 215), # Depot
    (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232),
    (128, 231), (156, 217), (129, 214), (146, 208), (164, 208),
    (141, 208), (147, 193), (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Calculating Euclidean distance between two cities given their indices
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Sklearn KMeans to cluster the cities to reduce travel distance for each robot
kmeans = KMeans(n_clusters=num_robots, random_state=42)
assignments = kmeans.fit_predict([city for city in cities[1:]])

# Grouping cities based on their assignments
robot_routes = {i: [] for i in range(num_robots)}
for index, label in enumerate(assignments):
    robot_routes[label].append(index + 1)  # +1 because cities indices in assignments are zero-based and excludes the depot

# Helper function to find the nearest city
def nearest_city(current_city, cities_left):
    return min(cities_left, key=lambda city: distance(cities[current_city], cities[city]))

# Compute TSP route for assigned cities using a greedy nearest neighbor approach
def compute_route(cities_list):
    if not cities_list:
        return [0, 0]  # Start and end at depot if no cities assigned
    route = [0]  # start at depot
    while cities_list:
        next_city = nearest_city(route[-1], cities_list)
        route.append(next_city)
        cities_list.remove(next_city)
    route.append(0)  # return to depot
    return route

# Construct routes for each robot and calculate distances
max_cost = 0
for robot_id, cities_list in robot_routes.items():
    route = compute_route(cities_list.copy())  # Use a copy to preserve original
    tour_cost = sum(distance(cities[route[i]], cities[route[i+1]]) for i in range(len(route)-1))
    max_cost = max(max_cost, tour_cost)
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")

print(f"Maximum Travel Cost: {max_cost:.2f}")