import math

# Coordinates setup for each city
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Helper function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Heuristic: Nearest Neighbor Tour for robot given a starting point and specific cities
def nearest_neighbor_tour(start_point):
    unvisited = set(cities.keys()) - {start_point}
    tour = [start_point]
    while unvisited:
        nearest = min(unvisited, key=lambda city: euclidean_distance(tour[-1], city))
        tour.append(nearest)
        unvisited.remove(nearest)
    return tour

# Assign tours to robots ensuring that each robot starts from an initial depot
def generate_robots_tours(num_robots, start_depot):
    tour_length = len(cities) // num_robots
    remaining = list(cities.keys())[1:]  # all except the starting depot
    random.shuffle(remaining)
    tours = []

    for i in range(num_robots):
        if i == num_robots - 1:
            sub_tour_cities = remaining[i * tour_length:]  # take the rest for the last robot
        else:
            sub_tour_cities = remaining[i * tour_length:(i + 1) * tour_length]
        sub_tour = nearest_neighbor_tour(start_depot)  # start each tour at the depot
        for suburb in sub_tour_cities:
            sub_tour.append(suburb)  # append the cities to visit after the depot
        sub_tour.append(start_depot)  # return to depot at the end
        tours.append(sub_tour)
    return tours

# Calculate the travel cost for each tour
def calculate_total_cost(tours):
    total_cost = 0
    for tour in tours:
        tour_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        total_cost += tour_cost
    return total_cost

# Generate the tours
robots_tours = generate_robots_tours(num_robots, 0)

# Calculate costs
total_travel_cost = calculate_total_cost(robots_tours)

# Output the results
for idx, tour in enumerate(robots_tours):
    print(f"Robot {idx} Tour: {tour}")
    tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_travel_account:.2f}")