import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33),
    16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Create a dictionary of dictionaries to store distances between cities
distances = {c1: {c2: euclidean_distance(cities[c1], cities[c2]) for c2 in cities if c1 != c2} for c1 in cities}

def nearest_neighbor_solution(starting_city, cities, distances):
    tour = [starting_city]
    current_city = starting_city
    used_cities = set(tour)

    while len(used_cities) < len(cities):
        next_city = min((city for city in cities if city not in used_cities), key=lambda x: distances[current_city][x])
        tour.append(next_city)
        current_city = next_city
        used_cities.add(next_city)

    return tour

# Initial tours for each robot (note: robots start from different depots)
robot_0_initial_tour = nearest_neighbor_solution(0, cities, distances)
robot_1_initial_tour = nearest_neighbor_solution(1, cities, distances)

# Function to calculate total distance of tour
def calculate_tour_cost(tour, distances):
    return sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

robot_0_total_cost = calculate_tour_cost(robot_0_initial_tour, distances)
robot_1_total_cost = calculate_tour_cost(robot_1_initial_tour, distances)
overall_cost = robot_0_total_cost + robot_1_total_cost

# Print output format
print("Robot 0 Tour:", robot_0_initial_tour)
print("Robot 0 Total Travel Cost:", round(robot_0_total_cost, 2))
print("\nRobot 1 Tour:", robot_1_initial_tour)
print("Robot 1 Total Travel Cost:", round(robot_1_total_cost, 2))
print("\nOverall Total Travel Cost:", round(overall_cost, 2))