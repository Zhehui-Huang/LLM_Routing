import numpy as np

# Coordinates of the cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots and depots
num_robots = 8
depots = list(range(num_robots))  # Assume depots are the first 8 cities (0 to 7)

# Distance function
def distance(i, j):
    return np.linalg.norm(np.array(cities[i]) - np.array(cities[j]))

# Initialize parameters
num_cities = len(cities)
pheromones = np.ones((num_cities, num_cities)) * 0.1
visibility = 1 / (1 + np.array([[distance(i, j) for j in range(num_cities)] for i in range(num_cities)]))
alpha = 1.0
beta = 5.0
pheromone_evaporation = 0.1
pheromone_deposit = 1.0

# Perform iterations to find the best tours
best_tours = {i: [] for i in range(num_robots)}
best_costs = {i: np.inf for i in range(num_robots)}
overall_best_cost = np.inf

for _ in range(100):  # simulation iterations
    tours = {i: [i] for i in depots}
    remaining_cities = set(range(num_cities)) - set(depots)

    while remaining_cities:
        for robot in range(num_robots):
            if not remaining_cities:
                break
            current_city = tours[robot][-1]
            probabilities = []
            for city in range(num_cities):
                if city in remaining_cities or (len(tours[robot]) > 1 and city == robot):
                    probabilities.append((pheromones[current_city][city]**alpha) * (visibility[current_city][city]**beta))
                else:
                    probabilities.append(0)
            next_city = np.random.choice(range(num_cities), p=np.array(probabilities)/sum(probabilities))
            tours[robot].append(next_city)
            if next_city in remaining_cities:
                remaining_cities.remove(next_city)

    # Close the tours by returning to the respective depots
    for robot in range(num_robots):
        tours[robot].append(robot)
        travel_cost = sum(distance(tours[robot][i], tours[robot][i + 1]) for i in range(len(tours[robot]) - 1))
        if travel_cost < best_costs[robot]:
            best_costs[robot] = travel_cost
            best_tours[robot] = tours[robot]

    # Update pheromones
    pheromones *= (1-pheromone_evaporation)
    for robot in range(num_robots):
        for i in range(len(tours[robot]) - 1):
            pheromones[tours[robot][i]][tours[robot][i+1]] += pheromone_deposit

# Calculate overall best cost
total_cost = sum(best_costs.values())

# Output the solution
for robot in range(num_robots):
    print(f"Robot {robot} Tour: {best_tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {best_costs[robot]}")

print(f"Overall Total Travel Cost: {total_cost}")