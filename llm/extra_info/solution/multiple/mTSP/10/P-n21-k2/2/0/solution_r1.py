import math

# Coordinates of the cities (depost included as index 0)
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Calculate Euclidean distance between two cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Creating all pairs of cities with their distances
def create_distance_matrix(cities):
    n = len(cities)
    dist_matrix = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]
    return dist_matrix

dist_matrix = create_distance_matrix(cities)

# Heuristic: Split cities by sorting based on the coordinate sum (x+y)
def split_cities(cities):
    sorted_cities = sorted(range(1, len(cities)), key=lambda i: cities[i][0] + cities[i][1])
    mid = len(sorted_cities) // 2
    return sorted_cities[:mid], sorted_cities[mid:]

robot1_cities, robot2_cities = split_cities(cities)

# Utilizing a greedy algorithm (nearest neighbor) for tour generation
def generate_tour(start_city, city_indices, dist_matrix):
    tour = [0]  # starts at the depot
    visited = set(tour)
    last_city = start_city

    while len(visited) < len(city_indices) + 1:  # +1 for the depot
        next_city = min([(dist_matrix[last_city][i], i) for i in city_indices if i not in visited], default=(0, 0))[1]
        tour.append(next_city)
        visited.add(next_city)
        last_city = next_city

    tour.append(0)  # return to depot
    return tour

tour1 = generate_tour(0, robot1_cities, dist_matrix)
tour2 = generate_tour(0, robot2_cities, dist_matrix)

def calculate_tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

cost1 = calculate_tour_cost(tour1, dist_matrix)
cost2 = calculate_tour_cost(tour2, dist_matrix)

# Output the tour and costs for each robot and the combined cost
print("Robot 0 Tour:", tour1)
print("Robot 0 Total Travel Cost: {:.2f}".format(cost1))
print()
print("Robot 1 Tour:", tour2)
print("Robot 1 Total Travel Cost: {:.2f}".format(cost2))
print()
print("Overall Total Travel Cost: {:.2f}".format(cost1 + cost2))