import math
import random

# Function to calculate Euclidean distance between two points
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Convert city keys to a list, excluding the depot
city_list = list(cities.keys())[1:]

# Randomly partition the cities into approximately equal parts for each robot
random.shuffle(city_list)
city_parts = [city_list[i::num_robots] for i in range(num_robots)]

# Generate tours for each robot and calculate the travel costs
tours = []
costs = []

for i in range(num_robots):
    tour = [0] + city_parts[i] + [0]
    tour_cost = 0
    for j in range(len(tour) - 1):
        tour_cost += distance(cities[tour[j]], cities[tour[j+1]])
    tours.append(tour)
    costs.append(tour_cost)

# Determine the maximum travel cost
max_travel_cost = max(costs)

# Print the results
for i, tour in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {costs[i]:.2f}")

print(f"Maximum Travel Cost: {max_travel_cost:.2f}")