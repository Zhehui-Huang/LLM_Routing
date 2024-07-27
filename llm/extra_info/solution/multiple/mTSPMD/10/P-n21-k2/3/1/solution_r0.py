import math

# Given cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41),  8: (57, 58),  9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67),
    13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63),
    19: (63, 69), 20: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0]) ** 2 + (cities[city_a][1] - cities[city_b][1]) ** 2)

# Initialize tours for each robot
tours = {0: [0], 1: [1]}
remaining_cities = set(cities.keys()) - {0, 1}

# Assign remaining cities to nearest robot depot
while remaining_cities:
    for robot in tours.keys():
        if not remaining_cities:
            break
        nearest_city = min(remaining_cities, key=lambda city: distance(city, tours[robot][0]))
        tours[robot].append(nearest_city)
        remaining_cities.remove(nearest_city)

# Ensure robots return to their respective depots
for robot in tours:
    tours[robot].append(tours[robot][0])

# Function to calculate total travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output results
total_cost = 0
for robot in tours:
    robot_cost = calculate_tour_cost(tours[robo])
    total_cost += robot_cost
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_cost}")