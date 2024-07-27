import math

# Calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Given coordinates of cities (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Dictionary to associate each robot with starting cities and the cities they need to cover.
team_assignments = {
    0: [0] + list(range(4, 10)),
    1: [1] + list(range(10, 15)),
    2: [2] + list(range(15, 19)),
    3: [3] + list(range(19, 22))
}

def nearest_neighbor_tour(start, cities):
    tour = [start]
    current_city = start
    unvisited = set(cities)
    unvisited.remove(start)

    # Construct the tour by always going to the nearest unvisited city
    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start)  # return to the starting city
    return tour

def calculate_total_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return cost

overall_total_cost = 0

for robot, cities in team_assignments.items():
    tour = nearest_neighbor_tour(cities[0], cities)
    tour_cost = calculate_total_tour_cost(tour)
    overall_total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")