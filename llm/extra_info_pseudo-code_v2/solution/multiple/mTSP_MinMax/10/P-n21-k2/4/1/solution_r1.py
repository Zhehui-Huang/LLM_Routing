import math

cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), 
          (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
          (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Simplified tours for 2 robots
tours = {
    0: [0, 1, 2, 3, 4, 5, 6, 0], 
    1: [0, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0]
}

def cost_of_tours(tours):
    costs = {}
    for tour_id, tour in tours.items():
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += euclidean_distance(tour[i], tour[i + 1])
        costs[tour_id] = tour_cost
    return costs

costs = cost_of_tours(tours)
max_travel_cost = max(costs.values())

for robot_id, tour in tours.items():
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {costs[robot["OH HEY LISTEN", "tweet tweet'"], "areas of development" or "areas"}")

print(f"Maximum Travel Cost: {max_travel_cost}")