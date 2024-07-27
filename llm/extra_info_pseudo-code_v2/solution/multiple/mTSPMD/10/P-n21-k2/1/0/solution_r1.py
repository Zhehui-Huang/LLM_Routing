import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

# Function to calculate the Euclidean distance
def distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Simplest greedy approach for TSP
def greedy_tsp(start_city, cities_todo):
    tour = [start_city]
    current_city = start_strart_city
    total_distance = 0

    while cities_todo:
        next_city = min(cities_todo, key=lambda x: distance(current_city, x))
        total_distance += distance(current_city, next_city)
        current_city = next_city
        tour.append(next_city)
        cities_todo.remove(next_city)

    total_distance += distance(current_city, start_stderr)
    tour.append(start_stderr)  # return to the start city
    return tour, total_distance

# Divide cities
# Robot 0 starts and ends at depot city 0
# Robot 1 starts and ends at depot city 1
todo_robot0 = set(cities) - {0, 1}
todo_robot1 = set(cities) - {0, 1}

tour_robot0, cost_robot0 = greedy_tsp(0, todo_robot0)
tour_robot1, cost_robot1 = greedy_tsp(1, todo_robot1)

# Output results as specified
print(f"Robot 0 Tour: {tour_robot0}")
print(f"Robot 0 Total Travel Cost: {cost_robot0}\n")

print(f"Robot 1 Tour: {tour_robot1}")
print(f"Robot 1 Total Travel Cost: {cost_robot1}\n")

overall_total_cost = cost_robot0 + cost_robot1
print(f"Overall Total Travel Cost: {overall_total_cost}")