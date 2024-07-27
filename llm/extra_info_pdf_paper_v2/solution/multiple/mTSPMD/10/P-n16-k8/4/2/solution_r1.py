import math
import random

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]
robot_depot = {i: i for i in range(8)}  # Each robot starts at consecutive depots from 0 to 7

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour):
    total_dist = 0
    for i in range(1, len(tour)):
        total_dist += euclidean_distance(coordinates[tour[i - 1]], coordinates[tour[i]])
    return total_dist

def initialize_pheromone(n, initial_value=1.0):
    return [[initial_value] * n for _ in range(n)]

def visibility(c1, c2):
    if c1 == c2:
        return 0
    return 1 / euclidean_distance(coordinates[c1], coordinates[c2])

def choose_next_city(current_city, pheromone, visibility, taboo_list, alpha=1.0, beta=5.0):
    probs = []
    for i in range(len(pheromone)):
        if i not in taboo_list:
            probs.append(pheromone[current_city][i] ** alpha * visibility(current_city, i) ** beta)
        else:
            probs.append(0)
    total = sum(probs)
    probs = [p / total if total > 0 else 0 for p in probs]
    next_city = random.choices(range(len(pheromone)), weights=probs, k=1)[0]
    return next_city

def update_pheromone(pheromone, tours, decay=0.1, contribution=1.0):
    for i, route in enumerate(tours):
        for j in range(len(route) - 1):
            pheromone[route[j]][route[j+1]] += contribution / calculate_total_distance(route)
    for i in range(len(pheromone)):
        for j in range(len(pheromone[i])):
            pheromone[i][j] *= (1 - decay)

def ant_colony_optimization(num_cities, num_robots, num_iterations=100):
    pheromone = initialize_pheromone(num_cities)
    best_tours = None
    best_total_cost = float('inf')

    for iteration in range(num_iterations):
        tours = {r: [robot_depot[r]] for r in range(num_robots)}
        for r in range(num_robots):
            current_city = tours[r][-1]
            while len(tours[r]) < (num_cities // num_robots) + 1:
                next_city = choose_next_city(current_city, pheromone, visibility, tours[r])
                tours[r].append(next_city)
                current_city = next_city
            tours[r].append(robot_depot[r]) # return to depot

        total_cost = sum(calculate_total_distance(tours[r]) for r in range(num_robots))

        if total_cost < best_total_cost:
            best_total_cost = total_cost
            best_tours = tours

        # Update pheromone based on all robots' tours
        update_pheromone(pheromone, [tour for tour in tours.values()])

    return best_tours, best_total_cost

# Run the optimization
best_tours, best_total_cost = ant_colony_optimization(len(coordinates), len(robot_depot))

# Print tours and costs
for robot, tour in best_tours.items():
    cost = calculate_total_distance(tour)
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost}")
print(f"Overall Total Travel Cost: {best_total_cost}")