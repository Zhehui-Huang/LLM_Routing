import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, cities):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return tour_cost

def nearest_neighbor_tour(start_city_index, cities, unvisited):
    tour = [start_city_index]
    while unvisited:
        current_city = tour[-1]
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start_city_index)  # Complete the round trip to the depot
    return tour

def mTSP(n_robots, cities):
    depot_index = 0
    city_indices = list(cities.keys())
    city_indices.remove(depot_index)  # Removing the depot from cities to be visited
    robot_tours = []

    # Assigning cities to robots
    for i in range(n_robots):
        assigned_cities = city_indices[i::n_robots]
        unvisited = set(assigned_cities)
        if unvisited:
            tour = nearest_neighbor_tour(depot_index, cities, unvisited)
            robot_tours.append(tour)
    return robot_tours

# Set up cities and robot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Run the mTSP algorithm
tours = mTSP(2, cities)
overall_cost = 0

# Printing the tours and calculating the total costs
for i, tour in enumerate(tours):
    tour_cost = calculate_total_cost(tour, cities)
    overall_cost += tour_cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")