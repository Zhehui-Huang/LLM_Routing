import math

# Distance calculation as per Euclidean formula
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculating the tour total distance based on the indices in the tour array
def tour_distance(tour, cities):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

# 2-opt swap optimizer function
def two_opt(route, cities):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:  # Skip adjacent edges
                    continue
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if tour_distance(new_route, cities) < tour_distance(route, cities):
                    route = new_route
                    improvement = True
    return route

# Assignment of cities to nearest robot
def nearest_robot_assignment(cities, num_robots):
    unvisited = list(range(1, len(cities)))
    tours = [[0] for _ in range(num_robots)]
    
    while unvisited:
        for t in tours:
            if not unvisited:
                break
            nearest_city = min(unvisited, key=lambda x: calculate_distance(cities[t[-1]], cities[x]))
            t.append(nearest_city)
            unvisited.remove(nearest_city)
    
    # Close all tours back to the depot
    for t in tours:
        t.append(0)
    
    # Optimize each tour using 2-opt
    for i in range(num_robots):
        tours[i] = two_opt(tours[i], cities)
    
    return tours

# City coordinates
cities = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
          (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)]

# Given number of robots
num_robots = 2

# Generate initial assignments and improve them
tours = nearest_robot_assignment(cities, num_robots)
overall_cost = 0

# Output format
for idx, tour in enumerate(tours):
    cost = tour_distance(tour, cities)
    overall_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall","overall_cost,"sum of all tours' costs.")