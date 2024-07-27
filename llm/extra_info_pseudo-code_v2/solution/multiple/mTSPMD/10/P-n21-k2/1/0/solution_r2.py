import math

# City coordinates keyed by their index
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Distance calculation using Euclidean formula
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Function implementing a simple Greedy TSP approach for a given start point
def greedy_tsp(start, not_visited):
    tour = [start]
    current = start
    total_cost = 0

    while not_visited:
        next_city = min(not_visited, key=lambda x: calc_distance(current, x))
        total_cost += calc_distance(current, next_city)
        current = next_city
        tour.append(next_city)
        not_visited.remove(next_city)
    
    total_cost += calc_distance(current, start)  # Returning to start
    tour.append(start)
    return tour, total_cost

# Preparing sets of cities for each robot
cities_robot_0 = set(cities.keys()) - {0, 1}
cities_robot_1 = set(cities.keys()) - {0, 1}

# Finding tours and costs for each robot
tour_0, cost_0 = greedy_tsp(0, cities_robot_0)
tour_1, cost_1 = greedy_tsp(1, cities_robot_1)

# Printing the results
print(f"Robot 0 Tour: {tour_0}")
print(f"Robot 0 Total Travel Cost: {cost_0}\n")

print(f"Robot 1 Tour: {tour_1}")
print(f"Robot 1 Total Travel Cost: {cost_1}\n")

overall_cost = cost_0 + cost_1
print(f"Overall Total Travel Cost: {overall_cost}")