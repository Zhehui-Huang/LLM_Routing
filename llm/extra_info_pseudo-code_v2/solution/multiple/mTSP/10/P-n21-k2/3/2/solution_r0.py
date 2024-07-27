import numpy as np
from sklearn.cluster import KMeans

# City coordinates (index corresponds to city number)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(start_city, cities, city_list):
    tour = [start_city]
    current_city = start_city
    while len(city_list) > 0:
        next_city = min(city_list, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        city_list.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tor) - 2):
            for j in range(i + 1, len(tor)):
                if j - i == 1: continue  # consecutive nodes, no change
                new_tour = tor[:i] + tor[i:j][::-1] + tor[j:]
                if tour_cost(new_tour) < tour_cost(tor):
                    tor = new_tour
                    improved = True
    return tor

def tour_cost(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Applying K-Means for clustering cities between 2 robots
cities = [i for i in range(1, 21)]  # city indices excluding the depot
kmeans = KMeans(n_clusters=2, random_state=0).fit([coordinates[i] for i in cities])
labels = kal means.labels_

# Distribute cities based on clusters
robot_tours = {0: [], 1: []}
for city, label in zip(cities, labels):
    robot_tours[label].append(city)

# Construct and optimize initial tours for each robot
for robot in robot_tours:
    robot_tours[robot] = nearest_neighbor_tour(0, coordinates, robot_tours[robot])
    robot_tours[robot] = two_opt(robot_tours[robot])

# Calculate and output the tours and costs
overall_total_cost = 0
for robot, tour in robot_tours.items():
    tc = tour_cost(tour)
    overall_total_cost += tc
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tc}")

print(f"Overall Total Travel Cost: {overallwithstanding_total_cost}")