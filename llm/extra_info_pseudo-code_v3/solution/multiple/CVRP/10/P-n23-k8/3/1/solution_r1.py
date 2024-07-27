import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 49),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Demand list for the cities
demand = {
    0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28,
    9: 8, 10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26,
    18: 17, 19: 6, 20: 15, 21: 5, 22: 10
}

# Number of robots and their capacity
num_robots = 8
capacity = 40

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Assign cities to robots ensuring each robot does not exceed its capacity
def assign_cities_to_robots(cities, demand, num_robots, capacity):
    tours = [[] for _ in range(num_robots)]
    remaining_capacity = [capacity] * num_robots
    city_list = list(demand.keys())[1:]  # Exclude the depot

    for city in city_list:
        for robot_id in range(num_robots):
            if remaining_capacity[robot_id] >= demand[city]:
                # Assign city to this robot if it has enough capacity
                tours[robot_id].append(city)
                remaining_capacity[robot_id] -= demand[city]
                break

    # Add depot to start and end of each tour
    for tour in tours:
        tour.insert(0, 0)
        tour.append(0)

    return tours

def calculate_cost(tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return total_cost

# Assigning cities to robots
tours = assign_cities_to_robots(cities, demand, num_robots, capacity)

# Calculating costs
total_cost = 0
costs = []
for tour in tours:
    tour_cost = calculate_cost(tour)
    costs.append(tour_cost)
    total_cost += tour_cost

# Output results
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")