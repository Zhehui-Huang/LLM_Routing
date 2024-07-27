import math
import random

# Environment information
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8
depots = list(range(num_robots))  # depots are from 0 to 7

# Calculate euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Initialize robots tours starting from depot 0
tours = {robot_id: [0] for robot_id in range(num_robots)} 

# Step 1: Nearest Neighbor Search
# Allocate each city to the nearest depot not already having a second city (other than itself)
unvisited_cities = set(cities.keys()) - {0}
assigned_cities = []

for current_depot in depots:
    if len(tours[current_depot]) > 1:
        continue
    nearest = min(unvisited_cities, key=lambda city: distance(current_depot, city))
    tours[current_depot].append(nearest)
    unvisited_cities.remove(nearest)
    assigned_cities.append(nearest)

# Continue allocating cities to the nearest last-city in each tour
while unvisited_cities:
    for tour in tours.values():
        if not unvisited_cities:
            break
        last_city = tour[-1]
        nearest = min(unvisited_cities, key=lambda city: distance(last_city, city))
        tour.append(nearest)
        unvisited_cities.remove(nearest)
        assigned_cities.append(nearest)

# Divide load more evenly
random.shuffle(assigned_cities)
for robot_id, tour in tours.items():
    if len(tour) < (16 / num_robots):  # Roughly balance the tour lengths
        extra_city = assigned_cities.pop()
        tour.append(extra_city)

# Calculate total travel cost per tour and complete tour by returning to depot
total_costs = {}
total_overall_cost = 0

for robot_id, tour in tours.items():
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    # Add path back to the depot
    tour.append(0)
    total_cost += distance(tour[-2], tour[-1])
    total_costs[robot_id] = total_cost
    total_overall_cost += total_cost
    
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robotid} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {total_overall_cost}")