import math

def calculate_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

def find_tour_for_robot(unvisited, start_city=0):
    tour = [start_city]
    current_city = start_city
    total_cost = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: calculate_distance(current_city, city))
        total_cost += calculate_distance(current_city, next_city)
        current_city = next_city
        tour.append(next_city)
        unvisited.remove(next_city)
    
    # Closing the loop back to the depot
    total_cost += calculate_distance(current City, start_city)
    tour.append(start_city)
    
    return tour, total_cost

# Assign initial unvisited cities list excluding the depot
unvisited_cities = list(range(1, len(coordinates)))

# Find tours for each robot
robot_0_tour, robot_0_cost = find_tour_for_robot(unvisited_cities[:len(unvisited_cities)//2])
robot_1_tour, robot_1_cost = find_tour_for_robot(unvisited_cities[len(unvisited_cities)//2:])

overall_total_cost = robot_0_cost + robot_1_cost

print(f"Robot 0 Tour: {robot_0_tour}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")

print(f"Robot 1 Tour: {robot_1_tour}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")