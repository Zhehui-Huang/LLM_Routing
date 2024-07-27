import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69), 
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}
demands = {
    1: 19, 2: 30, 3: 16, 4: 23, 5: 11, 6: 31, 7: 15, 8: 28, 9: 14, 
    10: 8, 11: 7, 12: 14, 13: 19, 14: 11, 15: 26, 16: 17, 17: 6, 18: 15
}
num_robots = 2
capacity = 160

# Greedy assignment of cities to robots based on demands and simple clustering
assignment = {0: [], 1: []}
current_capacity = {0: 0, 1: 0}

sorted_cities = sorted(demands.items(), key=lambda x: -x[1])

for city, demand in sorted_cities:
    if current_capacity[0] + demand <= capacity:
        assignment[0].append(city)
        current_capacity[0] += demand
    elif current_capacity[1] + demand <= capacity:
        assignment[1].append(city)
        current_capacity[1] += demand

def compute_tour(cities_list):
    tour = [0]
    unvisited = set(cities_list)
    current_city = 0
    tour_cost = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        tour_cost += euclidean_distance(cities[current_city], cities[next_city])
        current_city = next_city
        tour.append(current_city)
        unvisited.remove(current_city)
    tour_cost += euclidean_distance(cities[current_city], cities[0])  # return to depot
    tour.append(0)
    return tour, tour_cost

tours = {}
total_cost = 0

for robot in range(num_robots):
    tours[robot], cost = compute_tour(assignment[robot])
    total_cost += cost
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Screen: {cost}")

print(f"Overall Total Travel Screen: {total_cost}")