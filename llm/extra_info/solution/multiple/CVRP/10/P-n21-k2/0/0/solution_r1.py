import math

# Function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Data Initialization
cities = [
    (30, 40),
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]
capacity = 160
num_robots = 2

# Basic heuristic: nearest neighbor approach with demand checks
def nearest_neighbor_tsp(capacity, cities, demands):
    routes = []
    demands_met = [False] * len(cities)
    demands_met[0] = True  # Depot city
    for _ in range(num_robots):
        load = 0
        current_city_index = 0
        tour = [0]
        while True:
            nearest = None
            min_dist = float('inf')
            for i, city in enumerate(cities):
                if not demands_met[i] and (load + demands[i] <= capacity):
                    dist = distance(cities[current_city_index], city)
                    if dist < min_dist:
                        min_dist = dist
                        nearest = i
            if nearest is None:
                break
            tour.append(nearest)
            load += demands[nearest]
            demands_met[nearest] = True
            current_city_index = nearest
        tour.append(0)  # Return to depot
        routes.append(tour)
        if all(demands_met):
            break
    return routes

# Get tours using the heuristic
tours = nearest_neighbor_tsp(capacity, cities, demands)

# Calculate total travel cost for each tour
def calculate_tour_cost(tour, cities):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(cities[tour[i]], cities[tour[i+1]])
    return cost

# Display the results
total_cost = 0
for i, tour in enumerate(tours):
    tour_cost = calculate_tour_cost(tour, cities)
    total_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_multiplier:.2f}")