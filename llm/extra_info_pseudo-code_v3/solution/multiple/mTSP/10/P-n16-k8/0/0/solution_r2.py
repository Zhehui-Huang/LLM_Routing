import math

# Cities and their coordinates (index corresponds to city number)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots
num_robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix
distance_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Nearest Neighbor Algorithm to create a tour starting and ending at the depot
def nearest_neighbor_tour(start, unvisited):
    tour = [start]
    current = start
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance_matrix[(current, x)])
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    tour.append(start)
    return tour

# Divide cities among robots
city_ids = list(cities.keys())[1:]  # excluding the depot
per_robot = len(city_ids) // num_robots
assignments = [city_ids[i * per_robot:(i + 1) * per_robot] for i in range(num_robots)]

# Handle leftover cities if number of cities isn't exactly divisible by number of robots
leftover = city_ids[num_robots * per_robot:]
for i, city in enumerate(leftover):
    assignments[i].append(city)

# Generate tours and calculate costs
robots_tours = []
total_overall_cost = 0

for robot_id, assigned_cities in enumerate(assignments):
    tour = nearest_neighbor_tour(0, assigned_cities.copy())
    tour_cost = sum(distance_matrix[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
    robots_tours.append((tour, tour_cost))
    total_overall_cost += tour_cost

# Output results
for robot_id, (tour, cost) in enumerate(robots_tours):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel A cost: {zzz}")