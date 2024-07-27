import math
from itertools import permutations

# City coordinates and demands
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}
demands = {
    1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
    10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26,
    18: 17, 19: 6, 20: 15
}

# Robots
num_robots = 2
robot_capacity = 160

# Calculate distance using Euclidean formula
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Heuristic function
def tabu_search_with_alns(robots, capacity, demands):
    tours = [[] for _ in range(robots)]
    loads = [0] * robots
    remaining = set(demands.keys())
    depot = 0

    while remaining:
        for i in range(robots):
            if not tours[i]:
                tours[i].append(depot)
            current_city = tours[i][-1]
            possible_moves = [city for city in remaining if loads[i] + demands[city] <= capacity]
            if not possible_moves:
                continue
            next_city = min(possible_moves, key=lambda x: euclidean_distance(current_city, x))
            tours[i].append(next_city)
            loads[i] += demands[next_city]
            remaining.remove(next_city)

            if loads[i] == capacity or not remaining:
                tours[i].append(depot)
                if loads[i] < capacity and remaining:
                    tours[i].remove(depot)

    for tour in tours:
        if tour[-1] != depot:
            tour.append(depot)
            
    return tours

# Implement tours using the heuristic
tours = tabu_search_with_alns(num_robots, robot_capacity, demands)

# Calculate tour costs
tour_costs = []
for tour in tours:
    cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    tour_costs.append(cost)

# Output Results
total_cost = sum(tour_costs)
for idx, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")