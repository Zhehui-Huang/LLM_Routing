import math
import random


# Define city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Initialize tours using a simple greedy approach
def initialize_tours(num_robots=2):
    unvisited = set(cities.keys()) - {0}
    tours = [[0] for _ in range(num_robots)]
    available_cities = set(unvisited)

    for i in range(num_robots):
        current_city = 0
        while available_cities:
            next_city = min(available_cities, key=lambda x: distance(current_city, x))
            tours[i].append(next_city)
            available_cities.remove(next_city)
            current_city = next_city
            if len(available_cities) < num_robots - i - 1:
                break

    return tours

# Simulate tabu search (Iteratively improve the tours)
def tabu_search(tours, iterations=10):
    current_cost = calculate_tour_cost(tours)
    best_tours = tours
    best_cost = current_cost

    for _ in range(iterations):
        new_tours = [tour[:] for tour in tours]
        # Attempt a simple 2-opt move
        for i in range(len(new_tours)):
            if len(new_tours[i]) > 3:
                # Swap two cities in a tour
                a, b = random.sample(range(1, len(new_tours[i])-1), 2)
                new_tours[i][a], new_tours[i][b] = new_tours[i][b], new_tours[i][a]
        new_cost = calculate_tour_cost(new_tours)
        if sum(new_cost) < sum(best_cost):
            best_tours, best_cost = new_tours, new_cost

    return best_tours

# Calculate the cost of a tour
def calculate_tour_cost(tours):
    costs = []
    for tour in tours:
        tour_cost = 0
        for i in range(1, len(tour)):
            tour_cost += distance(tour[i - 1], tour[i])
        costs.append(tour_cost)
    return costs


## Main Execution
tours = initialize_tours(2)
tours = tabu_search(tours, 100)
costs = calculate_tour_cost(tours)
total_cost = sum(costs)

# Output formatted results
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")