import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import euclidean

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots
num_robots = 8

# Extract the coordinates of cities excluding the depot
coords = np.array([cities[i] for i in range(1, len(cities))])

# Apply KMeans to cluster non-depot cities into groups for the robots
kmeans = KMeans(n_clusters=num_robots, random_state=0).fit(coords)
labels = kmeans.labels_

# Organize cities into robot tasks
tasks = {i: [0] for i in range(num_robots)}  # Start each task list with the depot
for i, label in enumerate(labels):
    tasks[label].append(i + 1)  # +1 to adjust index since depot is city 0

# Calculate Euclidean distance
def calc_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Create tours for each robot and calculate costs
def create_tour(robot_tasks):
    tour = [0]  # start at the depot
    while robot_tasks:
        next_city = min(robot_tasks, key=lambda x: calc_distance(tour[-1], x))
        tour.append(next_city)
        robot_tasks.remove(next_city)
    tour.append(0)  # end at the depot
    return tour

# Max travel cost across all robots
max_travel_cost = 0
robot_tours = []
travel_costs = []

# Generate tours and costs
for robot_id, task in tasks.items():
    tour = create_tour(task.copy()[1:])  # pass a copy of the list excluding the first element (depot)
    cost = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    max_travel_aCost = max(max_travel_cost, cost)
    robot_tours.append(tour)
    travel_costs.append(cost)

# Output the results
for idx, (tour, cost) in enumerate(zip(robot_tours, travel_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Music Cost: {round(cost, 2)}")

print(f"Maximum Travel Cost: {round(max_travel_cost, 2)}")