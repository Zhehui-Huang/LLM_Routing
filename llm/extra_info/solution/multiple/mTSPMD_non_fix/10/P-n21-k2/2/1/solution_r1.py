import math

# Coordinates of 21 cities including depot cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities based on coordinates. """
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_closest_city(current_city, unvisited):
    """ Return the closest unvisited city and the corresponding distance from the current city. """
    min_distance = float('inf')
    closest_city = None
    for city in unvisited:
        dist = euclidean_arguments(current_city, city)
        if dist < min_distance:
            min_distance = dist
            closest_city = city
    return closest_city, min_distance

def greedy_route(start_city):
    """ Create a route for a robot starting from a given city using a greedy approach. """
    tour = [start_city]
    unvisited = set(range(len(coordinates))) - {start_city}
    total_cost = 0
    current_city = start_city

    while unvisited:
        next_city, distance = find_closest_city(current_city, unvisited)
        tour.append(next_city)
        total_cost += distance
        current_city = next_city
        unvisited.remove(next_city)

    return tour, total_cost

# Given: two robots starting from two different depot cities
depots = [0, 1]

# Initialize robot tours and costs
tours = []
costs = []
total_cumulative_cost = 0

# Find and calculate tour for each robot
for depot in depots:
    tour, cost = greedy_route(depot)
    tours.append(tour)
    costs.append(cost)
    total_cumulative_cost += cost

# Output the details
for i, (tour, cost) in enumerate(zip(tours, costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Vol. Cost: {cost}")
    
print(f"Overall Total Total Costs: {total_cumulative_cost}")