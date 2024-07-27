import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41),
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

def euclidean_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of robots
num_robots = 8
start_depot = 0  # All robots start from city 0

# Distribute cities among robots evenly, naive distribution
total_cities = len(cities)
cities_per_robot = (total_cities - 1) // num_robots
extra_cities = (total_cities - 1) % num_robots

tours = []
total_travel_cost = 0

# Create tours for each robot
for i in range(num_robots):
    if i < extra_cities:
        robot_cities = list(range(1+i*(cities_per_robot+1), 1+(i+1)*(cities_per_robot+1)))
    else:
        start_index = extra_cities * (cities_per_robot + 1) + (i - extra_cities) * cities_per_robot
        robot_cities = list(range(1+start_index, 1+start_index + cities_per_robot))
    if robot_cities:
        # Adding start depot city
        tour = [start_depot] + robot_cities
        # Calculate tour cost
        tour_cost = sum(euclidean_distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
        tours.append((tour, tour_cost))
        total_travel_cost += tour_cost

# Output tours and costs
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_operational_cost:.2f}")