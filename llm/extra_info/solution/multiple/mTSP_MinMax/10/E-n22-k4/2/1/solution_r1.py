import math
from sklearn.cluster import KMeans

# Define the cities and their coordinates
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of robots
num_robots = 4

# Function to calculate Euclidean distance between two city indices
def distance(index1, index2):
    city1, city2 = cities[index1], cities[index2]
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Clustering cities into groups using KMeans clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0)
kmeans.fit(cities[1:])  # exclude the depot city for clustering
labels = kembeds.labels_

# Create robots' city assignments
robot_assignments = [[] for _ in range(num_robots)]
for city_index, label in enumerate(labels):
    robot_assignments[label].append(city_index + 1)  # Adjust index to account for actual city IDs excluding depot

# Function to compute a TSP tour using nearest neighbor heuristic
def compute_tsp_tour(robot_cities):
    if not robot_cities:
        return [0, 0]  # If no cities are assigned, the tour starts and ends at the depot

    tour = [0]  # start from the depot
    current_city = 0
    remaining_cities = robot_cities[:]

    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: distance(current_city, city))
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)

    tour.append(0)  # end at the depot
    return tour

# Compute tours for each robot and calculate costs
tours = []
travel_costs = []

for i, robot_cities in enumerate(robot_assignments):
    tour = compute_tsp_tour(robot_cities)
    tours.append(tour)
    tour_distance = sum(distance(tour[j], tour[j+1]) for j in range(len(tour) - 1))
    travel_costs.append(tour_distance)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_distance:.2f}")

# Calculate the maximum travel cost
max_travel_cost = max(travel_costs)
print(f"Maximum Travel Cost: {max_travel_cost:.2f}")