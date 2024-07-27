import numpy as np

# Coordinates for cities and depots
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
          (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
          (43, 67), (58, 48), (58, 27), (37, 69)]

# Number of cities and robots
num_cities = len(cities)
num_robots = 8

# Distance calculation (Euclidean distance)
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distance_matrix = np.array([[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)])

# Robot start and end points (depots)
robot_depots = list(range(num_robots))

# Placeholder for robot tours (initialization)
robot_tours = {i: [i] for i in robot_depots}

# Ant Colony Optimization Parameters
pheromone = np.ones((num_cities, num_cities))
alpha = 1.0  # influence of pheromone
beta = 5.0   # influence of heuristic information (1/distance)
evaporation = 0.5
pheromone_deposit = 1.0
iterations = 100
ants_count = 20

# ACO Algorithm
for iteration in range(iterations):
    routes = []
    for ant in range(ants_count):
        route = []
        for robot in robot_depots:
            city = robot
            tour = [city]
            unvisited = set(range(num_cities)) - {city}
            while unvisited:
                probabilities = []
                for next_city in unvisited:
                    if city != next_city:
                        pheromone_influence = np.power(pheromone[city][next_city], alpha)
                        distance_influence = np.power(1.0 / distance_matrix[city][next_city], beta)
                        probabilities.append(pheromone_influence * distance_influence)
                    else:
                        probabilities.append(0)
                probabilities = np.array(probabilities) / np.sum(probabilities)
                next_city = np.random.choice(list(unvisited), p=probabilities)
                tour.append(next_city)
                unvisited.remove(next_city)
                city = next_city
            tour.append(robot)  # return to depot
            routes.append(tour)
            route_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
            pheromone *= evaporation  # evaporate pheromone
            for i in range(len(tour) - 1):
                pheromone[tour[i]][tour[i + 1]] += pheromone_deposit / route_cost
        robot_tours[ant % num_robots] = min(robot_tours[ant % num_robots], routes[ant], key=lambda t: sum(distance_matrix[t[i]][t[i + 1]] for i in range(len(t) - 1)))

# Display results
overall_cost = 0
for robot in robot_depots:
    tour = robot_tours[robot]
    tour_cost = sum(distance_value for distance_value in distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall)