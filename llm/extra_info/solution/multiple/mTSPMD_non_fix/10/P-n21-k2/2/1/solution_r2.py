import math

# Coordinates of the cities including depot cities
coordinates = [
    (30, 40),  # Depot city 0
    (37, 52),  # Depot city 1
    (49, 49),  # City 2
    (52, 64),  # City 3
    (31, 62),  # City 4
    (52, 33),  # City 5
    (42, 41),  # City 6
    (52, 41),  # City 7
    (57, 58),  # City 8
    (62, 42),  # City 9
    (42, 57),  # City 10
    (27, 68),  # City 11
    (43, 67),  # City 12
    (58, 48),  # City 13
    (58, 27),  # City 14
    (37, 69),  # City 15
    (38, 46),  # City 16
    (61, 33),  # City 17
    (62, 63),  # City 18
    (63, 69),  # City 19
    (45, 35)   # City 20
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
        dist = euclidean_distance(current_city, city)
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
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cumulative_cost}")