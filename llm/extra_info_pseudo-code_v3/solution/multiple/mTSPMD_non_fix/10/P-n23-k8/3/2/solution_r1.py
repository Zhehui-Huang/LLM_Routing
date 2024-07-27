import math

# City coordinates with index as city ID
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

num_robots = 8
starting_depot = 0  # All robots start at city 0 initially

# Calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Simple greedy nearest neighbor tour construction
def nearest_neighbour_tours(starting_depot):
    unvisited_cities = set(range(1, len(city_coordinates)))  # Exclude the starting depot
    tours = {i: [starting_depot] for i in range(num_robots)}
    
    # Assign nearest unvisited city to each robot starting at depot
    for i in range(num_robots):
        min_dist, nearest_city = float('inf'), None
        for city in unvisited_cities:
            dist = calculate_distance(tours[i][-1], city)
            if dist < min_dist:
                nearest_city, min_dist = city, dist
        if nearest_city is not None:
            tours[i].append(nearest_city)
            unvisited_cities.remove(nearest_city)
    
    # Continue assigning the nearest unvisited city to the last city in each robot's tour
    while unvisited_cities:
        for i in range(num_robots):
            if not unvisited_cities:
                break
            min_dist, nearest_city = float('inf'), None
            for city in unvisited_cities:
                dist = calculate_distance(tours[i][-1], city)
                if dist < min_dist:
                    nearest_city, min_dist = city, dist
            if nearest_city is not None:
                tours[i].append(nearest_city)
                unvisited_cities.remove(nearest_city)
    
    return tours

# Calculate travel costs for the tours
def calculate_tour_costs(tours):
    costs = {}
    total_cost = 0
    for i in range(num_robots):
        tour = tours[i]
        tour_cost = 0
        for j in range(1, len(tour)):
            tour_cost += calculate_distance(tour[j - 1], tour[j])
        costs[i] = tour_cost
        total_cost += tour_cost
    return costs, total_cost

# Generate and display tours and costs
initial_tours = nearest_neighbour_tours(starting_depot)
tour_costs, total_travel_cost = calculate_tour_costs(initial_tours)

for i in range(num_robots):
    print(f"Robot {i} Tour: {initial_tours[i]}")
    print(f"Robot {i} Total Travel Cost: {tour_costs[i]}")

print(f"Overall Total Travel Cost: {total_travel_cost}")