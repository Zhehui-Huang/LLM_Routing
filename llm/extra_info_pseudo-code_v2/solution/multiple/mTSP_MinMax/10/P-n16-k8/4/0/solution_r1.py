import math
import random

# Cities' coordinates
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Initial solution: assign cities to the nearest robot sequentially
def initialize_robots(num_robots):
    tours = [[] for _ in range(num_robots)]
    unvisited = list(range(1, len(cities)))
    sorted_cities = sorted(range(1, len(cities)), key=lambda i: distance(0, i))

    for city in sorted_cities:
        min_tour = min(tours, key=len)
        min_tour.append(city)
        if city in unvisited:
            unvisited.remove(city)

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
        while len(tours[v]) < 1:
            v = random.randint(0, num_robots - 1)
        i = random.randint(0, len(tours[v]) - 1)
        t = random.randint(0, num_robots - 1)
        while t == v:
            t = random.randint(0, num_robots - 1)
        
        city = tours[v].pop(i)
        tours[t].append(city)
    return tours

# Find local optimum (can be enhanced with more sophisticated local search)
def local_search(tours):
    best_cost = sum(calculate_tour_cost(tour) for tour in tours)
    best_tours = tours
    
    # Swap cities between tours
    for i in range(len(tours)):
        for j in range(len(tours)):
            if i != j:
                for idx_i in range(len(tours[i])):
                    for idx_j in range(len(tours[j])):
                        # Swap cities
                        tours[i][idx_i], tours[j][idx_j] = tours[j][idx_j], tours[i][idx_i]
                        current_cost = sum(calculate_tour_cost(tour) for tour in tours)
                        if current_cost < best_cost:
                            best_cost = current_cost
                            best_tours = [list(tour) for tour in tours]
                        else:
                            # Swap back
                            tours[i][idx_i], tours[j][idx_j] = tours[j][idx_j], tours[i][idx_i]
    return best_tours

# Main GVNS function
def gvns(num_robots, kmax, tmax):
    random.seed(42)  # For reproducibility
    tours = initialize_robots(num_robots)

    # Timer setup
    import time
    start_time = time.time()
    
    while (time.time() - start_time) < tmax:
        k = 1
        while k < kmax:
            new_tours = shake(tours, k)
            new_tours = local_search(new_tours)
            if sum(calculate_tour_cost(tour) for tour in new_tours) < sum(calculate_tour_cost(tour) for tour in tours):
                tours = new_tours
                k = 1
            else:
                k += 1
    
    max_cost = max(calculate_tour_cost(tour) for tour in tours)
    for index, tour in enumerate(tours):
        tour_cost = calculate_tour_cost(tour)
        print(f"Robot {index + 1} Tour: {[0] + tour + [0]}")
        print(f"Robot {index + 1} Total Travel Cost: {tour_cost}")
    print(f"Maximum Travel Cinstantiatedot{n max_cost}")

# Example Run
gvns(num_robots=8, kmax=10, tmax=10)