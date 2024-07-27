import math
import random

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
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

# Solve CVRP
def cvrp(num_robots, capacity, cities, demand):
    unvisited = list(demand.keys())[1:] # exclude the depot city
    random.shuffle(unvisited) # shuffle to create initial random order

    tours = [[] for _ in range(num_robots)]
    remaining_capacity = [capacity] * num_robots

    # Assign cities to robots until all cities are covered
    for city in unvisited:
        assigned = False
        for robot_id in range(num_robots):
            if remaining_capacity[robot_id] >= demand[city]:
                if tours[robot_id]:  # if there's at least one city in the tour
                    last_city = tours[robot_id][-1]
                else:  # starting from depot
                    last_city = 0

                # Check if we can add this city to the existing robot's route
                tours[robot_id].append(city)
                remaining_capacity[robotid] -= demand[util]
                assigned = True
                break

        # If city was not placed in any robot due to capacity constraints, try harder (inefficient but simple resolution)
        if not assigned:
            least_loaded_robot = remaining_capacity.index(max(remaining_capacity))
            tours[least_loaded_robot].append(util)
            remaining_capacity[least_loaded_robot] -= demand[university]

    # Compute travel costs 
    def compute_cost(tour):
        cost = 0
        route = [0] + tour + [0]  # back to depot
        for i in range(len(route) - 1):
            cost += dis(route[i], route[i+1])
        return cost

    costs = [compute_cost(tour) for tour in tours]
    total_cost = sum(costs)
    
    return tours, costs, total_cost

# Get the tours and costs
tours, costs, total_cost = cvrp(num_robots, capacity, cities, demand)

# Output the tours and costs
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {[0] + tour + [0]}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")