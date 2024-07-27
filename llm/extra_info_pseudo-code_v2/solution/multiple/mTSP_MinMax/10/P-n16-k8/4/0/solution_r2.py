import math
import random
import time

# Cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial solution: assign cities to robots in a balanced way
def initialize_robots(num_robots):
    tours = [[] for _ in range(num_robots)]
    sorted_cities = sorted(range(1, len(cities)), key=lambda i: distance(0, i))
    
    for idx, city in enumerate(sorted_cities):
        tours[idx % num_robots].append(city)
        
    return tours

# Calculate the tour cost
def calculate_tour_cost(tour):
    cost = distance(0, tour[0])  # depot to first city
    for i in range(1, len(tour)):
        cost += distance(tour[i - 1], tour[i])
    cost += distance(tour[-1], 0)  # last city back to depot
    return cost

# Run shaking process
def shake(tours, k):
    num_robots = len(tours)
    for _ in range(k):
        v = random.randint(0, num_robots - 1)
        if len(tours[v]) > 1:
            i = random.randint(0, len(tours[v]) - 1)
            t = random.randint(0, num_robots - 1)
            while t == v:
                t = random.randint(0, num_robots - 1)

            city = tours[v].pop(i)
            tours[t].append(city)
    return tours

# Find local optimum
def local_search(tours):
    for i in range(len(tours)):
        for j in range(i + 1, len(tours)):
            for c1 in range(len(tours[i])):
                for c2 in range(len(tours[j])):
                    tours[i][c1], tours[j][c2] = tours[j][c2], tours[i][c1]
                    if calculate_tour_cost(tours[i]) + calculate_tour_cost(tours[j]) < calculate_tour_cost(tours[i]) + calculate_tour_cost(tours[j]):
                        tours[i][c1], tours[j][c2] = tours[j][c2], tours[i][c1]  # Revert if no improvement
    return tours

# Main GVNS function
def gvns(num_robots, kmax, tmax):
    random.seed(42) # For reproducibility
    tours = initialize_robots(num_robots)
    start_time = time.time()

    while (time.time() - start_time) < tmax:
        k = 1
        while k < kmax:
            new_tours = shake(tours, k)
            new_tours = local_search(new_tours)
            new_total_cost = sum(calculate_tour_cost(tour) for tour in new_tours)
            current_total_cost = sum(calculate_tour_cost(tour) for tour in tours)
            if new_total_cost < current_total_cost:
                tours = new_tours
                k = 1  # reset k
            else:
                k += 1

    # Outputting results
    max_cost = 0
    for index, tour in enumerate(tours):
        tour_cost = calculate_tour_cost(tour)
        max_cost = max(max_cost, tour_cost)
        print(f"Robot {index} Tour: [0, " + ', '.join(map(str, tour)) + ", 0]")
        print(f"Robot {index} Total Travel Cost: {tour_cost}")
    print(f"Maximum Travel Cost: {max_cost}")

# Example run configuration
gvns(num_robots=8, kmax=10, tmax=60)  # Specify the allowed maximum time (seconds)