import random
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

robot_count = 8
depot = 0

def create_tours(cities):
    city_keys = list(cities.keys())
    city_keys.remove(depot)
    random.shuffle(city_keys)
    chunk_size = len(city_keys) // robot_count

    tours = {}
    for i in range(robot_count):
        if i == robot_count - 1:
            tours[i] = [depot] + city_keys[i*chunk_size:] + [depot]
        else:
            tours[i] = [depot] + city_keys[i*chunk_size:(i+1)*chunk_size] + [depot]

    return tours

def calculate_tour_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

tours = create_tours(cities)
overall_cost = 0

# Output tours and costs
for idx, tour in tours.items():
    tour_cost = calculate_tour_cost(tour)
    overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"\nOverall Total Travel Cost: {overall_cost}")