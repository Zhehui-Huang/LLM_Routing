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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Clustering cities into groups using KMeans clustering
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(cities[1:])  # excluding the depot
labels = kmeans.labels_

# Assign cities to robots based on clustering result
robots = [[] for _ in range(num_robots)]
for idx, label in enumerate(labels, start=1):  # Start index with 1 to exclude depot
    robots[label].append(idx)

# Calculate TSP tour for each robot using nearest neighbor heuristic
def compute_tsp_tour(start_city, cities, city_coordinates):
    tour = [start_city]
    current_city = start_city
    remaining_cities = cities[:]
    
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distance(city_coordinates[current_city], city_coordinates[x]))
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    
    tour.append(start_city)  # return to the depot
    return tour

# Compute tours and travel costs for each robot
tours = []
travel_costs = []

for i, cities in enumerate(robots):
    tour = compute_tsp_tour(0, cities, cities)
    tours.append(tour)
    cost = sum(distance(cities[tour[j]], cities[tour[j+1]]) for j in range(len(tour)-1))
    travel_costs.append(cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

# Calculate the maximum travel cost 
max_travel_cost = max(travel_costs)
print(f"\nMaximum Travel Cost: {max_travel_cost:.2f}")