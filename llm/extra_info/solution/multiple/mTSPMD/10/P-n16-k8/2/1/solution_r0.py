import math

# Coordinates of depot cities and other cities
coordinates = {
    0: (30, 40),   1: (37, 52),   2: (49, 49),   3: (52, 64),
    4: (31, 62),   5: (52, 33),   6: (42, 41),   7: (52, 41),
    8: (57, 58),   9: (62, 42),   10: (42, 57),  11: (27, 68),
    12: (43, 67),  13: (58, 48),  14: (58, 27),  15: (37, 69)
}

# Number of robots and their assigned depots
num_robots = 8
robots = {key: key for key in range(num_robots)}

# Function to compute Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Nearest neighbour algorithm
def nearest_neighbour_tour(start_city, available_cities):
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while available_cities:
        next_city = min(available_cities, key=lambda city: euclidean_distance(current_city, city))
        total_cost += euclidean_distance(current_city, next_city)
        current_city = next_city
        tour.append(current_city)
        available_cities.remove(current_city)
    
    # Return to start depot
    total_cost += euclidean_distance(current_city, start_city)
    tour.append(start_city)
    return tour, total_cost

# Assigning cities to robots excluding depots
all_cities = set(range(len(coordinates)))
depots = set(range(num_robots))
non_depot_cities = list(all_cities - depots)

assigned_cities = non_depot_cities.copy()

# Compute total tour for each robot
overall_total_cost = 0
for robot in robots:
    if assigned_cities:
        tour, cost = nearest_neighbour_tour(robots[robot], assigned_cities)
        overall_total_cost += cost
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {cost}")
    else:
        # If no cities left, just return to depot
        print(f"Robot {robot} Tour: [{robots[robot]}, {robots[robot]}]")
        print(f"Robot {robot} Total Travel Cost: 0")

print(f"Overall Total Travel Cost: {overall_total_cost}")