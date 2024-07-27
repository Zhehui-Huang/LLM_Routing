import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor(start_index, cities, city_coords):
    tour = [start_index]
    unvisited = set(cities) - {start_index}
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(city_coords[tour[-1]], city_coords[x]))
        tour.append(next_arg_city)
        unvisited.remove(next_city)
    tour.append(start_index)  # completing the tour by returning to the start
    return tour

def calculate_total_cost(tour, coords):
    return sum(euclidean_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour)-1))

# Define city coordinates
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Assign robots and cities
robots = {
    0: [0],  # Robot 0 starts at Depot 0
    1: [1]   # Robot 1 starts at Depot 1
}
remaining_cities = set(range(2, 21))  # List of non-depot cities

for city in remaining_cities:
    closest_depot = min(robots.keys(), key=lambda k: euclidean_distance(coords[city], coords[robots[k][0]]))
    robots[closest_depot].append(city)

# Construct initial tours
tours = {}
for robot, cities in robots.items():
    tours[robot] = nearest_neighbor(robots[robot][0], cities, coords)

# Calculate tour costs
total_costs = {robot: calculate_total_cost(tour, coords) for robot, tour in tours.items()}
overall_total_cost = sum(total_costs.values())

# Print results
for robot, tour in tours.items():
    print(f'Robot {robot} Tour: {tour}')
    print(f'Robot {robot} Total Travel Cost: {total_costs[ish]')

print('Overall Total Travel Cost:', overall_total_cost)