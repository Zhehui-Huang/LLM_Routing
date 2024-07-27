import math
import random

# City coordinates (index is city number)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    dx = cities[c1][0] - cities[c2][0]
    dy = cities[c1][1] - cities[c2][1]
    return math.sqrt(dx**2 + dy**2)

# Generate initial solution based on nearest unvisited city, equally distributing cities to 8 robots
def initial_solution(cities, num_robots=8):
    tours = {i: [] for i in range(num_robots)}
    unvisited = list(cities.keys())[1:]  # Exclude depot city 0 from the unvisited list
    depot = 0
    robot = 0

    while unvisited:
        if robot not in tours:
            tours[robot] = [depot]
        if tours[robot]:
            last_city = tours[robot][-1]
        else:
            last_city = depot

        # Find nearest unvisited city
        nearest_city = min(unvisited, key=lambda x: distance(last_city, x))
        tours[robot].append(nearest_city)
        unvisited.remove(nearest_city)

        # Move to the next robot
        robot = (robot + 1) % num_robots

    # Ensuring all robots start and end at the depot city 0
    for r in tours:
        if tours[r]:
            tours[r].insert(0, depot)
        else:
            tours[r] = [depot, depot]
    return tours

# Calculating tour cost
def tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Simulated Annealing main procedure
def simulated_annealing(tours, iterations=1000, temperature=1000, alpha=0.995):
    for i in range(iterations):
        # Pick a random robot and two cities to swap (excluding the start city)
        robot = random.choice(list(tours.keys()))
        if len(tours[robot]) <= 3:
            continue
        c1, c2 = random.sample(range(1, len(tours[robot])-1), 2)
        new_tour = tours[robot][:]
        new_tour[c1], new_tour[c2] = new_tour[c2], new_tour[c1]
        
        if tour_cost(new_tour) < tour_cost(tours[robot]):
            tours[robot] = new_tour
        else:
            if math.exp(-(tour_cost(new_tour) - tour_cost(tours[robot])) / temperature) > random.random():
                tours[robot] = new_tour
        temperature *= alpha

    return tours

# Main Execution
num_robots = 8
initial_tours = initial_solution(cities, num_robots)
optimized_tours = simulated_annealing(initial_tours)

# Calculate total cost and individual tour costs
total_cost = 0
for robot, tour in optimized_tours.items():
    cost = tour_cost(tour)
    total_cost += cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")