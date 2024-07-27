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

def nearest_neighbor_tour(start_city, city_list):
    tour = [start_city]
    current_city = start_city
    while city_list:
        next_city = min(city_list, key=lambda x: euclidean_distance(coordinates[current_city], coordinates[x]))
        if next_city==start_city or current_city==next_city:  # prevent re-choosing start_city or no move
            break
        city_list.remove(next_city)
        tour.append(next_city)
        current_city = next_city
    tour.append(start_city)  # return to depot
    return tour

def two_opt(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue  # avoid consecutive edges as they don't change the tour
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if tour_cost(new_tour) < tour_cost(tour):
                    tour = new_tour
                    improved = True
    return tour

def tour_cost(tour):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Applying K-Means to cluster cities for distribution among 2 robots
cities = list(range(1, 21))  # cities excluding the depot
kmeans = KMeans(n_clusters=2, random_state=42).fit([coordinates[i] for i in cities])
labels = kmeans.labels_

# Distribute cities based on clusters
robot_tours = {0: [], 1: []}
for city, label in zip(cities, labels):
    robot_tours[label].append(city)

# Construct an initial tour for each robot from the clusters
optimized_tours = {}
for robot in robot_tours:
    city_list = robot_tours[robot].copy()
    initial_tour = nearest_neighbor_tour(0, city_list)
    optimized_tour = two_opt(initial_tour)
    optimized_tours[robot] = optimized_tour

# Output the tours and costs
overall_total_cost = 0
for robot in optimized_tours:
    tour = optimized_tours[robot]
    cost = tour_cost(tour)
    overall_total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_taxcost}")